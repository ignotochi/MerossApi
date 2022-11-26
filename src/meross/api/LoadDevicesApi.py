from flask import request, Blueprint
from meross.services.LoadDevicesService import LoadDevicesService
from meross.services.LoadDevicesService import LoadDevicesService
from meross.services.AuthService import AuthService
from meross.core.WebApiOutcome import WebApiOutcome
from meross.abstractions.filters.DevicesFilter import DevicesFilter


LoadDevicesRoute = Blueprint("LoadDevicesRoute", __name__)


@LoadDevicesRoute.route("/loaddevices", methods=["GET"])
def WebLoadDevices() -> WebApiOutcome:
    
    if request.method == "GET":
        token: str = request.headers.get("token")
        dataRequest: str = request.data

        try:
            if AuthService.ValidateApiToken(token) == True:

                filters = DevicesFilter(dataRequest)
                webDevices = LoadDevicesService.Load(filters.devices)
                outcome = WebApiOutcome(webDevices)
                return outcome
            else:
                return WebApiOutcome("Authentication is needed")

        except Exception as exception:
            return {"WebLoadDevicesError": exception.args[0]}
