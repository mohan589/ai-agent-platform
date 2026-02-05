from typing import Dict, Any

class BaseAgent:
  def run(self, payload: Dict[str, Any], tools, prompt: Dict[str, str]) -> Dict[str, Any]:
    raise NotImplementedError
