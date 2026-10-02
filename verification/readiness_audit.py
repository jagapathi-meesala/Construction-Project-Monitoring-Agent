from pathlib import Path
import re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
HEADINGS=["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]
def sentences(s): return len([x for x in re.split(r"(?<=[.!?])\s+",s.strip()) if x])
def main():
 errors=[]
 for f in REQUIRED:
  if not (ROOT/f).is_file(): errors.append(f"missing {f}")
 x=(ROOT/"EXPLAINABILITY.md").read_text() if (ROOT/"EXPLAINABILITY.md").is_file() else ""
 for h in HEADINGS:
  if x.count(h)!=1: errors.append(f"heading count: {h}")
 for bad in ["## Inputs\n","## Decision\n","## Limits\n"]:
  if bad in x: errors.append(f"conflicting heading: {bad.strip()}")
 try:
  d=yaml.safe_load((ROOT/"agent.yaml").read_text())
  if d.get("spec_version")!="0.1.0": errors.append("spec_version is not 0.1.0")
  for s in d.get("skills",[]):
   if not (ROOT/"skills"/f"{s}.md").is_file(): errors.append(f"missing skill {s}")
 except Exception as e: errors.append(f"manifest parse error: {e}")
 if errors:
  print("READINESS AUDIT: FAIL"); print("\n".join(f"- {e}" for e in errors)); return 1
 print("READINESS AUDIT: PASS"); print(f"Checked {len(REQUIRED)} required root files, manifest, skills, and explainability headings."); return 0
if __name__=="__main__": sys.exit(main())
