from policy_engine import PolicyEngine
from tool_router import ToolRouter
from prompt_registry import PromptRegistry
from eval_engine import EvalEngine
from audit_logger import AuditLogger
from agents.test_generator import TestGeneratorAgent
from agents.security_reviewer import SecurityReviewerAgent
from agents.compliance_auditor import ComplianceAuditorAgent

class AgentOrchestrator:
  def __init__(self):
    self.policy = PolicyEngine()
    self.tools = ToolRouter(self.policy)
    self.prompts = PromptRegistry()
    self.eval = EvalEngine()
    self.audit = AuditLogger()
    self.agents = {
      "test_generator": TestGeneratorAgent(),
      "security_reviewer": SecurityReviewerAgent(),
      "compliance_auditor": ComplianceAuditorAgent()
    }

  def execute(self, request):
    try:
      self.policy.validate_request(request)
      agent = self.agents[request.agent_type.value]
      prompt = self.prompts.get_prompt(request.agent_type)
      output = agent.run(request.payload, self.tools, prompt)
      status = self.eval.validate(output)
      if status == ExecutionStatus.NEEDS_HUMAN_REVIEW:
        approved = self.human_approval.request_approval(request.trace_id, output)
        if not approved:
          status = ExecutionStatus.FAILED
      result = {"status": status, "output": output}
    except Exception as e:
      result = {"status": "failed", "errors": [str(e)]}

    result["audit_id"] = self.audit.log(request, result)
    return result
