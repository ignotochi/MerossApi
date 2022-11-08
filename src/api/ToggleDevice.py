from flask import Flask, request
from ..services.ToggleDeviceService import ToggleDevice
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.filters.ToggleDeviceFilter import ToggleDeviceFilter

app = Flask(__name__)

@app.route("/toggleDevice", methods=['POST'])
def WebToggleDevice():
    if (request.method == 'POST'):

        user: str = request.args.get('user')
        passwd: str = request.args.get('passwd')
        data: str = request.data
        
        outcome = WebApiOutcome()
        toggleDeviceFilter = ToggleDeviceFilter(data)

        try:
            webToggleDevice = ToggleDevice(user, passwd, toggleDeviceFilter.toggledDevices)
            outcome = WebApiOutcome(webToggleDevice).result
        except Exception as e:
            print(f'Error when Toggle Device Controller: {e}')

    return outcome