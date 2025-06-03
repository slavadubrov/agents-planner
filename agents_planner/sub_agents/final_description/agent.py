"""
This agent is responsible for creating a comprehensive markdown description of the agent system.
"""

from crewai_tools import FileWriterTool
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.crewai_tool import CrewaiTool
import os

from ... import MODEL
from ...modules.constants import STATE_FINAL_DESCRIPTION
from .prompt import (
    INSTRUCTION,
)

DOCS_DIR = "docs"
os.makedirs(DOCS_DIR, exist_ok=True)

save_markdown_tool = CrewaiTool(
    name="save_markdown",
    description="Save markdown content to a file on disk.",
    tool=FileWriterTool(),
)

final_description_agent = LlmAgent(
    name="FinalDescriptionAgent",
    model=MODEL,
    instruction=INSTRUCTION,
    description="Creates a comprehensive markdown description of the agent system.",
    tools=[save_markdown_tool],
    output_key=STATE_FINAL_DESCRIPTION,
)

