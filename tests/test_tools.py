from tools import *
def test_schedule(): assert ScheduleProgressTool().run({"planned_progress":60,"actual_progress":55}).data["status"]=="behind"
def test_cost(): assert CostVarianceTool().run({"budget":1000,"actual_cost":900}).data["variance"]==100
def test_risk(): assert RiskRegisterTool().run({"risk":"delay","probability":4,"impact":5}).data["band"]=="critical"
def test_safety(): assert SafetyObservationTool().run({"observation":"blocked exit","severity":"high"}).data["follow_up_priority"]=="urgent"
