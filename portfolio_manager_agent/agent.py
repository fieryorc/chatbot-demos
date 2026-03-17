import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import McpToolset
from mcp import StdioServerParameters

import sys

mcp_toolset = McpToolset(
    connection_params=StdioServerParameters(
        command=sys.executable,
        args=["portfolio_manager_agent/run_mcp_server.py"],
    )
)

root_agent = Agent(
    name="portfolio_manager_agent",
    model="gemini-2.5-flash",
    description="Portfolio Manager Agent",
    instruction=(
        "You are a Portfolio Manager Agent. Your task is to analyze the stock provided by the user and "
        "recommend an action (Buy, Hold, or Sell). "
        "To make this recommendation, you should consider the recent news about the stock, the general market momentum, "
        "and the current stock price and historical trends. "
        "Use the provided MCP tools to fetch stock price, historical data, news, and market movers. "
        "Provide a well-reasoned explanation for your recommendation."
    ),
    tools=[mcp_toolset],
)

