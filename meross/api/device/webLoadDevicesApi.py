from flask import request, Blueprint
from meross.services.loadDevicesService import LoadDevicesService
from webApiOutcome.webApiOutcome import WebApiOutcome
from meross.core.httpRequest import HttpRequest
from meross.abstractions.webFilters.deviceFilter import DeviceFilter
from flask.wrappers import Response


LoadDevicesRoute = Blueprint("LoadDevicesRoute", __name__)


@LoadDevicesRoute.route("/loaddevices", methods=["GET"])
async def webLoadDevices() -> Response:
    context = await HttpRequest.validateHttpGetRequestAndGetContext(request)

    if context:
        try:
            filters = DeviceFilter(request.args.get('DevicesFilter'))
            webDevices = await LoadDevicesService.load(filters.devices, context)
            outcome = WebApiOutcome(webDevices)
            return outcome

        except Exception as exception:
            return HttpRequest.customResponse(f"Error on /loaddevices: {exception.args[0]}")

    else:
        return HttpRequest.customResponse(HttpRequest.AUTHENTICATION_REQUIRED)
