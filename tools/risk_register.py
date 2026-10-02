from contracts.tool_contract import Tool, ToolMetadata, ToolResult
from .common import require_mapping, text, number
class RiskRegisterTool(Tool):
    metadata = ToolMetadata("risk-register", "Score a construction risk using probability and impact and assign a response band.", {"type":"object"})
    def validate(self, inputs):
        require_mapping(inputs)
        return {"risk":text(inputs,"risk"),"probability":number(inputs,"probability",1,5),"impact":number(inputs,"impact",1,5)}
    def execute(self,x):
        score=round(x["probability"]*x["impact"],2)
        band="low" if score<=4 else "medium" if score<=9 else "high" if score<=16 else "critical"
        return ToolResult(True,{"risk":x["risk"],"risk_score":score,"band":band,"recommended_response":"monitor" if band=="low" else "mitigate and assign owner" if band in {"medium","high"} else "escalate immediately"})
