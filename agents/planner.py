from google.adk.agents import LlmAgent

planner_agent = LlmAgent(
    name="planner_agent",
    model="gemini-2.5-flash",  
    instruction="""
You are a planning agent.

Break the query into ONLY 3 tasks maximum.

Rules:
- Output ONLY a numbered list
- Keep tasks broad and meaningful
- Avoid too many details
"""
)
