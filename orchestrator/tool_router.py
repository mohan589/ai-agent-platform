from typing import Any, Dict

from orchestrator.policy_engine import AgentType, PolicyEngine

class ToolRouter:
  """Executes tools only if policy allows them."""

  def __init__(self, policy_engine: PolicyEngine):
    self.policy_engine = policy_engine

  def execute_tool(self, agent_type: AgentType, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if tool_name not in self.policy_engine.allowed_tools(agent_type):
      raise PermissionError(f"Tool '{tool_name}' not allowed for {agent_type}")

    return {  
      "tool": tool_name,
      "result": "ok",
      "params": params,
    }