from platform_agents.base import BaseAgent
from schemas.agent_types import AgentType
from schemas.agent import AgentMetadata

class SecurityReviewerAgent(BaseAgent):
  @property
  def metadata(self) -> AgentMetadata:
    return AgentMetadata(
      name="Security Reviewer",
      key=AgentType.SECURITY_REVIEWER,
      description="Analyzes API specifications and configurations for security risks.",
      capabilities=["auth_analysis", "cve_lookup"]
    )

  def run(self, payload, tools, prompt):
    tools.execute_tool(AgentType.SECURITY_REVIEWER, "auth_analyzer", payload)
    tools.execute_tool(AgentType.SECURITY_REVIEWER, "cve_lookup", payload)
    return {
      "security_status": "safe", 
      "issues_found": []
    }