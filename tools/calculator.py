"""
Calculator tool — evaluates a basic math expression.
Preserves the original implementation from the LangGraph source agent.
"""
import json
import sys


def calculator(expression: str) -> str:
    """Evaluate a basic math expression. Example: '2 + 2 * 10'"""
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    payload = json.load(sys.stdin)
    expression = payload.get("expression", "")
    result = calculator(expression)
    print(json.dumps({"result": result}))
