import json
from ..abstractions.IWebApiOutcome import IWebApiOutcome
from ..abstractions.OutcomeJsonEncoder import OutcomeJsonEncoder


class WebApiOutcome(IWebApiOutcome):

    def __init__(self, item = None):
        if(item != None):
         self.result = self.ToJson(item)

    def ToJson(self, item):
        try:
            return json.dumps(item, sort_keys=True, indent=4, cls=OutcomeJsonEncoder)
        except Exception as e:
            print(f'Error on WebApiOutcome: {e}')
