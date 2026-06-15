"""
Blog Article Generator — CrewAI Flow

Pipeline:
    classify_topic (@start)
          │
    route_by_type (@router)  ← branches on "technical" or "general"
         / \
        /   \
  research  research       (@listen on each route string)
  _technical _general
        [   ]
         [*]
    write_article          (@listen via or_  ← fan-in from either path)
          │
    review_and_finalize    (@listen)

State (Pydantic):
    topic          — the user's input topic
    topic_type     — "technical" | "general"  (set by classify_topic)
    research_notes — raw research output
    draft          — first-pass article
    final_article  — polished final output
"""

import os

from openai import OpenAI
from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, or_, router, start

from crews import build_research_crew, build_review_crew, build_writing_crew


# ── Structured state ────────────────────────────────────────────────────────


class BlogState(BaseModel):
    topic: str = ""
    topic_type: str = ""      # "technical" | "general"
    research_notes: str = ""
    draft: str = ""
    final_article: str = ""


# ── Flow ────────────────────────────────────────────────────────────────────


class BlogFlow(Flow[BlogState]):

    model = os.getenv("MODEL", "gpt-4o-mini")

    # ── Step 1: entry point ─────────────────────────────────────────────────

    @start()
    def classify_topic(self):
        """Classify the topic as 'technical' or 'general' with a single LLM call."""
        print(f"\n📋 Classifying topic: '{self.state.topic}'")

        response = OpenAI().chat.completions.create(
            model=self.model,
            messages=[{
                "role": "user",
                "content": (
                    f"Classify this topic as either 'technical' or 'general'.\n\n"
                    f"Topic: {self.state.topic}\n\n"
                    "Technical: involves programming, engineering, science, math, "
                    "or deep domain expertise.\n"
                    "General: accessible to broad audiences without specialized knowledge.\n\n"
                    "Reply with ONLY one word: technical  or  general"
                ),
            }],
        )

        raw = response.choices[0].message.content.strip().lower()
        self.state.topic_type = raw if raw in ("technical", "general") else "general"
        print(f"✅ Classified as: {self.state.topic_type}")

    # ── Step 2: router — conditional branching ──────────────────────────────

    @router(classify_topic)
    def route_by_type(self):
        """Return the route string that @listen methods below will match on."""
        print(f"\n🔀 Routing to '{self.state.topic_type}' research path")
        return self.state.topic_type   # "technical" or "general"

    # ── Step 3a: technical path ─────────────────────────────────────────────

    @listen("technical")
    def research_technical(self):
        """Deep technical research — code examples, specs, architecture details."""
        print("\n🔬 Deep technical research starting...")
        crew = build_research_crew(
            topic=self.state.topic,
            focus=(
                "deep technical — include code examples, specifications, "
                "architecture details, and expert-level insights"
            ),
        )
        result = crew.kickoff()
        self.state.research_notes = str(result)
        print("✅ Technical research done")

    # ── Step 3b: general path ───────────────────────────────────────────────

    @listen("general")
    def research_general(self):
        """Broad research for a general audience — concepts and real-world examples."""
        print("\n🔍 General audience research starting...")
        crew = build_research_crew(
            topic=self.state.topic,
            focus=(
                "broad and accessible — focus on concepts, real-world examples, "
                "and practical applications for a non-specialist audience"
            ),
        )
        result = crew.kickoff()
        self.state.research_notes = str(result)
        print("✅ General research done")

    # ── Step 4: fan-in with or_ — write article from either path ───────────

    @listen(or_(research_technical, research_general))
    def write_article(self):
        """Write the blog article using whichever research path completed."""
        print("\n✍️  Writing blog article...")
        crew = build_writing_crew(
            topic=self.state.topic,
            research_notes=self.state.research_notes,
        )
        result = crew.kickoff()
        self.state.draft = str(result)
        print("✅ Draft complete")

    # ── Step 5: review and finalize ─────────────────────────────────────────

    @listen(write_article)
    def review_and_finalize(self):
        """Review the draft and produce the final polished article."""
        print("\n📝 Reviewing and finalizing...")
        crew = build_review_crew(
            topic=self.state.topic,
            draft=self.state.draft,
        )
        result = crew.kickoff()
        self.state.final_article = str(result)
        print("✅ Final article ready")
        return self.state.final_article
