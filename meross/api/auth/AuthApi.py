from flask import request, Blueprint
from meross.abstractions.weboutcome.WebApiOutcome import WebApiOutcome
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
            error = str(exception.args[0])
            return HttpRequest.CustomErrorResponse("Web Auth Error: ", error)

    else:
        return HttpRequest.CustomResponse(HttpRequest.BAD_REQUEST_TYPE)
