from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional
import uuid

class AgentType(str, Enum):
  TEST_GENERATOR = "test_generator"
  SECURITY_REVIEWER = "security_reviewer"
  COMPLIANCE_AUDITOR = "compliance_auditor"

class ExecutionStatus(str, Enum):
  SUCCESS = "success"
  FAILED = "failed"
  NEEDS_HUMAN_REVIEW = "needs_human_review"

@dataclass
class AgentRequest:
  agent_type: AgentType
  payload: Dict[str, Any]
  user_id: str
  trace_id: str = str(uuid.uuid4())

@dataclass
class AgentResult:
  status: ExecutionStatus
  output: Optional[Dict[str, Any]]
  errors: Optional[List[str]] = None
  audit_id: Optional[str] = None

class PolicyEngine:
  """Defines what agents are allowed to do."""

  def validate_request(self, request: AgentRequest) -> None:
    if request.agent_type == AgentType.SECURITY_REVIEWER:
      if "auth_config" not in request.payload:
        raise ValueError("Security agent requires auth_config")

  def allowed_tools(self, agent_type: AgentType) -> List[str]:
    policy_map = {
      AgentType.TEST_GENERATOR: ["swagger_parser", "mongo_reader", "repo_writer"],
      AgentType.SECURITY_REVIEWER: ["dependency_scanner", "auth_analyzer"],
      AgentType.COMPLIANCE_AUDITOR: ["log_reader"],
    }
    return policy_map.get(agent_type, [])