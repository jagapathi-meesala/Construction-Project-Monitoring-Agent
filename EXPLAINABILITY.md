## Inputs and Data Sources
The agent accepts structured project inputs such as planned progress, actual progress, approved budget, actual cost, documented risk probability and impact, and recorded safety observations. Data sources are expected to be supplied by the user or an authorized project system through the tool input mechanisms; the current implementation does not fetch or invent field data.

### Input Requirements
Progress and health values are percentages from 0 to 100, budget values are non-negative numeric amounts, and risk probability and impact use a 1-to-5 scale. Safety observations require a documented observation and one of the supported severity levels.

## Decision and Reasoning
The agent makes decisions by applying explicit deterministic rules to validated inputs rather than using hidden model scores. Schedule variance is actual progress minus planned progress, cost variance is budget minus actual cost, risk score is probability multiplied by impact, and project health is the arithmetic mean of the four supplied health components.

### Rules Applied
A positive schedule variance is classified as ahead, zero as on-track, and negative as behind. Project health is green at 80 or above, amber from 60 through 79.99, and red below 60; risk bands are derived from the calculated risk score.

### Expected Outputs
Each tool returns a structured success flag plus data or an error object. Outputs are intended for monitoring and prioritization, not automatic contractual, engineering, or safety approval.

## Limits and Constraints
The implementation cannot independently verify physical construction progress, invoices, measurements, site conditions, weather, contracts, or regulatory compliance. It also does not claim live integrations with OpenAI, CrewAI, Claude Code, or Lyzr because the adapter layer is framework-neutral and has not been exercised through those external SDKs here.

### Failure Handling
Malformed, missing, out-of-range, or unsafe input values are rejected through validation and returned as structured validation errors where possible. Runtime exceptions are converted into structured execution errors so callers can distinguish tool failure from a valid project result.

### Constraints
The current implementation is deterministic and local, with no hardcoded secrets or production credentials. It is not a substitute for a qualified construction professional, site safety officer, project controls process, or approved enterprise source of truth.
