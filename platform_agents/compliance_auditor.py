from platform_agents.base import BaseAgent
from schemas.agent_types import AgentType
from schemas.agent import AgentMetadata

class ComplianceAuditorAgent(BaseAgent):
  @property
  def metadata(self) -> AgentMetadata:
    return AgentMetadata(
      name="Compliance Auditor",
      key=AgentType.COMPLIANCE_AUDITOR,
      description="Generates audit reports and validates compliance traces.",
      capabilities=["audit_report_generation", "trace_analysis"]
    )

  def run(self, payload, tools, prompt):
    tools.execute_tool(AgentType.COMPLIANCE_AUDITOR, "audit_report_generation", payload)
    tools.execute_tool(AgentType.COMPLIANCE_AUDITOR, "trace_analysis", payload) 
    return {
      "compliant": True,
      "audit_id": "AUD-123456"
    }