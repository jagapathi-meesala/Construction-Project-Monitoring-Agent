from contracts.tool_contract import Tool, ToolMetadata, ToolResult
from .common import require_mapping, number
class ProjectHealthTool(Tool):
    metadata = ToolMetadata("project-health", "Calculate a construction project health score from schedule, cost, safety, and completion indicators.", {"type":"object"})
    def validate(self, inputs):
        require_mapping(inputs)
        return {k:number(inputs,k,0,100) for k in ("schedule_progress","cost_health","safety_health","physical_progress")}
    def execute(self, x):
        score = round(sum(x.values())/4, 2)
        status = "green" if score >= 80 else "amber" if score >= 60 else "red"
        return ToolResult(True, {"health_score":score,"status":status,"components":x})
