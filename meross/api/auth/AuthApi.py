from flask import request, Blueprint
from meross.abstractions.webOutcome.WebApiOutcome import WebApiOutcome
from meross.abstractions.webFilters.AuhtFilter import AuthFilter
from meross.services.AuthService import AuthService
from flask.wrappers import Response
from meross.core.HttpRequest import HttpRequest

AuthRoute = Blueprint('AuthRoute', __name__)


@AuthRoute.route("/auth", methods=['POST'])
def WebAuth() -> Response:
    if request.method == 'POST':

        try:
            filters = AuthFilter(request.data)
            outcome = WebApiOutcome(AuthService.CreateContext(filters))
            return outcome

        except Exception as exception:
            HttpRequest.LoginErrorResponse(f"Error on /auth: {exception.args[0]}")

    else:
        return HttpRequest.CustomResponse(HttpRequest.BAD_REQUEST_TYPE)
