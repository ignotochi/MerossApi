from flask import Flask, request
from ..services.LoadDevicesService import searchDevices

app = Flask(__name__)

@app.route("/loaddevices", methods=['GET'])
    
def Search():
    if (request.method == 'GET'):
      
      user = request.args.get('user')
      passwd = request.args.get('passwd')

      outcome = searchDevices(user, passwd)
        
    return outcome
