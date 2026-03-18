from google.adk.agents import LlmAgent

summarizer_agent = LlmAgent(
    name="summarizer_agent",
    model="gemini-2.5-flash",
    instruction="""
You are a summarization agent.

Your job:
- Combine multiple research results into a clean final answer

Rules:
- Remove repetition
- Structure the answer clearly
- Use bullet points if needed
- Keep it concise but informative
"""
)
