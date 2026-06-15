---
name: classify-topic
description: "Classify the user's blog topic as either 'technical' or 'general'. Use as the first step in the blog article generation pipeline, before any research begins. Triggers on: any blog topic provided by the user, start of article generation pipeline."
metadata:
  version: "1.0.0"
  category: content-generation
---

# Classify Topic

Determine whether the user's topic is "technical" or "general" so that the research phase uses the right depth and focus.

## Step 1: Evaluate the topic
Consider the topic the user provided. Ask yourself:
- Does this topic involve programming, engineering, science, mathematics, or deep domain expertise that requires specialist knowledge?
- Or is it accessible to broad audiences without specialized knowledge?

**Technical topics** include: programming languages, software architecture, machine learning, data science, networking protocols, engineering disciplines, scientific research, medical procedures, financial instruments, legal frameworks, and similar areas requiring specialist background.

**General topics** include: lifestyle, travel, personal development, culture, history (accessible level), cooking, sports, entertainment, business strategy at a conceptual level, and similar areas readable by a non-specialist.

## Step 2: Classify
Assign the topic type:
- `technical` — if the topic primarily requires specialist knowledge to explain properly
- `general` — if the topic is accessible to a broad non-specialist audience

If the topic is borderline, prefer `general` to keep the article maximally accessible.

## Step 3: Record and announce
State the classification clearly:
> "📋 Topic classified as: **[technical / general]**"

Remember this classification — the research phase depends on it.

## Step 4: Proceed to research
Immediately proceed to the `research-topic` skill using the classification determined here. Pass the topic and classification forward.
