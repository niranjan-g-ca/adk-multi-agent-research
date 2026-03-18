import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agents.planner import planner_agent
from agents.research_agent import research_agent
import asyncio
from agents.summarizer_agent import summarizer_agent


# ✅ Match ADK expected structure
class SimplePart:
    def __init__(self, text):
        self.text = text


class SimpleMessage:
    def __init__(self, role, content):
        self.role = role
        self.parts = [SimplePart(content)]


# ✅ Reusable agent runner
async def run_agent(agent, user_query, session_service):
    runner = Runner(
        app_name="research_app",
        agent=agent,
        session_service=session_service
    )

    session = await session_service.create_session(
        app_name="research_app",
        user_id="user_1"
    )

    response = runner.run(
        user_id="user_1",
        session_id=session.id,
        new_message=SimpleMessage(
            role="user",
            content=user_query
        )
    )

    final_output = None

    for event in response:
        if hasattr(event, "content") and event.content:
            for part in event.content.parts:
                if hasattr(part, "text") and part.text:
                    final_output = part.text

    return final_output


# ✅ Main orchestration
async def run():
    user_query = input("Enter your research query: ")

    session_service = InMemorySessionService()

    # 🧠 Step 1: Planner Agent
    print("\n--- PLANNING ---")
    plan = await run_agent(planner_agent, user_query, session_service)
    print(plan)

    # 🧠 Step 2: Convert plan into tasks
    tasks = plan.split("\n") if plan else []

    results = []

    # 🔍 Step 3: Research each task
    print("\n--- RESEARCH ---")

    for task in tasks:
        task = task.strip()

        if not task:
            continue

        print(f"\nTask: {task}")

        result = await run_agent(research_agent, task, session_service)

        print(f"Result: {result}")

        if result:
            results.append(result)
        await asyncio.sleep(12)

    # 🧾 Step 4: Combine results
    print("\n--- FINAL ANSWER ---")

    combined_text = "\n".join(results)

    print("\n--- SUMMARIZING ---")

    final_answer = await run_agent(
        summarizer_agent,
        combined_text,
        session_service
    )

    print("\n--- FINAL ANSWER ---")
    print(final_answer)


if __name__ == "__main__":
    asyncio.run(run())
