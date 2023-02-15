from flask import request, Blueprint
from meross.services.AuthService import AuthService
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.core.HttpRequest import HttpRequest
from flask.wrappers import Response


LogOutRoute = Blueprint("WebLogOutRoute", __name__)


@LogOutRoute.route("/logout", methods=["GET"])
async def WebLogOut() -> Response:
    context = await HttpRequest.ValidateHttpGetRequestAndGetContext(request)

    if context:
        try:
            outcome = WebApiOutcome(await AuthService.LogOut(context))
            return outcome

        except Exception as exception:
            return HttpRequest.CustomResponse(f"Error on /logout: {exception.args[0]}")

    else:
        return HttpRequest.CustomResponse(HttpRequest.AUTHENTICATION_REQUIRED)