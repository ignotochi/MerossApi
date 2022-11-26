import json
from meross.abstractions.IWebApiOutcome import IWebApiOutcome
from meross.abstractions.OutcomeJsonEncoder import OutcomeJsonEncoder
from typing import TypeVar

T = TypeVar("T")

class WebApiOutcome(IWebApiOutcome):

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
