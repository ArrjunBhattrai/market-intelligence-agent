from agents.base import BaseAgent
from llm.ollama_llm import OllamaLLM

class WriterAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)
        self.llm = OllamaLLM()

    def run(self, analyzed_data: dict):
        prompt = f"""
        Write a polished report for the founder based on this analysis:
        {analyzed_data}
        """
        report = self.llm.synthesize(prompt)
        return report
