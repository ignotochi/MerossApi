import json
from flask.wrappers import Response
from meross.abstractions.IWebApiOutcome import IWebApiOutcome
from meross.abstractions.OutcomeJsonEncoder import OutcomeJsonEncoder
from typing import List


class WebApiOutcome(IWebApiOutcome):

    def __new__(self, item) -> Response:
        response = Response()
        response.content_type = "'application/json" 
        response.data = self.ToJson(self, item)
        return response

    @staticmethod
    def ToJson(self, item) -> str:
        try:
            return json.dumps(item, sort_keys=True, indent=4, cls=OutcomeJsonEncoder)
        except Exception as exception:
            return "WebApiOutcomeError: " + str(exception.args[0])