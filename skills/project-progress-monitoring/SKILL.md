---
name: project-progress-monitoring
description: Monitor construction project progress against planned milestones and identify schedule deviations.
---

# Project Progress Monitoring
## Purpose
Monitor planned versus actual physical progress and combine progress indicators into a project-health view.
## Inputs
Planned and actual progress percentages plus validated health components.
## Processing
The agent calculates schedule variance and an arithmetic health score; it does not invent field observations.
## Outputs
Structured progress variance and health status.
## Limitations
Percentages must be supplied by an authorized project source. The agent does not verify construction work on site.
## Expected behavior
Flag behind-schedule conditions and preserve the supplied measurements.
