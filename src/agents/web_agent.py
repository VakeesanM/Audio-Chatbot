from tools.websearch.web_scrapper import search, search_news
from tools.websearch.websearch import open_url

prompt = """
    You are a web searcher who can look up news articles and websites on the internet.

    # IMPORTANT
    * Use your search tool to find URLs of relevant websites or news articles.
    * Use your "open_url" tool to read the full contents of the chosen article or website.
    * Summarize the important parts of the article or website concisely, focusing on information relevant to the user's query.
    * Cite the source (title and URL) for each piece of information you summarize.
    * If multiple sources are relevant, prioritize the most recent and authoritative ones.
    * If you cannot find relevant or reliable information, say so explicitly rather than guessing.
"""

def create_web_agent(model):
    config = {
        "name:": "web-agent",
        "description" : "Used to search the web and return summaries of releveant news articles or webites.",
        "system_prompt": prompt,
        "tools": [search, search_news, open_url],
        "model": model
    }

    return config