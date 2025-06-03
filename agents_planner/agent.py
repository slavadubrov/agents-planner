"""
This is the main agent that orchestrates the planning process.
"""

import typer
from dotenv import load_dotenv
from pathlib import Path
from google.adk.agents.sequential_agent import SequentialAgent

from .sub_agents.agent_designer.agent import agent_designer_agent
from .sub_agents.final_description.agent import final_description_agent
from .sub_agents.task_analyzer.agent import task_analyzer_agent
from .sub_agents.workflow_designer.agent import workflow_designer_agent
from .modules.constants import STATE_FINAL_DESCRIPTION, STATE_TASK

load_dotenv()

app = typer.Typer()
planning_agents = SequentialAgent(
    name="PlanningAgents",
    sub_agents=[
        task_analyzer_agent,
        agent_designer_agent,
        workflow_designer_agent,
        final_description_agent,
    ],
)

root_agent = planning_agents


def run_and_save(task: str, file_path: str = "docs/agent_system_description.md"):
    """Run the planning agents and save the final markdown report."""
    state = {STATE_TASK: task}
    result = planning_agents.run(state)
    markdown = result.get(STATE_FINAL_DESCRIPTION)
    if markdown:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown)
    return result


@app.command()
def run(task: str, file_path: str = "docs/agent_system_description.md"):
    """Run the agent planner and save the report to a markdown file."""
    run_and_save(task, file_path)
