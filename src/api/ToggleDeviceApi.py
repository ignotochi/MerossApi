from flask import Flask, request, Blueprint
from ..services.ToggleDeviceService import ToggleDeviceService
from ..services.AuthService import ValidateApiToken
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.filters.ToggleDeviceFilter import ToggleDeviceFilter

ToggleDeviceRoute = Blueprint('ToggleDeviceRoute', __name__)

@ToggleDeviceRoute.route("/toggleDevice", methods=['POST'])

def WebToggleDevice() -> WebApiOutcome:
    if (request.method == 'POST'):

        token: str = request.args.get('token')
        dataRequest: str = request.data
    
        try:
            outcome = WebApiOutcome()
            toggleDeviceFilter = ToggleDeviceFilter(dataRequest)
        
            if (ValidateApiToken(token) == True):
                webToggleDevice = ToggleDeviceService(toggleDeviceFilter.toggledDevices)
                outcome = WebApiOutcome(webToggleDevice)
            
            return outcome
        
        except Exception as e:
            print(f'Error when Toggle Device Controller: {e}')
