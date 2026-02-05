from schemas.agent_request import ExecutionStatus

class EvalEngine:
  def validate(self, output):
    if not output:
      return ExecutionStatus.FAILED
    if output.get("confidence", 0) < 0.7:
      return ExecutionStatus.NEEDS_HUMAN_REVIEW
    return ExecutionStatus.SUCCESS
