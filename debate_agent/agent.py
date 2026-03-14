import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

researcher_agent = Agent(
    name="researcher_agent",
    model="gemini-3-flash-preview",
    description="Agent A (The Researcher)",
    instruction=(
        "You are Agent A (The Researcher). Your task is to find and present three "
        "positive facts about the topic provided by the user. "
        "Use the Google Search tool to find accurate and up-to-date facts."
    ),
    tools=[google_search],
)

critic_agent = Agent(
    name="critic_agent",
    model="gemini-3-flash-preview",
    description="Agent B (The Critic)",
    instruction=(
        "You are Agent B (The Critic). Your task is to find and present three "
        "risks or downsides to the topic the user asked about. "
        "Respond critically after Agent A speaks."
    ),
    tools=[],
)

judge_agent = Agent(
    name="judge_agent",
    model="gemini-3-flash-preview",
    description="Agent C (The Judge)",
    instruction=(
        "You are Agent C (The Judge). Your task is to read the arguments presented "
        "by the Researcher and the Critic. Based on their points, make a final "
        "decision on who won the debate and explain why."
    ),
    tools=[],
)

root_agent = SequentialAgent(
    name="orchestrator",
    description=(
        "The Orchestrator that sequentially delegates to Agent A (Researcher) to present "
        "positive facts, then to Agent B (Critic) to present risks and downsides, "
        "and finally to Agent C (The Judge) to make the final decision."
    ),
    sub_agents=[researcher_agent, critic_agent, judge_agent],
)