import asyncio
from meross.abstractions.context.Context import Context
from meross.abstractions.context.IContext import IContext
from meross.abstractions.webFilters.AuhtFilter import AuthFilter
from meross.resources.manager.ManagerUtils import ManagerUtils
from typing import Union


class AuthService:

    @staticmethod
    def CreateContext(auth: AuthFilter) -> str:
        try:
            if len(auth.credentials.user) > 0 and len(auth.credentials.password) > 0:
                context = Context(None, auth.credentials.user, auth.credentials.password)
                return context.GetToken()
            else:
                return "Credentials are required"

        except Exception as exception:
            return "CreateContextError: " + str(exception.args[0])

    @staticmethod
    def RetrieveUserContext(token: str) -> Union[IContext, None, str]:
        try:
            context = Context(token)

            if context.GetToken() == token:
                return context
            else:
                return None

        except Exception as exception:
            return "RetrieveUserContextError: " + str(exception.args[0])

    @staticmethod
    def ValidateApiToken(token: str) -> Union[bool, str]:
        try:
            context = AuthService.RetrieveUserContext(token)

            if context is not None and context.authenticated is True:
                validLocalToken: bool = token == context.GetToken()
                isValid = context.authenticated is True and validLocalToken is True
                return isValid

            else:
                return False

        except Exception as exception:
            return "ValidateApiTokenError: " + str(exception.args[0])

    @staticmethod
    def LogOut(context: IContext) -> str:
        try:
            closed = asyncio.run(ManagerUtils.StopManagerAndLogOut(context.manager, context.client))
            return "disconnected: " + str(closed)

        except Exception as exception:
            return "LogOutError: " + str(exception.args[0])

        finally:
            context.Reset()
