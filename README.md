# Chatbot Demos

This repository contains examples and demonstrations of various chatbots and AI agents.

## Contents

- `debate_agent/`: A debate orchestration using the `google.adk.agents` framework. It includes a `SequentialAgent` demonstrating a debate flow between a Researcher (Agent A), a Critic (Agent B), and a Judge (Agent C).
- `portfolio_manager_agent/`: A portfolio manager agent that recommends actions (Buy/Hold/Sell) for a given stock symbol based on stock price, market news, and historical data. This agent interacts with tools supplied by `yfinance-mcp-server`.

## Setup

Follow the steps in [google adk documentation](https://google.github.io/adk-docs/get-started/quickstart/) to set up the python venv environment.

1. Make sure you have the required dependencies installed (e.g. `google-adk[agents]` and `yfinance-mcp-server`).
   ```bash
   pip install "google-adk[agents]" yfinance-mcp-server
   ```
2. Configure your environment variables in `.env`.
   - To use Vertex AI, set `GOOGLE_GENAI_USE_VERTEXAI=TRUE` and ensure you have run `gcloud auth application-default login`.
   - Or to use a Gemini API key directly, set `GEMINI_API_KEY="YOUR_KEY"`.
3. Try running the agents:
   - Run Portfolio Manager: `python run_portfolio_manager.py`
