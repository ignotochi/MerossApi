from flask import request, Blueprint
from meross.services.LoadDevicesService import LoadDevicesService
from meross.services.AuthService import AuthService
from meross.abstractions.weboutcome.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from meross.abstractions.webFilters.DevicesFilter import DevicesFilter
from flask.wrappers import Response


LoadDevicesRoute = Blueprint("LoadDevicesRoute", __name__)


@LoadDevicesRoute.route("/loaddevices", methods=["GET"])
def WebLoadDevices() -> Response:

    if HttpRequest.ValidateHttpGetRequest(request):

        try:
            userToken = HttpRequest.GetUserApiToken(request)
            context = AuthService.RetrieveUserContext(userToken)

            filters = DevicesFilter(request.data)

            webDevices = LoadDevicesService.Load(filters.devices, context)
            outcome = WebApiOutcome(webDevices)

            return outcome

        except Exception as exception:
            error = exception.args[0]
            return HttpRequest.CustomErrorResponse("Web Load Devices Error: ", error)

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)
