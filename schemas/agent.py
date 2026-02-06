from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

from schemas.agent_types import AgentType

class AgentMetadata(BaseModel):
  name: str
  key: AgentType
  description: str
  version: str = "1.0.0"
  capabilities: List[str] = Field(default_factory=list)