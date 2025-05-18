"""
This agent is responsible for designing appropriate agents for each subtask.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.load_web_page import load_web_page

from ... import MODEL
from ...modules.constants import STATE_AGENT_DESCRIPTIONS
from .prompt import (
    INSTRUCTION,
)

web_loader = FunctionTool(load_web_page)

agent_designer_agent = LlmAgent(
    name="AgentDesignerAgent",
    model=MODEL,
    instruction=INSTRUCTION,
    description="Designs appropriate agents for each subtask.",
    tools=[web_loader],
    output_key=STATE_AGENT_DESCRIPTIONS,
)
