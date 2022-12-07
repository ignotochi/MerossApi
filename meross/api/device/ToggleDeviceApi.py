from flask import request, Blueprint
from meross.services.AuthService import AuthService
from meross.services.ToggleDeviceService import ToggleDeviceService
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from meross.abstractions.webFilters.ToggleDeviceFilter import ToggleDeviceFilter
from flask.wrappers import Response


ToggleDeviceRoute = Blueprint("ToggleDeviceRoute", __name__)


@ToggleDeviceRoute.route("/toggledevice", methods=["POST"])
def WebToggleDevice() -> Response:

    if HttpRequest.ValidateHttpPostRequest(request):

        try:
            userToken = HttpRequest.GetUserApiToken(request)
            context = AuthService.RetrieveUserContext(userToken)

            filters = ToggleDeviceFilter(request.data)
            webToggleDevice = ToggleDeviceService.Toggle(filters.toggledDevices, context)
            outcome = WebApiOutcome(webToggleDevice)

            return outcome

        except Exception as exception:
            error = exception.args[0]
            return HttpRequest.CustomErrorResponse("Web Toggle device Error: ", error)

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)
