---
name: orchestrate
description: "Coordinate the researcher, writer, coder, and reviewer sub-agents to fulfil the user's request. Use for any prompt or question that requires research, writing, or coding. Triggers on: any user request or question."
allowed-tools: cli
metadata:
  version: "1.0.0"
  category: orchestration
---

# Orchestrate

Drive the four specialist sub-agents in the correct order and combine their outputs into one final answer. The flow is:

```
[researcher] --> [writer]   \
             \-> [coder]    /--> [reviewer] --> final answer
```

The writer and coder run on the same research output (fan-out). The reviewer combines both their outputs (fan-in).

## Step 0: Discover sub-agent folder names
Run `ls agents/` with the `cli` tool and confirm the exact folder names before proceeding. Use those literal names in every `gitagent --dir` call below.

**Guard:** if a `cli` call prints `Creating directory` or `Created agent.yaml`, the path was wrong — gitagent bootstrapped an empty throwaway agent. Stop immediately, correct the path to `agents/<name>` with a forward slash, and re-run. Never use output from a freshly-created default agent.

## Step 1: Research phase
Call the `cli` tool to run the researcher sub-agent:

    gitagent --dir agents/researcher -p "Research the following and gather key facts and insights:\n\n<USER_PROMPT>"

Wait for it to finish. Capture its stdout as `RESEARCH_OUTPUT`.

The expected output is: a detailed summary of findings with key points and analysis.

## Step 2a: Write phase (fan-out — run after Step 1)
Call the `cli` tool to run the writer sub-agent:

    gitagent --dir agents/writer -p "Using the research below, produce a clear and well-structured response to the original request.\n\nRequest: <USER_PROMPT>\n\nResearch:\n<RESEARCH_OUTPUT>"

Wait for it to finish. Capture its stdout as `WRITE_OUTPUT`.

The expected output is: a polished, well-written response addressing the request.

## Step 2b: Code phase (fan-out — run after Step 1, can follow Step 2a)
Call the `cli` tool to run the coder sub-agent:

    gitagent --dir agents/coder -p "If the request involves code, write a clean implementation with a brief explanation. If no code is needed, respond with 'N/A'.\n\nRequest: <USER_PROMPT>\n\nResearch:\n<RESEARCH_OUTPUT>"

Wait for it to finish. Capture its stdout as `CODE_OUTPUT`.

The expected output is: working code with a short explanation, or 'N/A' if no code is needed.

## Step 3: Review phase (fan-in — runs after Steps 2a and 2b)
Call the `cli` tool to run the reviewer sub-agent:

    gitagent --dir agents/reviewer -p "Review and combine the outputs below into a single high-quality final response.\n\nOriginal request: <USER_PROMPT>\n\nWritten response:\n<WRITE_OUTPUT>\n\nCode output:\n<CODE_OUTPUT>"

Wait for it to finish. Capture its stdout as `FINAL_OUTPUT`.

The expected output is: a complete, accurate, and well-presented final answer.

## Step 4: Synthesize and stop
Return `FINAL_OUTPUT` directly as the response to the user. Do not add commentary or loop. The task is complete once the reviewer's output is delivered.
