from __future__ import annotations
from typing import Any, Mapping
from contracts.tool_contract import Tool, ToolResult
class ToolRegistry:
    def __init__(self): self._tools: dict[str,Tool]={}
    def register(self,tool:Tool):
        name=tool.metadata.name
        if name in self._tools: raise ValueError(f"tool already registered: {name}")
        self._tools[name]=tool
    def discover(self): return sorted(self._tools)
    def get(self,name): return self._tools.get(name)
    def execute(self,name,inputs:Mapping[str,Any])->ToolResult:
        tool=self.get(name)
        if not tool: return ToolResult(False,error={"type":"unknown_tool","message":f"Unknown tool: {name}"})
        return tool.run(inputs)
class ConstructionProjectMonitoringAgent:
    def __init__(self,registry:ToolRegistry): self.registry=registry
    def inspect(self,tool_name:str,inputs:Mapping[str,Any])->dict[str,Any]:
        result=self.registry.execute(tool_name,inputs)
        return {"tool":tool_name,"success":result.success,"data":result.data,"error":result.error}
