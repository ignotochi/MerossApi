from flask import Flask, request
from ..services.LoadDevicesService import SearchDevices
from ..tools.WebApiOutcome import WebApiOutcome

# app = Flask(__name__)

@app.route("/toggleDevice", methods=['POST'])
def WebToggleDevice():
    if (request.method == 'POST'):

        user = request.args.get('user')
        passwd = request.args.get('passwd')

        try:
            outcome = WebApiOutcome(SearchDevices(user, passwd))
        except:
            print("Error on toggle device")

    return outcome.result