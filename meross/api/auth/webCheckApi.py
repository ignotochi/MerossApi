from flask import request, Blueprint
from meross.abstractions.webOutcome.webApiOutcome import WebApiOutcome
from meross.services.authService import AuthService
from flask.wrappers import Response
from meross.core.httpRequest import HttpRequest

CheckRoute = Blueprint('CheckRoute', __name__)


@CheckRoute.route("/check", methods=['POST'])
async def webCheck() -> Response:
    if request.method == 'POST':

        try:
            outcome = WebApiOutcome(await AuthService.validateUserContext(HttpRequest.getUserApiToken(request)))
            return outcome

        except Exception as exception:
            HttpRequest.loginError(f"Error on /check: {exception.args[0]}")

    else:
        return HttpRequest.customResponse(HttpRequest.BAD_REQUEST_TYPE)
