from flask import request, Blueprint
from meross.services.authService import AuthService
from webApiOutcome.webApiOutcome import WebApiOutcome
from meross.core.httpRequest import HttpRequest
from flask.wrappers import Response


LogOutRoute = Blueprint("WebLogOutRoute", __name__)


@LogOutRoute.route("/logout", methods=["GET"])
async def webLogOut() -> Response:
    context = await HttpRequest.validateHttpGetRequestAndGetContext(request)

    if context:
        try:
            outcome = WebApiOutcome(await AuthService.logOut(context))
            return outcome

        except Exception as exception:
            return HttpRequest.customResponse(f"Error on /logout: {exception.args[0]}")

    else:
        return HttpRequest.customResponse(HttpRequest.AUTHENTICATION_REQUIRED)