import json
from ..abstractions.IWebApiOutcome import IWebApiOutcome
from ..abstractions.OutcomeJsonEncoder import OutcomeJsonEncoder
from typing import TypeVar, Generic, List, Tuple

T = TypeVar("T")

class WebApiOutcome(IWebApiOutcome):
    
    result = [T]

    def __init__(self, item = [T]) -> T:
        if (item != []):
         self.result = self.ToJson(item)

    def ToJson(self, item):
        try:
            return json.dumps(item, sort_keys=True, indent=4, cls=OutcomeJsonEncoder)
        except Exception as e:
            print(f'Error on WebApiOutcome: {e}')
