from abc import ABC, abstractmethod
from typing import List

class BaseLLM(ABC):
    @abstractmethod
    def plan(self, goal: str) -> List[str]:
        """Decide what queries to run"""
        pass

    @abstractmethod
    def synthesize(self, text: List[str], goal: str) -> List[str]:
        """Extract insights from raw text"""
        pass
