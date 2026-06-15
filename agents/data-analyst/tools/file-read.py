"""
File read tool implementation.
# TRANSLATION NOTE: Source used crewai_tools.FileReadTool which reads local files.
# This implementation provides the same functionality directly.
"""
import json
import sys


def file_read(path: str, encoding: str = "utf-8") -> dict:
    """
    Read the contents of a file.

    Args:
        path: Path to the file to read
        encoding: File encoding (default utf-8)

    Returns:
        dict with 'content' key containing file text, or 'error' on failure
    """
    try:
        with open(path, "r", encoding=encoding) as f:
            content = f.read()
        return {"content": content}
    except FileNotFoundError:
        return {"error": f"File not found: {path}", "content": ""}
    except PermissionError:
        return {"error": f"Permission denied: {path}", "content": ""}
    except Exception as e:
        return {"error": str(e), "content": ""}


if __name__ == "__main__":
    input_data = json.loads(sys.stdin.read())
    path = input_data.get("path", "")
    encoding = input_data.get("encoding", "utf-8")
    output = file_read(path, encoding)
    print(json.dumps(output))
