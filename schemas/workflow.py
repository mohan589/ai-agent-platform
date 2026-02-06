from pydantic import BaseModel, Field
from typing import List, Dict, Any
from enum import Enum

class WorkflowStatus(str, Enum):
  PENDING = "pending"
  RUNNING = "running"
  COMPLETED = "completed"
  FAILED = "failed"

class WorkflowStep(BaseModel):
  step_id: str
  agent_type: str  # e.g., "test_generator"
  input_mapping: Dict[str, str] = Field(default_factory=dict) # Map output of prev step to input of this
  params: Dict[str, Any] = Field(default_factory=dict)
    
class WorkflowDefinition(BaseModel):
  name: str
  steps: List[WorkflowStep]

class WorkflowResult(BaseModel):
  workflow_id: str
  status: WorkflowStatus
  results: Dict[str, Any]  # step_id -> result