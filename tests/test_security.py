from tools import ScheduleProgressTool, SafetyObservationTool

def test_invalid_type(): assert not ScheduleProgressTool().run({"planned_progress":"x","actual_progress":2}).success
def test_missing_field(): assert not ScheduleProgressTool().run({"planned_progress":2}).success
def test_bad_severity(): assert not SafetyObservationTool().run({"observation":"x","severity":"unknown"}).success
def test_long_input(): assert not SafetyObservationTool().run({"observation":"x"*501,"severity":"low"}).success
