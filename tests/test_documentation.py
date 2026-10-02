from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_docs():
 for p in ["README.md","AGENTS.md","DUTIES.md","RULES.md","SOUL.md","EXPLAINABILITY.md"]: assert (ROOT/p).is_file()
 x=(ROOT/"EXPLAINABILITY.md").read_text(); assert all(h in x for h in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"])
 assert "## Inputs\n" not in x and "## Decision\n" not in x and "## Limits\n" not in x
