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
