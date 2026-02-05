from agents.base import BaseAgent
from schemas.agent_request import AgentType

class TestGeneratorAgent(BaseAgent):
  def run(self, payload, tools, prompt):
    tools.execute_tool(AgentType.TEST_GENERATOR, "swagger_parser", payload)
    return {
      "tests_generated": True,
      "confidence": 0.9
    }
