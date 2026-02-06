from typing import Dict, Any
from schemas.workflow import WorkflowDefinition, WorkflowResult, WorkflowStatus
from orchestrator.registry import AgentRegistry

class WorkflowEngine:
  def __init__(self, registry: AgentRegistry, tools, prompts):
    self.registry = registry
    self.tools = tools
    self.prompts = prompts

  def run_workflow(self, workflow: WorkflowDefinition, initial_payload: Dict[str, Any]) -> WorkflowResult:
    results = {}
    context = initial_payload.copy()

    for step in workflow.steps:
      # 1. Prepare Payload via Input Mapping
      step_payload = step.params.copy()
      for input_key, source_key in step.input_mapping.items():
        if source_key in context:
             step_payload[input_key] = context[source_key]
        elif "." in source_key: # Support step_id.field syntax
             s_id, s_field = source_key.split(".", 1)
             if s_id in results and isinstance(results[s_id], dict):
                 step_payload[input_key] = results[s_id].get(s_field)

      # 2. Execute Agent
      agent = self.registry.get_agent(step.agent_type)
      prompt = self.prompts.get_prompt(step.agent_type)
      
      # Execute
      output = agent.run(step_payload, self.tools, prompt)
      
      # 3. Store Results
      results[step.step_id] = output
      if isinstance(output, dict):
        context.update(output)

    return WorkflowResult(
      workflow_id=workflow.name,
      status=WorkflowStatus.COMPLETED,
      results=results
    )