from abc import ABC, abstractmethod


class SpecialCaseRule(ABC):

    @abstractmethod
    def apply(self, sentences: list) -> None:
        pass
