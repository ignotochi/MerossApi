from flask import request, Blueprint
from meross.services.AuthService import AuthService
from meross.core.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from flask.wrappers import Response


LogOutRoute = Blueprint("WebLogOutRoute", __name__)


@LogOutRoute.route("/logout", methods=["GET"])
def WebLogOut() -> Response:

    if HttpRequest.ValidateHttpGetRequest(request):

        try:
            userToken = HttpRequest.GetUserApiToken(request)

            outcome = WebApiOutcome(AuthService.LogOut(userToken))
            return outcome

        except Exception as exception:
            error = exception.args[0]
            return HttpRequest.CustomErrorResponse("Web LogOut Error: ", error)

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)