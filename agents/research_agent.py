from google.adk.agents import LlmAgent
from tools.search_tool import search_tool

research_agent = LlmAgent(
    name="research_agent",
    model="gemini-2.5-flash",
    tools=[search_tool],   # ✅ THIS IS KEY
    instruction="""
You are a research agent.

Your job:
- Use the search_tool to gather information
- Answer the query based on tool results

Rules:
- Always try to use the tool
- Keep answers concise
"""
)
