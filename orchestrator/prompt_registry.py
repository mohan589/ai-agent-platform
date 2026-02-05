class PromptRegistry:
  def get_prompt(self, agent_type):
    return {
      "version": "v1.0",
      "template": f"You are {agent_type.value}. Output JSON only."
    }
