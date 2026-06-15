"""
Entry point for the Blog Article Generator CrewAI Flow.

Usage:
    python main.py                        # interactive prompt
    python main.py "Your topic here"      # pass topic as CLI argument

Environment variables required:
    OPENAI_API_KEY — OpenAI key used by all agents and the classification LLM call

Optional:
    MODEL — LiteLLM model string (default: gpt-4o-mini)
"""

import sys

from dotenv import load_dotenv

from flow import BlogFlow

load_dotenv()


def run(topic: str) -> str:
    flow = BlogFlow()
    flow.state.topic = topic
    result = flow.kickoff()
    return str(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = input("Enter a blog topic: ").strip()
        if not topic:
            print("No topic provided. Exiting.")
            sys.exit(1)

    print("\n" + "=" * 60)
    print(f"BLOG FLOW STARTED — topic: {topic}")
    print("=" * 60)

    article = run(topic)

    print("\n" + "=" * 60)
    print("FINAL ARTICLE")
    print("=" * 60)
    print(article)
