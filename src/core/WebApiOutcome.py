import json
from ..abstractions.IWebApiOutcome import IWebApiOutcome
from ..abstractions.OutcomeJsonEncoder import OutcomeJsonEncoder
from typing import TypeVar, Generic, List, Tuple

T = TypeVar("T")


class WebApiOutcome(IWebApiOutcome):

    @staticmethod
    def __new__(self, item: T = None) -> T:
        if (item != None):
            return self.ToJson(self, item)
        else:
            return []
 
    @staticmethod
    def ToJson(self, item):
        try:
            return json.dumps(item, sort_keys=True, indent=4, cls=OutcomeJsonEncoder)
        except Exception as exception:
            return {"WebApiOutcomeError" : exception.args[0]}
