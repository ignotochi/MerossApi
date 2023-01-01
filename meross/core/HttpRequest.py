from flask import abort
from flask.wrappers import Response, Request

from meross.abstractions.context import IContext
from meross.abstractions.webFilters.AuhtFilter import AuthFilter
from meross.services.AuthService import AuthService


class HttpRequest:
    AUTHENTICATION_REQUIRED = "Authentication is needed"
    BAD_REQUEST_TYPE = "Wrong request type"
    USER_ALREADY_AUTHENTICATED = "User already authenticated"

    @staticmethod
    async def ValidateHttpGetRequestAndGetContext(request: Request) -> IContext:
        token = str(request.headers.get("token"))
        isGetRequest = request.method == "GET"
        context = await AuthService.RetrieveUserContext(token)

        if context is not None and isGetRequest:
            return context
        else:
            return None

    @staticmethod
    async def ValidateHttpPostRequestAndGetContext(request: Request) -> IContext:
        token = str(request.headers.get("token"))
        isPostRequest = request.method == "POST"
        context = await AuthService.RetrieveUserContext(token)

        if context is not None and isPostRequest:
            return context
        else:
            return None

    @staticmethod
    def GetUserApiToken(request: Request) -> str:
        token = str(request.headers.get("token"))
        if len(token) > 0:
            return token
        else:
            return str()

    @staticmethod
    def CustomResponse(response: str) -> Response:
        response = Response(response)
        response.status_code = 500
        return response

    @staticmethod
    def LoginErrorResponse(error: str):
        abort(500, error)
