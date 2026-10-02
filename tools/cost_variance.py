from contracts.tool_contract import Tool, ToolMetadata, ToolResult
from .common import require_mapping, number
class CostVarianceTool(Tool):
    metadata = ToolMetadata("cost-variance", "Calculate construction budget variance and cost performance ratio.", {"type":"object"})
    def validate(self, inputs):
        require_mapping(inputs)
        budget=number(inputs,"budget",0.000001); actual=number(inputs,"actual_cost",0)
        if actual < 0: raise ValueError("actual_cost cannot be negative")
        return {"budget":budget,"actual_cost":actual}
    def execute(self,x):
        variance=round(x["budget"]-x["actual_cost"],2)
        ratio=round(x["budget"]/x["actual_cost"],4) if x["actual_cost"] else None
        return ToolResult(True,{"variance":variance,"variance_percent":round(variance/x["budget"]*100,2),"budget_to_actual_ratio":ratio,"status":"under-budget" if variance>0 else "on-budget" if variance==0 else "over-budget"})
