from flask import Flask, request, Blueprint
from ..services.LoadDevicesService import LoadDevicesService
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.filters.DevicesFilter import DevicesFilter

LoadDevicesRoute = Blueprint('LoadDevicesRoute', __name__)

@LoadDevicesRoute.route("/loaddevices", methods=['GET'])
def WebLoadDevices() ->  WebApiOutcome :
    if (request.method == 'GET'):

        user: str = request.args.get('user')
        passwd: str = request.args.get('passwd')
        data: str = request.data
        
        outcome = WebApiOutcome()
        devicesFilter = DevicesFilter(data)

        try:
            webDevices = LoadDevicesService(user, passwd, devicesFilter.devices)
            outcome = WebApiOutcome(webDevices)
        except Exception as e:
            print (f'Error on Load Devices: {e}')

    return outcome
