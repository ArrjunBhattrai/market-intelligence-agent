from agents.base import BaseAgent
from llm.ollama_llm import OllamaLLM

class ResearchAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)
        self.llm = OllamaLLM()

    def run(self, task: dict):
        domain = task["domain"]

        decision = self.llm.plan(
            f"""
            Given the startup domain "{domain}",
            decide which research steps are required:
            - competitors
            - pricing
            - market trends

            Respond with a comma-separated list.
            """
        )

        return {
            "domain": domain,
            "plan": decision
        }
