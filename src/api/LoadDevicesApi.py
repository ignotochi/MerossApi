from flask import Flask, request
from ..services.LoadDevicesService import SearchDevices
from ..tools.WebApiOutcome import WebApiOutcome

app = Flask(__name__)

@app.route("/loaddevices", methods=['GET'])
def WebSearchDevices():
    if (request.method == 'GET'):

        user = request.args.get('user')
        passwd = request.args.get('passwd')
        
        outcome: WebApiOutcome

        try:
            outcome = WebApiOutcome(SearchDevices(user, passwd)).result
        except:
            print("Error on search Devices")

    return outcome