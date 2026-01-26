from agents.base import BaseAgent
from tools.web_search import search_web
from tools.scraper import scrape_page

class ResearchAgent(BaseAgent):
    def run(self, task: dict) -> dict:
        domain = task["domain"]
        depth = task.get("depth", 1)

        query = f"{domain} startups competitors pricing market trends"
        search_results = search_web(query, max_results=depth * 3)

        competitors = []
        trends = []
        pricing = []

        for result in search_results:
            page_text = scrape_page(result["url"]).lower()

            if "startup" in page_text:
                competitors.append(result["title"])

            if "trend" in page_text:
                trends.append(result["snippet"])

            if "pricing" in page_text or "$" in page_text:
                pricing.append(result["snippet"])

        return {
            "agent": self.name,
            "domain": domain,
            "depth": depth,
            "findings": {
                "competitors": list(set(competitors)),
                "market_trends": trends[:3],
                "pricing_models": pricing[:3]
            },
            "status": "completed"
        }
