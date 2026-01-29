from agents.base import BaseAgent
from llm.ollama_llm import OllamaLLM

class AnalystAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)
        self.llm = OllamaLLM()

    def run(self, research_results: dict):
        prompt = f"""
        Analyze the following research data and identify:
        - Pricing models
        - Customer segments
        - Competitive patterns

        Data: {research_results}
        Respond as JSON.
        """
        analysis = self.llm.synthesize(prompt)
        return analysis
