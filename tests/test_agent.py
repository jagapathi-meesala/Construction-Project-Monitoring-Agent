from core.agent_core import ToolRegistry, ConstructionProjectMonitoringAgent
from tools import ProjectHealthTool

def test_agent_execution():
 r=ToolRegistry(); r.register(ProjectHealthTool()); a=ConstructionProjectMonitoringAgent(r)
 out=a.inspect("project-health",{"schedule_progress":80,"cost_health":90,"safety_health":100,"physical_progress":70})
 assert out["success"] and out["data"]["status"]=="green"
