from flask import request, Blueprint
from meross.services.AuthService import AuthService
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from flask.wrappers import Response


LogOutRoute = Blueprint("WebLogOutRoute", __name__)


@LogOutRoute.route("/logout", methods=["GET"])
def WebLogOut() -> Response:

    if HttpRequest.ValidateHttpGetRequest(request):

        userToken = HttpRequest.GetUserApiToken(request)
        context = AuthService.RetrieveUserContext(userToken)

        try:
            outcome = WebApiOutcome(AuthService.LogOut(context))
            return outcome

        except Exception as exception:
            error = exception.args[0]
            return HttpRequest.CustomErrorResponse("Web LogOut Error: ", error)

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)