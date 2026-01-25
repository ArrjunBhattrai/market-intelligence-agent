from fastapi import FastAPI
from schemas.task import ResearchTask
from agents.research_agent import ResearchAgent

app = FastAPI()

@app.post("/research")
def research(task: ResearchTask):
    agent = ResearchAgent(name="research-agent")
    result = agent.run(task.dict())
    return result
