from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_static_schema():
    manifest = yaml.safe_load((ROOT / "agent.yaml").read_text())

    assert manifest["spec_version"] == "0.1.0"
    assert manifest["name"] == "construction-project-monitoring-agent"

    expected_skills = {
        "project-progress-monitoring",
        "construction-risk-monitoring",
        "cost-schedule-analysis",
    }

    expected_tools = {
        "project-health",
        "schedule-progress",
        "cost-variance",
        "risk-register",
        "safety-observation",
    }

    assert set(manifest["skills"]) == expected_skills
    assert set(manifest["tools"]) == expected_tools

    for skill in manifest["skills"]:
        assert (ROOT / "skills" / skill / "SKILL.md").is_file()

    for tool in manifest["tools"]:
        assert (ROOT / "tools" / f"{tool}.yaml").is_file()
