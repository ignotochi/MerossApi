from flask import request, Blueprint
from merossApi.services.LoadDevicesService import LoadDevicesService
from merossApi.services.AuthService import AuthService
from merossApi.core.WebApiOutcome import WebApiOutcome
from merossApi.abstractions.filters.DevicesFilter import DevicesFilter


LoadDevicesRoute = Blueprint('LoadDevicesRoute', __name__)

@LoadDevicesRoute.route("/loaddevices", methods=['GET'])

def WebLoadDevices() -> WebApiOutcome:
    if (request.method == 'GET'):

        token: str = request.headers.get('token')
        dataRequest: str = request.data

        try:
            outcome = WebApiOutcome()
            
            if (AuthService.ValidateApiToken(token) == True):
                outcome = WebApiOutcome()
                devicesFilter = DevicesFilter(dataRequest)
                
                webDevices = LoadDevicesService.Load(devicesFilter.devices)
                outcome = WebApiOutcome(webDevices)
            
            return outcome
                
        except Exception as exception:
            return {"WebLoadDevicesError" : exception.args[0]}
