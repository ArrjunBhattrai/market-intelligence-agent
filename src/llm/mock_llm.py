from llm.base import BaseLLM

class MockLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        if "competitors" in prompt.lower():
            return "search_competitors"
        if "pricing" in prompt.lower():
            return "search_pricing"
        return "search_market_trends"
