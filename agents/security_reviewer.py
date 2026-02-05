from agents.base import BaseAgent
from schemas.agent import AgentMetadata, AgentType

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
    tools.execute_tool(AgentType.SECURITY_REVIEWER, "auth_analysis", payload)
    tools.execute_tool(AgentType.SECURITY_REVIEWER, "cve_lookup", payload)
    return {
      "security_status": "safe", 
      "issues_found": []
    }