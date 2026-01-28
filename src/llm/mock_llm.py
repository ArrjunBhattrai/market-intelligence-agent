from llm.base import BaseLLM

class MockLLM(BaseLLM):
    def plan(self, goal: str):
        return [
            f"{goal} competitors",
            f"{goal} market trends",
            f"{goal} pricing models"
        ]

    def synthesize(self, texts, goal: str):
        insights = []

        for text in texts:
            text = text.lower()
            if "pricing" in text or "$" in text:
                insights.append("Pricing information identified")
            if "trend" in text:
                insights.append("Market trend identified")
            if "startup" in text:
                insights.append("Competitor startup mentioned")

        return list(set(insights))
