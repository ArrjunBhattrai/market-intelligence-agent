from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, task: dict) -> dict:
        """
        Execute the agent logic.
        """
        pass
