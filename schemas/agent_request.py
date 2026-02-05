from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, Optional, List
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
