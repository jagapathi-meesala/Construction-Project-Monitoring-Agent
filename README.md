# Construction Project Monitoring Agent

A framework-independent OpenGAP 0.1.0 agent for monitoring construction project progress, cost, schedule, risks, and safety observations.

## Architecture
`agent.yaml` defines the portable manifest. `core/` provides framework-independent orchestration, `contracts/` defines the tool interface, `tools/` contains deterministic domain tools, `adapters/` exposes framework-neutral adapter entry points, and `verification/` provides readiness checks.

## Installation
Use Python 3.10+ and install `requirements.txt`. Set the required environment variables from `.env.example` before loading runtime settings.

## Configuration
Runtime configuration is read only from `ENVIRONMENT`, `LOG_LEVEL`, and `TOOL_TIMEOUT_SECONDS`; secrets are not stored in the repository.

## Tools
- project-health
- schedule-progress
- cost-variance
- risk-register
- safety-observation

## Skills
- project-progress-monitoring
- construction-risk-monitoring
- cost-schedule-analysis

## Usage
Instantiate `ToolRegistry`, register domain tools, and pass the registry to `ConstructionProjectMonitoringAgent`. Call `agent.inspect(tool_name, inputs)` for a structured result.

## Testing
Run `pytest -q` and `python verification/readiness_audit.py`.

## Portability
The core does not import OpenAI, CrewAI, Claude, or Lyzr. Adapter classes provide the same invocation contract for those environments, but external framework compatibility is not claimed as tested until those SDKs are actually exercised.

## Limitations
The agent analyzes supplied data and cannot independently verify physical work, invoices, contract compliance, or site conditions.
