from contracts.tool_contract import Tool, ToolMetadata, ToolResult
from .common import require_mapping, text
class SafetyObservationTool(Tool):
    metadata = ToolMetadata("safety-observation", "Classify a site safety observation and return a proportional follow-up priority.", {"type":"object"})
    def validate(self,inputs):
        require_mapping(inputs)
        severity=text(inputs,"severity").lower()
        if severity not in {"low","medium","high","critical"}: raise ValueError("severity must be low, medium, high, or critical")
        return {"observation":text(inputs,"observation"),"severity":severity}
    def execute(self,x):
        priority={"low":"routine","medium":"prompt","high":"urgent","critical":"immediate"}[x["severity"]]
        return ToolResult(True,{"observation":x["observation"],"severity":x["severity"],"follow_up_priority":priority})
