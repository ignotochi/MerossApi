from flask import request, Blueprint
from webApiOutcome.webApiOutcome import WebApiOutcome
from meross.abstractions.webFilters.auhtFilter import AuthFilter
from meross.services.authService import AuthService
from flask.wrappers import Response
from meross.core.httpRequest import HttpRequest

AuthRoute = Blueprint('AuthRoute', __name__)


@AuthRoute.route("/auth", methods=['POST'])
def webAuth() -> Response:
    if request.method == 'POST':

        try:
            filters = AuthFilter(request.data)
            outcome = WebApiOutcome(AuthService.createContext(filters))
            return outcome

        except Exception as exception:
            HttpRequest.loginError(f"Error on /auth: {exception.args[0]}")

    else:
        return HttpRequest.customResponse(HttpRequest.BAD_REQUEST_TYPE)
