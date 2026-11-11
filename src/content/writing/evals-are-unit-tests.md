---
title: Evals are unit tests for non-deterministic code
description: If a prompt change can silently regress your product, you do not have an engineering process - you have a demo. A practical starting point for LLM evaluation suites.
publishDate: 2026-11-11
tags:
  - evals
  - LLMOps
draft: false
---

Ask an engineering team how they know a code change is safe, and they will
describe tests that run on every merge. Ask them how they know a prompt change
is safe, and the answer is usually a shrug and a manual smoke test.

A prompt is code. An index configuration is code. A retrieval filter is code.
None of them are deterministic, but all of them can regress your product, and
none of them deserve to be changed on vibes.

## The smallest useful eval suite

The word "evals" intimidates people into doing nothing. The smallest useful
suite is three files and a script:

1. **A golden set.** Twenty to fifty real questions your users actually ask,
   each with the source documents or reference answer that a good response
   must use. Mine them from support tickets, search logs, or user sessions.
   Imperfect and real beats curated and fictional.
2. **A runner.** For each question: retrieve, generate, record the answer and
   the retrieved sources. A script that produces a JSON report is fine.
3. **Assertions.** Start with checks that need no LLM judgment: was the
   expected source document retrieved? Do numbers in the answer match the
   source data? Does the response violate a length or format contract? Add
   LLM-as-judge scoring only after these pass deterministically.

Wire it into CI so it runs on every change to prompts, index configs, and
retrieval logic. A regression blocks the merge, exactly like a failing unit
test would.

## What to measure first

Retrieval quality before answer quality. If the right document is not in the
context window, no amount of model quality will save the answer, and if it is,
many failures disappear without touching anything. Track:

- **Hit rate:** how often the expected source appears in retrieved context.
- **Contract violations:** format, length, and structured-output failures.
- **Grounding:** whether claims in the answer trace to the retrieved sources.

Perception metrics - "the answer feels good" - come later, judged by humans
on a sample, not by another model on the whole set.

## The compounding effect

The first version of the suite is not the point. The point is that it exists
and runs automatically, because every improvement to it - new questions,
harder edge cases, better assertions - makes every future change cheaper to
ship. Teams that skip this stage pay for it forever in manual verification,
and eventually in one very public, very silent regression.

The teams that ship LLM features reliably are not the ones with the best
prompts. They are the ones who can answer: "how do you know it still works
after this change?"
