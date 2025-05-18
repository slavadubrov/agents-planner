"""
This agent is responsible for determining the optimal workflow pattern for the agent system.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.load_web_page import load_web_page

from ... import MODEL
from ...modules.constants import STATE_WORKFLOW_PATTERN
from .prompt import (
    INSTRUCTION,
)

web_loader = FunctionTool(load_web_page)

workflow_designer_agent = LlmAgent(
    name="WorkflowDesignerAgent",
    model=MODEL,
    instruction=INSTRUCTION,
    description="Determines the optimal workflow pattern for the agent system.",
    tools=[web_loader],
    output_key=STATE_WORKFLOW_PATTERN,
)
