from flask import request, Blueprint
from meross.services.ToggleDeviceService import ToggleDeviceService
from meross.core.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from meross.abstractions.filters.ToggleDeviceFilter import ToggleDeviceFilter
from flask.wrappers import Response


ToggleDeviceRoute = Blueprint("ToggleDeviceRoute", __name__)


@ToggleDeviceRoute.route("/toggleDevice", methods=["POST"])
def WebToggleDevice() -> Response:

    if HttpRequest.ValidateHttpPostRequest:

        try:
            userToken = HttpRequest.GetUserApiToken(request)
            filters = ToggleDeviceFilter(request.data)

            webToggleDevice = ToggleDeviceService.Toggle(filters.toggledDevices, userToken)
            outcome = WebApiOutcome(webToggleDevice)
            return outcome

        except Exception as exception:
            error = exception.args[0]
            return HttpRequest.CustomErrorResponse("Web Toggle Device Error: ", error)

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)
