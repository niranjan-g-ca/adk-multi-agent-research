from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

from main import run_agent
from agents.planner import planner_agent
from agents.research_agent import research_agent
from agents.summarizer_agent import summarizer_agent
from google.adk.sessions import InMemorySessionService
from fastapi import Header, HTTPException
from fastapi import Depends

app = FastAPI()
API_KEY = "mysecret123"  # move this to .env later

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {"message": "AI Research API is running 🚀"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "adk-research-api"
    }
# -----------------------
# FULL MULTI-AGENT FLOW
# -----------------------
@app.post("/research")
async def research(
    query_request: QueryRequest,
    x_api_key: str = Header(None)
):
    verify_api_key(x_api_key)
    user_query = query_request.query
    session_service = InMemorySessionService()

    try:
        plan = await run_agent(planner_agent, user_query, session_service)
    except Exception as e:
        return {"error": f"Planner failed: {str(e)}"}

    tasks = plan.split("\n") if plan else []
    results = []

    for i, task in enumerate(tasks):
        task = task.strip()
        if not task:
            continue

        try:
            result = await run_agent(research_agent, task, session_service)
            results.append(result if result else "No result returned")
        except Exception as e:
            results.append(f"Error in task {i+1}: {str(e)}")

        await asyncio.sleep(2)

    combined_text = "\n".join(results)

    try:
        final_answer = await run_agent(
            summarizer_agent,
            combined_text,
            session_service
        )
    except Exception as e:
        final_answer = f"Error during summarization: {str(e)}"

    return {
        "query": user_query,
        "plan": plan,
        "tasks": tasks,
        "results": results,
        "final_answer": final_answer
    }


# -----------------------
# LITE VERSION (FAST + STABLE)
# -----------------------
@app.post("/research-lite")
async def research_lite(
    query_request: QueryRequest,
    x_api_key: str = Header(None),
    _: None = Depends(verify_api_key)
):
    verify_api_key(x_api_key)

    user_query = query_request.query
    session_service = InMemorySessionService()

    try:
        result = await run_agent(
            research_agent,
            user_query,
            session_service
        )

        if not result:
            raise Exception("Empty response")

        return {
            "query": user_query,
            "mode": "lite",
            "source": "gemini",
            "answer": result
        }

    except Exception:
        # 🔥 FALLBACK RESPONSE
        mock_answer = """
Electric vehicles (EVs) generally reduce greenhouse gas emissions during operation compared to traditional vehicles. 
However, their overall environmental impact depends on factors such as battery production, electricity sources, 
and recycling processes. With advancements in renewable energy and battery technology, EVs are expected to become 
more environmentally sustainable in the future.
"""

        return {
            "query": user_query,
            "mode": "lite",
            "source": "mock",
            "answer": mock_answer.strip()
        }
