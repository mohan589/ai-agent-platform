from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class AgentType(str, Enum):
  TEST_GENERATOR = "test_generator"
  SECURITY_REVIEWER = "security_reviewer"
  COMPLIANCE_AUDITOR = "compliance_auditor"

class AgentMetadata(BaseModel):
  name: str
  key: AgentType
  description: str
  version: str = "1.0.0"
  capabilities: List[str] = Field(default_factory=list)