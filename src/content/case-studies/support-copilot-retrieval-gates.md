---
title: Cutting hallucinations in a support copilot with retrieval quality gates
description: A B2B software company's internal support copilot answered confidently from the wrong documents. We rebuilt retrieval around freshness and permission-aware filters, with evals that block regressions at deploy time.
publishDate: 2026-07-20
client: B2B SaaS company (anonymized)
industry: Software
timeframe: 6 weeks
services:
  - RAG and evaluation pipelines
  - LLM application architecture
stack:
  - Python
  - Vector database
  - OpenAI API
  - CI-based eval runner
outcomes:
  - metric: Answers citing stale or unauthorized sources
    before: ~1 in 5 in spot checks
    after: Zero detected across the eval suite
  - metric: Support agent time to a confident answer
    before: Frequent manual verification of AI output
    after: Verification only for flagged or low-confidence answers
draft: false
---

## The problem

The company gave its support team an internal copilot over product docs,
release notes, and historical tickets. Adoption collapsed within a month:
agents learned the hard way that the copilot would confidently cite a version
of a document that had been superseded, or pull from an internal-only source
agents were not supposed to rely on. The model was not the problem. The
retrieval layer had no concept of freshness or permissions.

## The approach

1. **Document lifecycle metadata first.** Every indexed document now carries
   version, effective date, and audience. The retriever filters on these
   before similarity ranking, so superseded and unauthorized documents never
   reach the prompt.
2. **Built a golden question set.** With the support leads, we captured real
   agent questions across product areas, each with the correct source
   documents. Retrieval quality is scored against this set on every change.
3. **Wired evals into deployment.** Index updates and prompt changes run the
   eval suite in CI. A drop in retrieval quality blocks the deploy. Agents
   rate answers in the flow of work, and those ratings flow back into the
   golden set.

## The outcome

Trust returned because correctness became observable. Agents stopped
re-verifying every answer manually and instead verify only what the system
flags. The support leads' favorite feature is not the copilot itself - it is
the dashboard that shows retrieval quality trending over time.

The lesson: hallucination remediation is mostly retrieval governance, not
prompt engineering.
