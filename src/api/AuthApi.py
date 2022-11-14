from flask import Flask, request, Blueprint
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.filters.Credentials import Credentials
from ..services.AuthService import AuthService

AuthSingletonRoute = Blueprint('WebSingletonRoute', __name__)

@AuthSingletonRoute.route("/auth", methods=['POST'])

def WebSingletonAuth() ->  WebApiOutcome :
    if (request.method == 'POST'):

        data: str = request.data
     
        try:
            outcome = WebApiOutcome()
            credentials = Credentials(data) 
            
            outcome = WebApiOutcome(AuthService(credentials)   )
            return outcome
        
        except Exception as e:
            print (f'Error on Auth controller: {e}')