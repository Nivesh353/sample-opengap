"""
File write tool implementation.
# TRANSLATION NOTE: Source used crewai_tools.FileWriterTool which writes local files.
# This implementation provides the same functionality directly.
"""
import json
import os
import sys


def file_write(path: str, content: str, encoding: str = "utf-8", mode: str = "w") -> dict:
    """
    Write content to a file.

    Args:
        path: Path to the file to write
        content: Content to write
        encoding: File encoding (default utf-8)
        mode: Write mode - 'w' to overwrite (default) or 'a' to append

    Returns:
        dict with 'success' boolean and 'path', or 'error' on failure
    """
    try:
        # Create parent directories if needed
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, mode, encoding=encoding) as f:
            f.write(content)
        return {"success": True, "path": path}
    except PermissionError:
        return {"success": False, "path": path, "error": f"Permission denied: {path}"}
    except Exception as e:
        return {"success": False, "path": path, "error": str(e)}


if __name__ == "__main__":
    input_data = json.loads(sys.stdin.read())
    path = input_data.get("path", "")
    content = input_data.get("content", "")
    encoding = input_data.get("encoding", "utf-8")
    mode = input_data.get("mode", "w")
    output = file_write(path, content, encoding, mode)
    print(json.dumps(output))
