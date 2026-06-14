---
name: orchestrate
description: >
  Supervisor orchestration skill. Analyzes the user request, routes it to the
  appropriate specialist sub-agent (researcher, writer, or coder), collects the
  response, and synthesizes the final answer. Implements the LangGraph
  supervisor-worker pattern with a maximum of 6 routing iterations.
allowed-tools: "cli"
metadata:
  version: "1.0.0"
  category: orchestration
  source_pattern: langgraph_supervisor_conditional_edges
---

# Orchestrate — Supervisor Routing Skill

This skill implements the supervisor-worker orchestration pattern translated from
LangGraph. The supervisor reads the conversation, decides which specialist to invoke,
calls that specialist, and loops until the task is complete (max 6 iterations).

## Step 1: Classify the Request

Read the user's message and classify it into one of:
- **researcher** — factual questions, lookups, analysis, explanations
- **writer** — drafting, summarizing, editing, creative text
- **coder** — writing, debugging, or explaining code
- **finish** — task is already complete, no delegation needed

## Step 2: Delegate to the Specialist

Based on the classification, invoke the appropriate sub-agent using the `cli` tool:

```
For researcher tasks:
  gitagent --dir ./agents/researcher run "<user_message>"

For writer tasks:
  gitagent --dir ./agents/writer run "<user_message>"

For coder tasks:
  gitagent --dir ./agents/coder run "<user_message>"
```

## Step 3: Collect and Evaluate the Response

Read the sub-agent's output. Determine if the task is complete:
- If complete → proceed to Step 4
- If another specialist is needed (e.g., researcher found facts, now writer should draft) → return to Step 2 with the accumulated context (count this as another iteration)
- If iteration count reaches 6 → stop and synthesize whatever has been gathered

## Step 4: Synthesize and Deliver

Combine the specialist's response with any prior context and deliver the final
synthesized answer to the user. Present it clearly and concisely.

## Routing Logic (from LangGraph source)

```
[START] → [Supervisor] --researcher--> [Researcher] → [Supervisor]
                        --writer-----> [Writer]     → [Supervisor]
                        --coder------> [Coder]      → [Supervisor]
                        --finish-----> [END]
```

Iteration guard: MAX_ITERATIONS = 6 (from state.py in source)
