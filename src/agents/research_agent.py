from agents.base import BaseAgent
from llm.mock_llm import MockLLM
from tools.web_search import search_web
from tools.scraper import scrape_page

class ResearchAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)
        self.llm = MockLLM()

    def run(self, task: dict) -> dict:
        domain = task["domain"]
        depth = task.get("depth", 1)

        queries = self.llm.plan(domain)

        raw_texts = []

        for query in queries:
            results = search_web(query, max_results=depth)
            for result in results:
                page_text = scrape_page(result["url"])
                raw_texts.append(page_text)

        insights = self.llm.synthesize(raw_texts, domain)

        return {
            "agent": self.name,
            "domain": domain,
            "insights": insights,
            "status": "completed"
        }
