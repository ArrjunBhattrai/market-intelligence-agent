## Problem

Early-stage founders and product teams spend significant time manually researching competitors,
market positioning, pricing models, and emerging trends.

Existing tools and chat-based LLMs provide generic, one-off answers that:
- lack source transparency
- cannot be rerun or updated over time
- do not track market changes
- do not store institutional knowledge

As a result, market research becomes repetitive, error-prone, and quickly outdated.

## Why This Is Not a Chatbot

This project is not a prompt-based chatbot.

It is a system composed of multiple specialized agents that:
- use real tools (web search, website parsing)
- store intermediate and historical data
- produce structured, source-backed outputs
- support repeatable and scheduled execution

The goal is to build a reliable market intelligence system, not generate one-off answers.

## High-Level Architecture

The system is designed as a multi-agent pipeline:

Input (startup idea / domain)
→ Research Agent (collects raw market data)
→ Analyst Agent (extracts patterns and pricing)
→ Writer Agent (produces structured reports)

All intermediate outputs are stored for reuse and future comparison.

## Agents Overview

### Research Agent
Responsible for discovering competitors and collecting raw market data using web-based tools.
Outputs factual, source-backed information only.

### Analyst Agent
Consumes raw research data and identifies pricing models, customer segments, and competitive patterns.

### Writer Agent
Generates structured, human-readable reports from analyzed data without introducing new facts.

## Tech Stack

- Language: Python
- Agent Orchestration: LangGraph
- LLM: Local models via Ollama (Qwen / DeepSeek)
- Web Search: DuckDuckGo / Tavily (free tier)
- Backend API: FastAPI
- Persistence: SQLite
- Vector Store: ChromaDB (local)
- UI (initial): Streamlit

All components are selected to be free, open-source, and easily replaceable.

## Development Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.api.main:app --reload


