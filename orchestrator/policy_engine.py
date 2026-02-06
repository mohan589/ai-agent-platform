from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional
import uuid

from schemas.agent_types import AgentType

from schemas.agent_request import AgentRequest, ExecutionStatus, AgentResult

class PolicyEngine:
  """Defines what agents are allowed to do."""

  def validate_request(self, request: AgentRequest) -> None:
    if request.agent_type == AgentType.SECURITY_REVIEWER:
      if "auth_config" not in request.payload:
        raise ValueError("Security agent requires auth_config")

  def allowed_tools(self, agent_type: AgentType) -> List[str]:
    policy_map = {
      AgentType.TEST_GENERATOR: ["swagger_parser", "mongo_reader", "repo_writer"],
      AgentType.SECURITY_REVIEWER: ["dependency_scanner", "auth_analyzer", "cve_lookup"],
      AgentType.COMPLIANCE_AUDITOR: ["log_reader"],
    }
    return policy_map.get(agent_type, [])