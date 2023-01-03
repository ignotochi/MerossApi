from flask import request, Blueprint
from flask_cors import cross_origin
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.core.logger import MerossLogger
from meross.services.AuthService import AuthService
from flask.wrappers import Response
from meross.core.HttpRequest import HttpRequest

CheckRoute = Blueprint('CheckRoute', __name__)


@CheckRoute.route("/check", methods=['POST'])
async def WebCheck() -> Response:
    if request.method == 'POST':

        try:
            outcome = WebApiOutcome(await AuthService.ValidateUserContext(HttpRequest.GetUserApiToken(request)))
            return outcome

        except Exception as exception:
            HttpRequest.LoginErrorResponse(f"Error on /check: {exception.args[0]}")

    else:
        return HttpRequest.CustomResponse(HttpRequest.BAD_REQUEST_TYPE)
