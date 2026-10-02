from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT_FILES = [
    "agent.yaml",
    "SOUL.md",
    "README.md",
    "AGENTS.md",
    "DUTIES.md",
    "RULES.md",
    "EXPLAINABILITY.md",
    ".env.example",
    ".gitignore",
    "requirements.txt",
    "pytest.ini",
]

REQUIRED_DIRECTORIES = [
    "adapters",
    "config",
    "contracts",
    "core",
    "skills",
    "tools",
    "tests",
    "verification",
]

REQUIRED_HEADINGS = [
    "## Inputs and Data Sources",
    "## Decision and Reasoning",
    "## Limits and Constraints",
]

EXPECTED_SKILLS = {
    "project-progress-monitoring",
    "construction-risk-monitoring",
    "cost-schedule-analysis",
}

EXPECTED_TOOLS = {
    "project-health",
    "schedule-progress",
    "cost-variance",
    "risk-register",
    "safety-observation",
}


def fail(message):
    print(f"- {message}")
    return False


def main():
    errors = []

    # Root files
    for filename in REQUIRED_ROOT_FILES:
        if not (ROOT / filename).is_file():
            errors.append(f"missing root file {filename}")

    # Directories
    for dirname in REQUIRED_DIRECTORIES:
        if not (ROOT / dirname).is_dir():
            errors.append(f"missing directory {dirname}")

    # Manifest
    manifest_path = ROOT / "agent.yaml"

    if manifest_path.is_file():
        try:
            manifest = yaml.safe_load(manifest_path.read_text())
        except Exception as exc:
            errors.append(f"agent.yaml cannot be parsed: {exc}")
            manifest = {}

        if manifest.get("spec_version") != "0.1.0":
            errors.append("agent.yaml spec_version must be 0.1.0")

        if manifest.get("name") != "construction-project-monitoring-agent":
            errors.append("agent.yaml name is incorrect")

        actual_skills = set(manifest.get("skills", []))
        actual_tools = set(manifest.get("tools", []))

        if actual_skills != EXPECTED_SKILLS:
            errors.append(
                f"skill declarations mismatch: {sorted(actual_skills)}"
            )

        if actual_tools != EXPECTED_TOOLS:
            errors.append(
                f"tool declarations mismatch: {sorted(actual_tools)}"
            )

        # OpenGAP skill structure
        for skill in actual_skills:
            skill_file = ROOT / "skills" / skill / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"missing skill {skill}: {skill_file}")

        # OpenGAP tool structure
        for tool in actual_tools:
            tool_file = ROOT / "tools" / f"{tool}.yaml"
            if not tool_file.is_file():
                errors.append(f"missing tool {tool}: {tool_file}")

    # Explainability
    explainability = ROOT / "EXPLAINABILITY.md"

    if explainability.is_file():
        text = explainability.read_text()

        for heading in REQUIRED_HEADINGS:
            if text.count(heading) != 1:
                errors.append(
                    f"EXPLAINABILITY.md must contain exactly one '{heading}' heading"
                )

        for forbidden in [
            "## Inputs\n",
            "## Decision\n",
            "## Limits\n",
        ]:
            if forbidden in text:
                errors.append(
                    f"EXPLAINABILITY.md contains conflicting heading {forbidden.strip()}"
                )

        sections = {}
        for index, heading in enumerate(REQUIRED_HEADINGS):
            start = text.find(heading)
            if start == -1:
                continue

            next_positions = [
                text.find(h, start + len(heading))
                for h in REQUIRED_HEADINGS
                if text.find(h, start + len(heading)) != -1
            ]

            end = min(next_positions) if next_positions else len(text)
            sections[heading] = text[start + len(heading):end].strip()

        for heading, section in sections.items():
            sentences = [
                s.strip()
                for s in section.replace("\n", " ").split(".")
                if s.strip()
            ]
            if len(sentences) < 2:
                errors.append(
                    f"EXPLAINABILITY.md section '{heading}' needs at least two sentences"
                )

    # Skill frontmatter
    for skill in EXPECTED_SKILLS:
        skill_file = ROOT / "skills" / skill / "SKILL.md"

        if skill_file.is_file():
            content = skill_file.read_text()

            if not content.startswith("---\n"):
                errors.append(f"{skill}/SKILL.md missing YAML frontmatter")
            elif "\n---\n" not in content[4:]:
                errors.append(f"{skill}/SKILL.md has invalid YAML frontmatter")

    if errors:
        print("READINESS AUDIT: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("READINESS AUDIT: PASS")
    print("Checked root files, directories, manifest, skills, tools, and explainability.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
