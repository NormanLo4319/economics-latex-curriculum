---
name: superpower
description: Agentic software development methodology and execution framework based on obra/superpowers. Use when planning, designing, architecting, or implementing software features, running test-driven development (TDD), generating technical specifications, conducting structured brainstorming, or executing multi-step engineering tasks.
---
# Superpower

A rigorous software development framework for AI agents based on the Superpowers methodology, ensuring disciplined design, specification, test-driven implementation, and systematic review.

## When to Use

  - Planning and building new software features, tools, or applications from scratch.

  - Transforming vague ideas into concrete technical design documents and specifications.

  - Creating structured, step-by-step implementation plans before touching production code.

  - Writing code following strict red/green Test-Driven Development (TDD), YAGNI, and DRY principles.

  - Debugging complex codebases through hypothesis testing and root-cause analysis.

## Core Development Workflow

### 1. Specification and Brainstorming

Never jump directly into writing production code. Step back and uncover the true requirements first:

  - Probe the intent: Ask targeted questions to understand what the user wants to achieve, why, and what constraints exist.

  - Present incremental designs: Break the proposal into small, digestible chunks so the user can validate assumptions without cognitive overload.

  - Formalize the spec: Summarize architecture, data flow, APIs, and edge cases into a clear specification document before moving forward.

  - Secure approval: Ensure the design is confirmed before drafting implementation steps.

### 2. Implementation Planning

Translate approved specifications into a granular, step-by-step roadmap:

  - Make tasks atomic: Each task must represent a discrete, verifiable unit of work.

  - Enforce TDD sequencing: Every task starts with writing a failing test (red), followed by minimal code to pass (green), followed by refactoring.

  - Eliminate fluff: Strictly adhere to YAGNI. Avoid premature abstraction, speculative features, or unnecessary dependencies.

  - Include verification commands: Every step must list the exact command or test suite required to verify success.

### 3. Execution and Testing

Execute the plan methodically:

  - Work sequentially: Complete one task at a time. Never rush ahead or skip validation steps.

  - Red-to-green cycle: Run tests before writing implementation code to confirm failure, then write code, and run tests again to verify passing status.

  - Inspect and self-review: Audit code diffs for unintended side effects, style drift, and unnecessary complexity.

  - Maintain clean state: Ensure all tests pass cleanly before moving to the next item on the plan.

### 4. Root-Cause Debugging

When encountering errors, test failures, or unexpected behaviors:

  - Stop and inspect: Do not introduce shotgun fixes or random speculative edits.

  - Formulate hypotheses: Identify the underlying cause based on stack traces, log outputs, and minimal reproductions.

  - Isolate with a test: Write a focused regression test that reproduces the bug reliably.

  - Resolve at the root: Fix the root issue, re-run the full test suite, and verify that no regressions were introduced.

## Gotchas

  - Skipping the brainstorming phase: Writing code before clarifying ambiguous requirements leads to rework and architectural drift.

  - Over-engineering: Writing abstractions for imagined future requirements violates YAGNI. Keep solutions minimal and concrete.

  - Modifying tests to match broken code: Never alter an existing test just to make a build pass without verifying whether the specification changed.

  - Large, unverified batches: Making edits across many files simultaneously without running intermediate tests makes debugging exponentially harder.
