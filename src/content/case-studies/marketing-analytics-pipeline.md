---
title: Rebuilding a marketing analytics pipeline to feed AI-assisted reporting
description: A consumer-goods company's weekly reporting lived in a fragile SSAS and Excel stack. We rebuilt the pipeline with quality gates, then layered an LLM narrative service on top that executives actually trust.
publishDate: 2026-09-15
client: Mid-size consumer goods company (anonymized)
industry: Consumer goods / retail
timeframe: 10 weeks
services:
  - Data platform to AI enablement
  - RAG and evaluation pipelines
stack:
  - SQL
  - SSAS
  - Python
  - dbt-style transformations
  - OpenAI API
  - Power BI
outcomes:
  - metric: Weekly reporting prep time
    before: 2 days of manual assembly
    after: Fully automated, zero-touch
  - metric: Data quality issues reaching reports
    before: Found by executives, after publication
    after: Caught by pipeline gates, before publication
  - metric: Time to draft weekly commentary
    before: 4-6 hours of analyst time
    after: 15 minutes of review and edit
draft: false
---

## The problem

The company's weekly trading reports were assembled by hand: numbers from a
SSAS cube, pivoted in Excel, annotated by an analyst, and sent to executives.
Every week carried the risk of a stale extract or a broken join reaching the
CEO's inbox. Leadership wanted "AI summaries", but the honest prerequisite was
a pipeline nobody had to babysit.

## The approach

We treated the LLM layer as the last mile, not the first one.

1. **Rebuilt the pipeline first.** Consolidated the fragmented extracts into a
   single transformation flow with explicit quality gates: row counts, freshness
   checks, and reconciliation against source-of-truth totals. Bad data now
   fails loudly before publication instead of quietly reaching the report.
2. **Structured the data for narration.** The LLM does not read raw tables. It
   receives a compact, pre-computed brief: the week's movements, rankings, and
   anomalies, already validated by the gates.
3. **Added the narrative layer.** A service turns the validated brief into
   first-draft commentary. The analyst reviews, edits, and approves. The eval
   suite checks that generated numbers always match the brief - any mismatch is
   a build failure.

## The outcome

Weekly reporting is now automated end to end, with the analyst role shifted
from assembly to review. The LLM drafts the commentary in minutes; a human
still signs off. Because the quality gates run before generation, the failure
mode went from "wrong number in the CEO report" to "pipeline stops and pages
the team".

The pattern generalizes: AI on top of untrusted data is a liability, but AI on
top of gated data compounds the value of the platform you already built.
