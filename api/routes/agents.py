from fastapi import APIRouter
from orchestrator.orchestrator import AgentOrchestrator
from schemas.agent_request import AgentRequest

router = APIRouter()
orchestrator = AgentOrchestrator()

@router.post("/agents/execute")
def execute_agent(req: AgentRequest):
  return orchestrator.execute(req)
