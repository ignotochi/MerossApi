from flask import Flask, request
from ..services.SwitchDeviceService import ToggleDevice
from ..tools.WebApiOutcome import WebApiOutcome

# app = Flask(__name__)

@app.route("/toggleDevice", methods=['POST'])
def WebToggleDevice():
    if (request.method == 'POST'):

        user = request.args.get('user')
        passwd = request.args.get('passwd')
        
        outcome: WebApiOutcome

        try:
            outcome = WebApiOutcome(ToggleDevice(user, passwd)).result
        except:
            print("Error on toggle device")

    return outcome