from flask import request, Blueprint
from meross.services.LoadDevicesService import LoadDevicesService
from meross.services.AuthService import AuthService
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from meross.abstractions.webFilters.DevicesFilter import DevicesFilter
from flask.wrappers import Response


LoadDevicesRoute = Blueprint("LoadDevicesRoute", __name__)


@LoadDevicesRoute.route("/loaddevices", methods=["GET"])
def WebLoadDevices() -> Response:

    if HttpRequest.ValidateHttpGetRequest(request):

        userToken = HttpRequest.GetUserApiToken(request)
        context = AuthService.RetrieveUserContext(userToken)

        try:
            filters = DevicesFilter(request.args.get('DevicesFilter'))
            webDevices = LoadDevicesService.Load(filters.devices, context)
            outcome = WebApiOutcome(webDevices)
            return outcome

        except Exception as exception:
            error = exception.args[0]
            return HttpRequest.CustomResponse(f"Error on /loaddevices: {error}")

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)
