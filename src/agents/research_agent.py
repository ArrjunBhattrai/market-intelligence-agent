from agents.base import BaseAgent
from llm.mock_llm import MockLLM
from tools.web_search import search_web

class ResearchAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)
        self.llm = MockLLM()

    def run(self, task: dict) -> dict:
        domain = task.get("domain")
        depth = task.get("depth", 1)

        prompt = f"""
        Research the following domain:
        {domain}

        Identify competitors, market trends, and pricing models.
        """

        decision = self.llm.generate(prompt)

        if decision == "search_competitors":
            results = search_web(f"{domain} competitors")
        elif decision == "search_pricing":
            results = search_web(f"{domain} pricing")
        else:
            results = search_web(f"{domain} market trends")

        return {
            "agent": self.name,
            "domain": domain,
            "decision": decision,
            "results": results,
            "status": "completed"
        }
