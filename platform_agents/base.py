from typing import Dict, Any
from abc import ABC, abstractmethod
from schemas.agent import AgentMetadata

class BaseAgent(ABC):

  @property
  @abstractmethod
  def metadata(self) -> AgentMetadata:
    pass

  @abstractmethod
  def run(self, payload: Dict[str, Any], tools, prompt: Dict[str, str]) -> Dict[str, Any]:
    pass
