from agents.base import BaseAgent
from schemas.agent_request import AgentType
from schemas.agent import AgentMetadata

class TestGeneratorAgent(BaseAgent):

  @property
  def metadata(self):
    return AgentMetadata(
      name="Test Generator Agent",
      key=AgentType.TEST_GENERATOR,
      description="Generates test cases for a given API specification.",
      version="1.0.0",
      capabilities=["test_generation", "swagger_parser"]
    )

  def run(self, payload, tools, prompt):
    tools.execute_tool(AgentType.TEST_GENERATOR, "swagger_parser", payload)
    return {
      "tests_generated": True,
      "confidence": 0.9
    }
