from abc import ABC, abstractmethod
from typing import Dict, Any
from pydantic import BaseModel

class ToolMetadata(BaseModel):
  name: str
  key: str
  description: str
  parameters: Dict[str, Any]

class BaseTool(ABC):
  @property
  @abstractmethod
  def metadata(self) -> ToolMetadata:
    pass

  @abstractmethod
  def execute(self, **kwargs) -> Any:
    pass