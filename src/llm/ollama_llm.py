import requests
from llm.base import BaseLLM

class OllamaLLM(BaseLLM):
    def __init__(self, model: str = "llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def plan(self, prompt: str) -> str:
        return self._call_llm(prompt)

    def synthesize(self, prompt: str) -> str:
        return self._call_llm(prompt)

    def _call_llm(self, prompt: str) -> str:
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["response"]
