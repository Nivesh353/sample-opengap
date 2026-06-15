---
name: orchestrate
description: "Coordinate the research-specialist, data-analyst, and content-writer sub-agents to produce a comprehensive research report on a given topic. Use for any research request. Triggers on: research, analyze, write report, investigate, study, find information about, tell me about, report on."
allowed-tools: cli read write
metadata:
  version: "1.0.0"
  category: orchestration
---

# Orchestrate Research Pipeline

Drive the three specialist sub-agents in sequence and combine their outputs into one final research package. Each sub-agent is run as a separate gitagent process via the `cli` tool.

## Step 0: Discover sub-agent folder names
Run `ls agents/` with the `cli` tool and read the exact folder names. Use those exact names in every subsequent `gitagent --dir` call. Do not recall paths from memory.

Example:
```
cli: ls agents/
```

## Step 1: Research Phase — Run the Research Specialist
Call the research-specialist sub-agent with the user's topic:

```
cli: gitagent --dir agents/research-specialist -p "Conduct comprehensive research on the topic: <TOPIC>

Your tasks:
1. Search for the most current and relevant information
2. Gather data from multiple reliable sources
3. Identify key facts, statistics, and expert opinions
4. Organize findings in a structured format
5. Ensure information is accurate and up-to-date

Provide a detailed research summary with:
- Key findings
- Important statistics
- Expert opinions
- Recent developments
- Reliable sources used"
```

**Guard**: If the `cli` output contains `Creating directory` or `Created agent.yaml`, the path was wrong — gitagent created an empty placeholder. Stop, verify the folder name from Step 0, correct the path to use a forward slash (e.g. `agents/research-specialist`), and re-run. Never use output from a freshly-created agent.

Capture the full output as `RESEARCH_OUTPUT`.

## Step 2: Save Research Findings
Use the `write` tool (or `cli` with a shell redirect) to save the research output to `research_findings.md`:

```
write: path=research_findings.md, content=<RESEARCH_OUTPUT>
```

## Step 3: Analysis Phase — Run the Data Analyst
Call the data-analyst sub-agent, providing the research findings as context:

```
cli: gitagent --dir agents/data-analyst -p "Analyze the following research findings for the topic: <TOPIC>

RESEARCH FINDINGS:
<RESEARCH_OUTPUT>

Your tasks:
1. Review the research findings above
2. Identify patterns, trends, and key insights
3. Analyze the implications and significance
4. Provide expert interpretation of the data
5. Highlight the most important conclusions

Provide:
- Key insights and patterns
- Trend analysis
- Implications and significance
- Expert interpretation
- Actionable conclusions"
```

Capture the full output as `ANALYSIS_OUTPUT`.

## Step 4: Save Analysis Report
Save the analysis output to `analysis_report.md`.

## Step 5: Writing Phase — Run the Content Writer
Call the content-writer sub-agent, providing both research and analysis as context:

```
cli: gitagent --dir agents/content-writer -p "Create a comprehensive report on the topic: <TOPIC>

RESEARCH FINDINGS:
<RESEARCH_OUTPUT>

ANALYSIS RESULTS:
<ANALYSIS_OUTPUT>

Your tasks:
1. Review both research findings and analysis results above
2. Write a well-structured, comprehensive report
3. Ensure clarity and readability for the target audience
4. Include executive summary, main content, and conclusions
5. Cite all sources appropriately

The report should include:
- Executive Summary
- Introduction
- Main Findings
- Analysis and Insights
- Conclusions and Recommendations
- Sources and References"
```

Capture the full output as `FINAL_REPORT`.

## Step 6: Save Final Report
Save the final report output to `final_report.md`.

## Step 7: Synthesize and Finish
Present a summary to the user:
- Confirm that all three phases completed successfully
- State that three files were produced: `research_findings.md`, `analysis_report.md`, `final_report.md`
- Provide the executive summary from the final report inline
- Do not loop — stop after delivering this summary
