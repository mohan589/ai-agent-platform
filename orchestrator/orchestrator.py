from orchestrator.registry import AgentRegistry
from orchestrator.policy_engine import PolicyEngine
from orchestrator.tool_router import ToolRouter
from orchestrator.prompt_registry import PromptRegistry
from orchestrator.eval_engine import EvalEngine
from orchestrator.audit_logger import AuditLogger
from orchestrator.workflow_engine import WorkflowEngine

class AgentOrchestrator:
  def __init__(self):
    self.policy = PolicyEngine()
    self.tools = ToolRouter(self.policy)
    self.prompts = PromptRegistry()
    self.eval = EvalEngine()
    self.audit = AuditLogger()
    self.registry = AgentRegistry()
    self.workflow_engine = WorkflowEngine(self.registry, self.tools, self.prompts)

  def run_workflow(self, workflow_def, initial_payload):
    return self.workflow_engine.run_workflow(workflow_def, initial_payload)

  def execute(self, request):
    try:
      self.policy.validate_request(request)
      agent = self.registry.get_agent(request.agent_type)
      prompt = self.prompts.get_prompt(request.agent_type)
      output = agent.run(request.payload, self.tools, prompt)
      status = self.eval.validate(output)
      if status == "NEEDS_HUMAN_REVIEW":
        approved = self.human_approval.request_approval(request.trace_id, output)
        if not approved:
          status = "FAILED"
      result = {"status": status, "output": output}
    except Exception as e:
      result = {"status": "failed", "errors": [str(e)]}

    result["audit_id"] = self.audit.log(request, result)
    return result
