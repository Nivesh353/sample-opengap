"""
Web search tool implementation using the Serper API.
# TRANSLATION NOTE: Source used crewai_tools.SerperDevTool which wraps the Serper search API.
# This implementation replicates the same API call directly.
"""
import os
import json
import sys
import http.client


def web_search(query: str, num_results: int = 10) -> dict:
    """
    Search the web using the Serper API.

    Args:
        query: The search query to look up
        num_results: Number of results to return (default 10)

    Returns:
        dict with 'results' list containing title, url, snippet for each result
    """
    api_key = os.environ.get("SERPER_API_KEY", "")
    if not api_key:
        return {"error": "SERPER_API_KEY environment variable not set", "results": []}

    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({"q": query, "num": num_results})
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    try:
        conn.request("POST", "/search", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e), "results": []}
    finally:
        conn.close()

    results = []
    for item in data.get("organic", []):
        results.append({
            "title": item.get("title", ""),
            "url": item.get("link", ""),
            "snippet": item.get("snippet", "")
        })

    return {"results": results}


if __name__ == "__main__":
    # Read input from stdin as JSON
    input_data = json.loads(sys.stdin.read())
    query = input_data.get("query", "")
    num_results = input_data.get("num_results", 10)
    output = web_search(query, num_results)
    print(json.dumps(output))
