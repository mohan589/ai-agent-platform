class PromptRegistry:
  def get_prompt(self, agent_type):
    agent_type_str = agent_type.value if hasattr(agent_type, "value") else agent_type
    return {
      "version": "v1.0",
      "template": f"You are {agent_type_str}. Output JSON only."
    }
