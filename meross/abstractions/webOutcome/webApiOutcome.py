import json
from flask.wrappers import Response
from meross.abstractions.webOutcome.webApiOutcome_interface import IWebApiOutcome
from meross.abstractions.webOutcome.outcomeJsonEncoder import OutcomeJsonEncoder
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger


class WebApiOutcome(IWebApiOutcome):

    def __new__(self, item) -> Response:
        response = Response()
        response.content_type = "'application/json" 
        response.data = self.toJson(self, item)
        return response

    def toJson(self, item) -> str:
        try:
            return json.dumps(item, sort_keys=True, indent=4, cls=OutcomeJsonEncoder)
        except Exception as exception:
            MerossLogger("WebApiOutcome").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception("Json outcome conversion failed")

