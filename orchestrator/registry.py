import pkgutil
import importlib
import inspect
from typing import Dict, Type
from agents.base import BaseAgent

class AgentRegistry:
  def __init__(self):
    self._agents: Dict[str, Type[BaseAgent]] = {}
    self.discover_agents()

  def discover_agents(self):
    """Auto-discover agent classes in the 'agents' package."""
    import agents
    package = agents
      
    # Iterate over all modules in the 'agents' package
    for _, name, _ in pkgutil.iter_modules(package.__path__):
      module_name = f"{package.__name__}.{name}"
      try:
        module = importlib.import_module(module_name)
      except ImportError:
        continue
          
      # Find classes that inherit from BaseAgent
      for _, obj in inspect.getmembers(module):
        if (inspect.isclass(obj) and 
            issubclass(obj, BaseAgent) and 
            obj is not BaseAgent):
                  
        try:
          # Instantiate to get metadata key
          # Note: This assumes __init__ takes no args or we handle it.
          # For this platform, agents init is empty/simple.
          instance = obj()
          self._agents[instance.metadata.key] = obj
        except Exception:
          # Skip if we can't instantiate or access metadata
          continue

  def get_agent(self, key: str) -> BaseAgent:
    agent_class = self._agents.get(key)
    if not agent_class:
      raise ValueError(f"Agent '{key}' not found in registry.")
    return agent_class()