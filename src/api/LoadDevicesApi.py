from flask import Flask, request
from ..services.LoadDevicesService import SearchDevices
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.DevicesFilter import DevicesFilter

app = Flask(__name__)

@app.route("/loaddevices", methods=['GET'])
def WebSearchDevices() ->  WebApiOutcome :
    if (request.method == 'GET'):

        user: str = request.args.get('user')
        passwd: str = request.args.get('passwd')
        
        outcome = WebApiOutcome()
        devicesFilter = DevicesFilter(request.data)

        try:
            outcome = WebApiOutcome(SearchDevices(user, passwd, devicesFilter)).result
        except Exception as e:
            print (f'Error on search Devices: {e}')

    return outcome
