HEAD
# 🧠 Multi-Agent Research Assistant (Google ADK)

## 🚀 Overview

This project is a **multi-agent AI system** built using Google ADK that performs intelligent research by breaking down complex queries into tasks and executing them using specialized agents.

---

## 🏗️ Architecture

* **Planner Agent** → Breaks user query into structured tasks
* **Research Agent** → Uses tools to fetch relevant information
* **Summarizer Agent** → Combines results into a clean final answer

---

## ⚙️ Tech Stack

* Python
* Google ADK
* Gemini API
* Async processing

---

## 🔄 Workflow

1. User inputs a research query
2. Planner agent decomposes it into tasks
3. Research agent executes each task using tools
4. Summarizer agent generates final structured output

---

## 🛠️ Features

* Multi-agent orchestration
* Tool integration (custom search tool)
* Async execution with session handling
* Modular and extensible design

---

## ▶️ How to Run

```bash
git clone https://github.com/YOUR_USERNAME/adk-multi-agent-research.git
cd adk-multi-agent-research
python main.py
```

---

## 📌 Example

**Input:**

```
Impact of electric vehicles on environment
```

**Output:**

* Reduced emissions
* Battery production impact
* Energy source dependency
* Recycling considerations

---

## 🚧 Future Improvements

* Integrate real search APIs (Google/Wikipedia)
* Add FastAPI backend
* Build UI for interaction
* Add memory and context awareness

---

## 👨‍💻 Author

Niranjan

🧠 AI Research Assistant using Google ADK
🚀 Overview

This project is a multi-agent AI research system built using the Google ADK and Gemini models.

It takes a user query and:

Breaks it into structured research tasks

Gathers information using tools

Synthesizes a final summarized answer

🏗️ Architecture
User Query
   ↓
Planner Agent
   ↓
Task Breakdown
   ↓
Research Agent (with tools)
   ↓
Collected Results
   ↓
Summarizer Agent
   ↓
Final Answer
🤖 Agents
🧠 Planner Agent

Converts user query into actionable tasks

🔍 Research Agent

Uses tools (search_tool) to gather information

Executes each task independently

🧾 Summarizer Agent

Combines all research outputs into a final answer

🛠️ Tech Stack

Python

Google ADK

Gemini (gemini-2.5-flash)

Async execution (asyncio)

Custom tool integration

⚙️ Setup Instructions
1. Clone the repo
git clone <your-repo-url>
cd adk-research-agent
2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Add API Key

Create .env file:

GOOGLE_API_KEY=your_api_key_here
▶️ Run the Project
python main.py

Example input:

Impact of electric vehicles on environment
📸 Sample Output
--- PLANNING ---
1. Analyze benefits
2. Evaluate drawbacks
3. Summarize impact

--- RESEARCH ---
Task 1...
Task 2...
Task 3...

--- FINAL ANSWER ---
Electric vehicles reduce emissions but have lifecycle considerations...
⚠️ Known Limitations

Free-tier Gemini API has strict rate limits (5 requests/min)

Multi-agent architecture may hit quota limits

Tool responses may sometimes be partial

## 🌐 API Endpoints

### 🔍 POST /research
Full multi-agent pipeline (may hit API limits)

### ⚡ POST /research-lite
Fast single-call version with fallback support

### ❤️ GET /health
Check if API is running

---

## 🧪 API Testing

Tested using Postman for real-world API interaction.
