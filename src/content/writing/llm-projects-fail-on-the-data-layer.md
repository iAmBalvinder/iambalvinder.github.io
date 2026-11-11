---
title: Most LLM projects fail on the data layer, not the model layer
description: Teams debug prompts when they should be auditing retrieval. The failure mode I see most in stalled LLM projects is a data problem wearing a model costume.
publishDate: 2026-11-11
tags:
  - LLM engineering
  - data quality
draft: false
---

A pattern repeats across almost every stalled LLM project I have reviewed. The
demo worked. The prototype answered questions impressively. Then the feature
met real data and real users, and the team spent three months tuning prompts
while the actual defect sat one layer down: the retrieval corpus.

## What the failure looks like

The user asks a question and gets a confident, well-written, wrong answer.
The team's instinct is to change the prompt. Add more instructions. Tell the
model to be careful. Sometimes that helps for a week. Then a document gets
updated and the answers quietly rot again.

The real questions are downstream of the prompt:

- Which version of the document did the retriever surface, and was it current?
- Did the chunk that ranked highest contain the answer, or just share
  vocabulary with the question?
- When the underlying data changed, did the index update - or is the system
  answering from last month's snapshot?

None of these are model questions. They are data engineering questions, and
they have been solved before, just under different names: freshness, lineage,
quality gates, reconciliation.

## Why data engineers have a head start

Everything I learned running analytics platforms applies directly to LLM
systems, because an LLM application is a data pipeline with an unusually
opinionated consumer at the end.

**Freshness beats cleverness.** A retrieval index that is stale by two weeks
will produce more wrong answers than any prompt can rescue. Track index lag
like you track warehouse load times.

**Quality gates go before the consumer.** You do not publish a dashboard
before reconciling totals. Do not let an LLM narrate data that has not passed
the same reconciliation. The gate is cheaper than the apology.

**Lineage answers the question users actually ask.** "Where did this answer
come from?" should be answerable to the source document and its version. If
you cannot trace it, you cannot trust it, and neither can your users.

**The demo lies.** Dashboards look great in demos on curated data. So do LLM
products. Both are judged by what happens on the messy data days later.

## What to do first

If your LLM feature is stuck, audit the corpus before you touch the prompt.
Write down what every document is, when it was last valid, who can rely on it,
and how it gets into the index. Instrument retrieval so you can see what got
surfaced for a given answer. Within a week you will usually find the wrong
answers are not random - they cluster around a handful of stale, duplicated,
or mis-scoped documents.

Fix the data layer, and the model layer usually turns out to be good enough.
It was always going to be.
