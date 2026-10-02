from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_manifest_static_schema():
 d=yaml.safe_load((ROOT/"agent.yaml").read_text())
 assert d["spec_version"]=="0.1.0" and d["name"]=="construction-project-monitoring-agent"
 assert set(d["skills"])=={"project-progress-monitoring","construction-risk-monitoring","cost-schedule-analysis"}
 assert set(d["tools"])=={"project-health","schedule-progress","cost-variance","risk-register","safety-observation"}
 assert all((ROOT/"skills"/f"{s}.md").is_file() for s in d["skills"])
