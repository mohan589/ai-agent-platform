from enum import Enum

class AgentType(str, Enum):
  TEST_GENERATOR = "test_generator"
  SECURITY_REVIEWER = "security_reviewer"
  COMPLIANCE_AUDITOR = "compliance_auditor"
