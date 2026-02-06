from tools.base import BaseTool, ToolMetadata
from typing import Any

class MongoReaderTool(BaseTool):
  @property
  def metadata(self) -> ToolMetadata:
    return ToolMetadata(
      name="Mongo Reader",
      key="mongo_reader",
      description="Reads schema information from a MongoDB collection.",
      parameters={
        "type": "object",
        "properties": {
          "connection_string": {"type": "string"},
          "database": {"type": "string"},
          "collection": {"type": "string"}
        },
        "required": ["database", "collection"]
      }
    )

  def execute(self, **kwargs) -> Any:
    # Simulating a schema read
    return {
      "collection": kwargs.get("collection"),
      "fields": ["_id", "created_at", "status", "payload"]
    }