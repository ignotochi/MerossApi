from flask import Flask, request, Blueprint
from ..services.AuthService import AuthService
from ..core.WebApiOutcome import WebApiOutcome


LogOutRoute = Blueprint('WebLogOutRoute', __name__)

@LogOutRoute.route("/logout", methods=['GET'])

def WebLogOut() -> WebApiOutcome:
    if (request.method == 'GET'):

        token: str = request.headers.get('token')

        try:
            outcome = WebApiOutcome()

            if (AuthService.ValidateApiToken(token) == True):
                outcome = WebApiOutcome(AuthService.LogOut())
        
            return outcome
                
        except Exception as e:
            print(f'Error on Load Devices: {e}')