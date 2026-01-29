from agents.base import BaseAgent
from llm.ollama_llm import OllamaLLM

def dummy_search_tool(step: str, domain: str) -> str:
    return f"Dummy data for '{step}' about '{domain}'"

class ResearchAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)
        self.llm = OllamaLLM()
        # Map steps to tools
        self.tools = {
            "competitors": dummy_search_tool,
            "pricing": dummy_search_tool,
            "market trends": dummy_search_tool
        }

    # Step 1: Plan
    def plan(self, query: str) -> list[str]:
        prompt = f"""
        You are a research assistant. Given the startup query: "{query}", 
        decide which information needs to be searched on the web.
        List actionable research steps like: competitors, pricing, market trends.
        Respond as a comma-separated list.
        """
        plan_str = self.llm.plan(prompt)
        steps = [s.strip() for s in plan_str.split(",")]
        return steps

    # Step 2: Execute steps
    def execute_steps(self, steps: list[str], query: str) -> dict:
        results = {}
        for step in steps:
            tool = self.tools.get(step, dummy_search_tool)
            results[step] = tool(step, query)
        return results

    # Step 3: Synthesize results
    def synthesize(self, results: dict, query: str) -> str:
        summary_prompt = f"""
        You are a startup analyst. Summarize the following research results for the founder:
        {results}
        """
        return self.llm.synthesize(summary_prompt)

    # Full run
    def run(self, task: dict):
        query = task["domain"]
        steps = self.plan(query)
        results = self.execute_steps(steps, query)
        summary = self.synthesize(results, query)
        return {
            "query": query,
            "plan": steps,
            "results": results,
            "summary": summary
        }
