from schemas.workflow import WorkflowDefinition, WorkflowStep
from orchestrator.orchestrator import AgentOrchestrator

# Define a workflow: Test Gen -> Security Review
workflow = WorkflowDefinition(
  name="Secure API Implementation",
  steps=[
    WorkflowStep(
      step_id="generate_tests",
      agent_type="test_generator",
      params={"spec_path": "api/users.yaml"}
    ),
    WorkflowStep(
      step_id="security_review",
      agent_type="security_reviewer",
      input_mapping={"spec": "generate_tests.test_plan"} 
    )
  ]
)

# Run
orchestrator = AgentOrchestrator()
result = orchestrator.run_workflow(workflow, {})
print(f"Workflow Status: {result.status}")
print(f"Results: {result.results}")