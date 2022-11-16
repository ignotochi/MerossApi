from flask import Flask, request, Blueprint
from ..services.LoadDevicesService import LoadDevicesService
from ..services.AuthService import AuthService
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.filters.DevicesFilter import DevicesFilter


LoadDevicesRoute = Blueprint('LoadDevicesRoute', __name__)

@LoadDevicesRoute.route("/loaddevices", methods=['GET'])

def WebLoadDevices() -> WebApiOutcome:
    if (request.method == 'GET'):

        token: str = request.headers.get('token')
        dataRequest: str = request.data

        try:
            outcome = WebApiOutcome()
            devicesFilter = DevicesFilter(dataRequest)
        
            if (AuthService.ValidateApiToken(token) == True):
                webDevices = LoadDevicesService.Load(devicesFilter.devices)
                outcome = WebApiOutcome(webDevices)
            
            return outcome
                
        except Exception as e:
            print(f'Error on Load Devices: {e}')
