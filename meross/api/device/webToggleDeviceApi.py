from flask import request, Blueprint
from meross.services.toggleDeviceService import ToggleDeviceService
from meross.webApiOutcome.webApiOutcome import WebApiOutcome
from meross.core.httpRequest import HttpRequest
from meross.abstractions.webFilters.toggleDeviceFilter import ToggleDeviceFilter
from flask.wrappers import Response


ToggleDeviceRoute = Blueprint("ToggleDeviceRoute", __name__)


@ToggleDeviceRoute.route("/toggledevice", methods=["POST"])
async def webToggleDevice() -> Response:
    context = await HttpRequest.validateHttpPostRequestAndGetContext(request)

    if context:
        try:
            filters = ToggleDeviceFilter(request.data)
            webToggleDevice = await ToggleDeviceService.toggle(filters.toggledDevices, context)
            outcome = WebApiOutcome(webToggleDevice)
            return outcome

        except Exception as exception:
            return HttpRequest.customResponse(f"Error on /toggledevice: {exception.args[0]}")

    else:
        return HttpRequest.customResponse(HttpRequest.AUTHENTICATION_REQUIRED)
