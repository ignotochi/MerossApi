from flask import request, Blueprint
from meross.services.ToggleDeviceService import ToggleDeviceService
from meross.services.AuthService import AuthService
from meross.core.WebApiOutcome import WebApiOutcome
from meross.abstractions.filters.ToggleDeviceFilter import ToggleDeviceFilter


ToggleDeviceRoute = Blueprint("ToggleDeviceRoute", __name__)


@ToggleDeviceRoute.route("/toggleDevice", methods=["POST"])
def WebToggleDevice() -> WebApiOutcome:
    
    if request.method == "POST":
        token: str = request.headers.get("token")
        dataRequest: str = request.data

        try:
            if AuthService.ValidateApiToken(token) == True:

                filters = ToggleDeviceFilter(dataRequest)
                webToggleDevice = ToggleDeviceService.Toggle(filters.toggledDevices)
                outcome = WebApiOutcome(webToggleDevice)
                return outcome
            else:
                return WebApiOutcome("Authentication is needed")

        except Exception as exception:
            return {"WebToggleDeviceError": exception.args[0]}
