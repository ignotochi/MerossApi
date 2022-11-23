from flask import request, Blueprint
from merossApi.services.ToggleDeviceService import ToggleDeviceService
from merossApi.services.AuthService import AuthService
from merossApi.core.WebApiOutcome import WebApiOutcome
from merossApi.abstractions.filters.ToggleDeviceFilter import ToggleDeviceFilter


ToggleDeviceRoute = Blueprint('ToggleDeviceRoute', __name__)

@ToggleDeviceRoute.route("/toggleDevice", methods=['POST'])

def WebToggleDevice() -> WebApiOutcome:
    if (request.method == 'POST'):

        token: str = request.headers.get('token')
        dataRequest: str = request.data
    
        try:
            outcome = WebApiOutcome()

            if (AuthService.ValidateApiToken(token) == True):
                outcome = WebApiOutcome()
                toggleDeviceFilter = ToggleDeviceFilter(dataRequest)
                
                webToggleDevice = ToggleDeviceService.Toggle(toggleDeviceFilter.toggledDevices)       
                outcome = WebApiOutcome(webToggleDevice)
            
            return outcome
        
        except Exception as exception:
            return {"WebToggleDeviceError" : exception.args[0]}
