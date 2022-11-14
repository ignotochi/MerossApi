from flask import Flask, request, Blueprint
from ..services.AuthService import LogOut, ValidateApiToken
from ..tools.WebApiOutcome import WebApiOutcome


LogOutRoute = Blueprint('WebLogOutRoute', __name__)

@LogOutRoute.route("/logout", methods=['GET'])

def WebLogOut() -> WebApiOutcome:
    if (request.method == 'GET'):

        token: str = request.args.get('token')

        try:
            outcome = WebApiOutcome()

            if (ValidateApiToken(token) == True):
                outcome = WebApiOutcome(LogOut())
        
            return outcome
                
        except Exception as e:
            print(f'Error on Load Devices: {e}')