from flask import request, Blueprint
from meross.services.AuthService import AuthService
from meross.core.WebApiOutcome import WebApiOutcome


LogOutRoute = Blueprint("WebLogOutRoute", __name__)

@LogOutRoute.route("/logout", methods=["GET"])
def WebLogOut() -> WebApiOutcome:
    
    if request.method == "GET":
        token: str = request.headers.get("token")

        try:
            if AuthService.ValidateApiToken(token) == True:
                outcome = WebApiOutcome(AuthService.LogOut())
                return outcome
            else:
                return WebApiOutcome("Authentication is needed")

        except Exception as exception:
            return {"WebLogOutError": exception.args[0]}