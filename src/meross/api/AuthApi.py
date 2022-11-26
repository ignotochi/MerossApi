from flask import request, Blueprint
from meross.core.WebApiOutcome import WebApiOutcome 
from meross.abstractions.filters.Credentials import Credentials
from meross.services.AuthService import AuthService


AuthSingletonRoute = Blueprint('WebSingletonRoute', __name__)

@AuthSingletonRoute.route("/auth", methods=['POST'])

def WebSingletonAuth() ->  WebApiOutcome :
    if (request.method == 'POST'):

        data: str = request.data
     
        try:
            filters = Credentials(data) 
            outcome = WebApiOutcome(AuthService.CreateContext(filters))
            return outcome
        
        except Exception as exception:
            return {"WebSingletonAuthError" : exception.args[0]}