from pydantic import BaseModel

class ResearchTask(BaseModel):
    domain: str
    depth: int = 1
