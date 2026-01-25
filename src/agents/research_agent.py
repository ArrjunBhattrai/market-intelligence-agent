from agents.base import BaseAgent

class ResearchAgent(BaseAgent):
    def run(self, task: dict) -> dict:
        domain = task.get("domain")
        depth = task.get("depth", 1)

        findings = {
            "competitors": [],
            "market_trends": [],
            "pricing_models": []
        }

        return {
            "agent": self.name,
            "domain": domain,
            "depth": depth,
            "findings": findings,
            "status": "completed"
        }
