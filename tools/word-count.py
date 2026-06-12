"""
Word-count tool — counts the number of words in a text string.
Preserves the original implementation from the LangGraph source agent.
"""
import json
import sys


def word_count(text: str) -> str:
    """Count the number of words in a text string."""
    return str(len(text.split()))


if __name__ == "__main__":
    payload = json.load(sys.stdin)
    text = payload.get("text", "")
    result = word_count(text)
    print(json.dumps({"result": result}))
