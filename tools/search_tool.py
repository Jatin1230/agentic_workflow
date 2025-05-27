from duckduckgo_search import DDGS

def search_tool(query):
    with DDGS() as ddgs:
        results = ddgs.text(query)
        return results[0]['body'] if results else "No results found."