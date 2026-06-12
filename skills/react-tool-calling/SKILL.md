---
name: react-tool-calling
description: "ReAct-style tool-calling loop: receive user input, decide whether to call
  a tool, execute the tool, feed the result back to the LLM, and repeat until a final
  answer is produced. Use when the user asks a question that may require calculator
  or word_count tools to answer accurately. Triggers on: any user message, math
  expressions, word count requests, general questions."
allowed-tools: calculator word-count
metadata:
  version: "1.0.0"
  category: reasoning
---

# ReAct Tool-Calling Loop

This skill implements a Reason-then-Act loop: the agent reasons about the user's request,
decides which tool (if any) to call, executes it, observes the result, and continues
until it can produce a final answer.

## Step 1: Receive Input
Accept the user's message. Assess whether the request requires computation (use calculator)
or text analysis (use word-count), or can be answered directly.

## Step 2: Reason
Think about what the user is asking. If a tool is needed, identify which one and what
arguments to pass.

## Step 3: Act (optional)
Call the appropriate tool with the correct arguments:
- Use `calculator` for arithmetic or mathematical expressions (e.g., `2 + 2 * 10`)
- Use `word-count` to count the number of words in a given text string

## Step 4: Observe
Receive the tool's output. If the result fully answers the user's question, proceed to
Step 5. If further tool calls are needed (e.g., chained computation), return to Step 3.

## Step 5: Respond
Produce a final natural-language response incorporating the tool result(s). Be concise
and directly address the user's original question.
