---
title: From spreadsheet sprawl to a governed source of truth before AI
description: A logistics company wanted AI insights but had thirty versions of the truth in spreadsheets. We consolidated reporting into one governed model first, which is what made their AI initiative viable a quarter later.
publishDate: 2026-05-12
client: Logistics company (anonymized)
industry: Logistics
timeframe: 12 weeks
services:
  - Data platform to AI enablement
  - AI strategy and roadmaps
stack:
  - SQL
  - Python
  - Semantic modeling
  - Power BI
outcomes:
  - metric: Competing versions of key operational metrics
    before: 30+ diverging spreadsheets
    after: One governed model with a single definition per metric
  - metric: Leadership reporting cycle
    before: Weekly manual consolidation
    after: Self-serve dashboard on governed data
draft: false
---

## The problem

The company wanted "AI-driven insights" in their ops organization. The
discovery call made the real situation clear: thirty-plus spreadsheets with
diverging definitions of on-time percentage, no shared metric definitions, and
a weekly leadership meeting where the first twenty minutes were spent
reconciling whose number was right. No AI system can add value on top of that
- it would just generate confident nonsense faster.

## The approach

1. **Metric definition audit.** We cataloged every spreadsheet in circulation,
   traced each metric to its source system, and documented where definitions
   disagreed. This map alone changed several operational conversations.
2. **One governed model.** Consolidated the definitions into a single semantic
   model with certified metrics, lineage back to source systems, and a
   deprecation path for the shadow spreadsheets.
3. **Self-serve reporting on the governed layer.** Leadership dashboards now
   read from the certified metrics. The consolidation ritual disappeared from
   the leadership meeting.
4. **A realistic AI roadmap.** With trusted data in place, we sequenced the AI
   initiatives that were actually feasible: anomaly alerts on lane
   performance, then a Q&A layer over the governed metrics.

## The outcome

The metric-definition work was the least glamorous and most valuable part of
the engagement. The company now has a foundation where an AI feature can cite
a number that everyone agrees is correct - the precondition for anything
intelligent to be built on top.

Sequencing matters: the AI roadmap was written after the data foundation, not
before it, and that is why it will actually be delivered.
