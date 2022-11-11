from flask import Flask, request, Blueprint
from ..services.ToggleDeviceService import ToggleDeviceService
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.filters.ToggleDeviceFilter import ToggleDeviceFilter

ToggleDeviceRoute = Blueprint('ToggleDeviceRoute', __name__)

@ToggleDeviceRoute.route("/toggleDevice", methods=['POST'])
def WebToggleDevice():
    if (request.method == 'POST'):

        user: str = request.args.get('user')
        passwd: str = request.args.get('passwd')
        data: str = request.data
        
        outcome = WebApiOutcome()
        toggleDeviceFilter = ToggleDeviceFilter(data)

        try:
            webToggleDevice = ToggleDeviceService(user, passwd, toggleDeviceFilter.toggledDevices)
            outcome = WebApiOutcome(webToggleDevice)
        except Exception as e:
            print(f'Error when Toggle Device Controller: {e}')

    return outcome