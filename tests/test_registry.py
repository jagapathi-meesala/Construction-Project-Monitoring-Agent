from core.agent_core import ToolRegistry
from tools import ScheduleProgressTool
def test_registry():
 r=ToolRegistry(); r.register(ScheduleProgressTool()); assert r.discover()==["schedule-progress"]
 assert r.execute("missing",{}).success is False
