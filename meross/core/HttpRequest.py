from telnetlib import AUTHENTICATION
from flask.wrappers import Response, Request
from meross.services.AuthService import AuthService


class HttpRequest:

    AUTHENTICATION_REQUIRED = "Authentication is needed"
    BAD_REQUEST_TYPE = "Wrong request type"
    USER_ALREADY_AUTHENTICATED = "User already authenticated"

    @staticmethod
    def ValidateHttpGetRequest(request: Request) -> bool:
        token = str(request.headers.get("token"))
        isGetRequest = request.method == "GET"
        isValid = AuthService.ValidateApiToken(token) is True
        return isValid and isGetRequest

    @staticmethod
    def ValidateHttpPostRequest(request: Request) -> bool:
        token = str(request.headers.get("token"))
        isPostRequest = request.method == "POST"
        isValid = AuthService.ValidateApiToken(token) is True
        return isValid and isPostRequest

    @staticmethod
    def GetUserApiToken(request: Request) -> str:
        token = str(request.headers.get("token"))
        return token

    @staticmethod
    def CustomResponse(response: str) -> Response:
        return Response(response)

    @staticmethod
    def CustomErrorResponse(message: str, error: str) -> Response:
        return Response(message + error)
