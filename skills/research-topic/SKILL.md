---
name: research-topic
description: "Research the blog topic thoroughly using the classification from the classify-topic step. Applies the correct research focus (technical or general) to produce comprehensive research notes. Triggers on: after topic classification, when research notes are needed before writing."
metadata:
  version: "1.0.0"
  category: content-generation
---

# Research Topic

Conduct thorough research on the topic, tailored to the topic type determined in the classify-topic step.

## Step 1: Determine research focus
Based on the topic classification:

- **If topic_type is "technical"**: Research with a deep technical focus — include code examples, specifications, architecture details, and expert-level insights. Target an audience with specialist knowledge.
- **If topic_type is "general"**: Research with a broad and accessible focus — focus on concepts, real-world examples, and practical applications for a non-specialist audience.

Announce the research path:
> "🔬 Deep technical research starting..." (for technical)  
> "🔍 General audience research starting..." (for general)

## Step 2: Gather key information
Research the topic comprehensively. Cover:
- **Key concepts** — the fundamental ideas, definitions, and principles
- **Important facts** — statistics, data points, historical context, timelines
- **Examples** — real-world applications, case studies, illustrative instances
- **Insights** — expert perspectives, trends, implications, counterpoints

For **technical** topics, additionally gather:
- Code examples or pseudocode demonstrating key concepts
- Technical specifications, standards, or architectural diagrams (described in prose)
- Common pitfalls, best practices, and expert-level considerations

For **general** topics, additionally gather:
- Relatable analogies and everyday examples
- Practical takeaways the reader can apply
- Accessible explanations that avoid jargon

## Step 3: Organize findings
Structure the research notes with clear sections:
- Overview / What is [topic]?
- Key concepts and facts
- Examples and real-world applications
- Insights and implications (or expert considerations for technical topics)

## Step 4: Record and announce
State research completion:
> "✅ Research complete. Proceeding to writing."

Retain the full research notes — the write-article skill depends on them in the next step.
