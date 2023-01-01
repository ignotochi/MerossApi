from flask import request, Blueprint
from meross.services.AuthService import AuthService
from meross.services.ToggleDeviceService import ToggleDeviceService
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from meross.abstractions.webFilters.ToggleDeviceFilter import ToggleDeviceFilter
from flask.wrappers import Response


ToggleDeviceRoute = Blueprint("ToggleDeviceRoute", __name__)


@ToggleDeviceRoute.route("/toggledevice", methods=["POST"])
async def WebToggleDevice() -> Response:

    if HttpRequest.ValidateHttpPostRequest(request):

        userToken = HttpRequest.GetUserApiToken(request)
        context = await AuthService.RetrieveUserContext(userToken)

        try:
            filters = ToggleDeviceFilter(request.data)
            webToggleDevice = await ToggleDeviceService.Toggle(filters.toggledDevices, context)
            outcome = WebApiOutcome(webToggleDevice)
            return outcome

        except Exception as exception:
            error = exception.args[0]
            return HttpRequest.CustomResponse(f"Error on /toggledevice: {error}")

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)
