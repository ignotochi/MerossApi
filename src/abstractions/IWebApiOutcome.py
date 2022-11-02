from abc import ABC, abstractmethod

class IWebApiOutcome(ABC):

    @abstractmethod
    def ToJson(self, item):
        pass