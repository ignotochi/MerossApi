from abc import ABC, abstractmethod


class IWebApiOutcome(ABC):

    @abstractmethod
    def toJson(self, item) -> str:
        pass
