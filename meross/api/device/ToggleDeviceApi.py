from flask import request, Blueprint
from meross.services.ToggleDeviceService import ToggleDeviceService
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from meross.abstractions.webFilters.ToggleDeviceFilter import ToggleDeviceFilter
from flask.wrappers import Response


ToggleDeviceRoute = Blueprint("ToggleDeviceRoute", __name__)


@ToggleDeviceRoute.route("/toggledevice", methods=["POST"])
async def WebToggleDevice() -> Response:
    context = await HttpRequest.ValidateHttpPostRequestAndGetContext(request)

    if context:
        try:
            filters = ToggleDeviceFilter(request.data)
            webToggleDevice = await ToggleDeviceService.Toggle(filters.toggledDevices, context)
            outcome = WebApiOutcome(webToggleDevice)
            return outcome

        except Exception as exception:
            return HttpRequest.CustomResponse(f"Error on /toggledevice: {exception.args[0]}")

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)
