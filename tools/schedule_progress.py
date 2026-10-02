from contracts.tool_contract import Tool, ToolMetadata, ToolResult
from .common import require_mapping, number
class ScheduleProgressTool(Tool):
    metadata = ToolMetadata("schedule-progress", "Compare planned and actual construction progress and calculate schedule variance.", {"type":"object"})
    def validate(self, inputs):
        require_mapping(inputs)
        return {k:number(inputs,k,0,100) for k in ("planned_progress","actual_progress")}
    def execute(self, x):
        variance=round(x["actual_progress"]-x["planned_progress"],2)
        return ToolResult(True,{"planned_progress":x["planned_progress"],"actual_progress":x["actual_progress"],"variance_percentage_points":variance,"status":"ahead" if variance>0 else "on-track" if variance==0 else "behind"})
