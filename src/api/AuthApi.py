from flask import Flask, request, Blueprint
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.filters.AuthFilter import AuthFilter
from ..services.AuthService import AuthService

authSingletonRoute = Blueprint('WebSingletonRoute', __name__)

@authSingletonRoute.route("/auth", methods=['POST'])
def WebSingletonAuth() ->  WebApiOutcome :
    if (request.method == 'POST'):

        data: str = request.data
    
        outcome = WebApiOutcome()
        authFilter = AuthFilter(data)
        
        try:
            token = AuthService(authFilter)
            authFilter = None         
            outcome = WebApiOutcome(token)
        except Exception as e:
            print (f'Error on Load Devices: {e}')

    return outcome