from flask import Flask, request, Blueprint
from ..tools.WebApiOutcome import WebApiOutcome
from ..abstractions.filters.Credentials import Credentials
from ..services.AuthService import AuthService

authSingletonRoute = Blueprint('WebSingletonRoute', __name__)

@authSingletonRoute.route("/auth", methods=['POST'])
def WebSingletonAuth() ->  WebApiOutcome :
    if (request.method == 'POST'):

        data: str = request.data
     
        try:
            outcome = WebApiOutcome()
            credentials = Credentials(data) 
            
            token = AuthService(credentials)    
            outcome = WebApiOutcome(token)
            return outcome
        
        except Exception as e:
            print (f'Error on Auth controller: {e}')