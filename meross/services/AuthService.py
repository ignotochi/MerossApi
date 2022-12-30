import asyncio
from meross.abstractions.context.Context import Context
from meross.abstractions.context.IContext import IContext
from meross.abstractions.webFilters.AuhtFilter import AuthFilter
from meross.resources.manager.ManagerUtils import ManagerUtils
from meross.core.singleton.Singleton import Singleton
from typing import Union


class AuthService:

    @staticmethod
    def CreateContext(auth: AuthFilter) -> object:
        try:
            if len(auth.credentials.user) > 0 and len(auth.credentials.password) > 0:
                context: IContext = Context(None, auth.credentials.user, auth.credentials.password)
                return {"token": context.GetToken()}
            else:
                return {"token": str()}

        except Exception as exception:
            raise Exception("Error on context creation: " + str(exception.args[0]))

    @staticmethod
    def CheckSession(context: IContext) -> bool:
        state = context.client.stats.get_stats()

        if state is not None:
            return True
        else:
            return False

    @staticmethod
    def CheckContext(token: str) -> object:
        try:
            if len(token) > 0:
                context: IContext = AuthService.RetrieveUserContext(token)

                if context is not None and AuthService.CheckSession(context) and context.GetToken() == token:
                    return {"token": context.GetToken()}

                else:
                    if context is not None:
                        AuthService.RetrieveUserContext(token).Reset()
                        return {"token": str()}

                    elif context is None:
                        return {"token": str()}
            else:
                return {"token": str()}

        except Exception as exception:
            raise Exception("error checking the context")

    @staticmethod
    def RetrieveUserContext(token: str) -> Union[IContext, None]:
        try:
            contextToken = Singleton.Get(token)

            if contextToken is not None:
                context: IContext = Singleton.Get(token)['Context']

                if context is not None and context.GetToken() == token and AuthService.CheckSession(context):
                    return context
                else:
                    return None
            else:
                return None

        except Exception as exception:
            raise Exception("Error trying to retrieve context")

    @staticmethod
    def ValidateApiToken(token: str) -> Union[bool, str]:
        try:
            context: IContext = AuthService.RetrieveUserContext(token)

            if context is not None and context.authenticated is True:

                validLocalToken: bool = token == context.GetToken()
                isValid = context.authenticated is True and validLocalToken is True
                return isValid

            else:
                return False

        except Exception as exception:
            raise Exception("Error on token validation")

    @staticmethod
    def LogOut(context: IContext) -> str:
        try:
            closed = asyncio.run(ManagerUtils.StopManagerAndLogOut(context.manager, context.client))
            return "disconnected: " + str(closed)

        except Exception as exception:
            raise "Error on logout: " + str(exception.args[0])

        finally:
            context.Reset()
