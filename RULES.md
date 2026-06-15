# Rules

## Must Always
- Run the three specialist sub-agents in order: research-specialist → data-analyst → content-writer
- Pass each specialist's output as context to the next specialist's prompt
- Produce a final synthesized answer after all three specialists have completed their work
- Cite sources gathered during the research phase in all subsequent outputs
- Save intermediate outputs to the appropriate files: research_findings.md, analysis_report.md, final_report.md

## Must Never
- Skip the research phase and go directly to writing
- Present analysis without having first gathered research findings
- Present a final report without incorporating both research and analysis phases
- Invent or fabricate statistics, facts, or sources not found during actual research

## Output Constraints
- Research findings must include: key findings, statistics, expert opinions, recent developments, and sources
- Analysis report must include: key insights, trend analysis, implications, expert interpretation, and actionable conclusions
- Final report must include: executive summary, introduction, main findings, analysis and insights, conclusions and recommendations, and sources/references
- All three reports must be saved as Markdown files

## Interaction Boundaries
- Only conduct research on topics explicitly provided by the user
- Do not modify or improve the user's research topic without asking
- After delivering the final report, stop and await the next user instruction — do not loop
