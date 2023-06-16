from flask import request, Blueprint
from meross.services.LoadDevicesService import LoadDevicesService
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from meross.abstractions.webFilters.DevicesFilter import DevicesFilter
from flask.wrappers import Response


LoadDevicesRoute = Blueprint("LoadDevicesRoute", __name__)


@LoadDevicesRoute.route("/loaddevices", methods=["GET"])
async def WebLoadDevices() -> Response:
    context = await HttpRequest.ValidateHttpGetRequestAndGetContext(request)

    if context:
        try:
            filters = DevicesFilter(request.args.get('DevicesFilter'))
            devices = await LoadDevicesService.Load(filters.devices, context)
            outcome = WebApiOutcome(devices)
            return outcome

        except Exception as exception:
            return HttpRequest.CustomResponse(f"Error on /loaddevices: {exception.args[0]}")

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)
