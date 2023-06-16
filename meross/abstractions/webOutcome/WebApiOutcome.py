import json
from flask.wrappers import Response
from meross.abstractions.webOutcome.IWebApiOutcome import IWebApiOutcome
from meross.abstractions.webOutcome.OutcomeJsonEncoder import OutcomeJsonEncoder
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger


class WebApiOutcome(IWebApiOutcome):

    def __new__(cls, item) -> Response:
        response = Response()
        response.content_type = "'application/json" 
        response.data = cls.ToJson(cls, item)
        return response

    def ToJson(self, item) -> str:
        try:
            return json.dumps(item, sort_keys=True, indent=4, cls=OutcomeJsonEncoder)
        except Exception as exception:
            MerossLogger("WebApiOutcome").WriteErrorLog(ExceptionManager.TryToCatch(exception))
            raise Exception("Json outcome conversion failed")

