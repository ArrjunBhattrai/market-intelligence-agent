from ddgs import DDGS

def search_web(query: str, max_results: int = 5):
    """
    Search the web and return top results.
    """
    results = []
    
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r["title"],
                "url": r["href"],
                "snippet": r["body"]
            })

    return results
