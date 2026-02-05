import uuid

class AuditLogger:
  def log(self, request, result):
    audit_id = str(uuid.uuid4())
    print(f"[AUDIT] {audit_id} | {request.agent_type} | {result.status}")
    return audit_id
