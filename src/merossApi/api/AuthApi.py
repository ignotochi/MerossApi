from flask import request, Blueprint
from merossApi.core.WebApiOutcome import WebApiOutcome
from merossApi.abstractions.filters.Credentials import Credentials
from merossApi.services.AuthService import AuthService


AuthSingletonRoute = Blueprint('WebSingletonRoute', __name__)

@AuthSingletonRoute.route("/auth", methods=['POST'])

def WebSingletonAuth() ->  WebApiOutcome :
    if (request.method == 'POST'):

        data: str = request.data
     
        try:
            outcome = WebApiOutcome()
            credentials = Credentials(data) 
                
            outcome = WebApiOutcome(AuthService.CreateContext(credentials))
            return outcome
        
        except Exception as exception:
            return {"WebSingletonAuthError" : exception.args[0]}