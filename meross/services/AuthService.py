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
    async def ManagerSessionIsActive(context: IContext) -> bool:
        try:
            if await context.client.async_list_devices():
                return True

        except Exception() as exception:
            return False

    @staticmethod
    async def ValidateUserContext(token: str) -> object:
        try:
            if len(token) > 0:
                context: IContext = await AuthService.RetrieveUserContext(token)

                if context is not None and \
                        await AuthService.ManagerSessionIsActive(context) and context.GetToken() == token:
                    return {"token": context.GetToken()}

                else:
                    if context is not None:
                        context.Reset()
                        return {"token": str()}

                    elif context is None:
                        return {"token": str()}
            else:
                return {"token": str()}

        except Exception as exception:
            raise Exception("error checking the context")

    @staticmethod
    async def RetrieveUserContext(token: str) -> Union[IContext, None]:
        try:
            contextToken = Singleton.Get(token)

            if contextToken is not None:
                context: IContext = Singleton.Get(token)['Context']

                if context is not None and context.GetToken() == token \
                        and await AuthService.ManagerSessionIsActive(context):
                    return context

                else:
                    return None
            else:
                return None

        except Exception as exception:
            raise Exception("Error trying to retrieve context")

    @staticmethod
    async def ValidateApiToken(token: str) -> Union[bool, str]:
        try:
            context: IContext = await AuthService.RetrieveUserContext(token)

            if context is not None and context.authenticated is True:

                validLocalToken: bool = token == context.GetToken()
                isValid = context.authenticated is True and validLocalToken is True
                return isValid

            else:
                return False

        except Exception as exception:
            raise Exception("Error on token validation")

    @staticmethod
    async def LogOut(context: IContext) -> str:
        try:
            try:
                loop = asyncio.get_running_loop()

            except RuntimeError:
                loop = None

            if loop and loop.is_running():
                tsk = loop.create_task(ManagerUtils.StopManagerAndLogOut(context.manager, context.client))

                return "disconnected: " + str(await tsk)

            else:
                result: bool = asyncio.run(ManagerUtils.StopManagerAndLogOut(context.manager, context.client))
                return "disconnected: " + str(result)

        except Exception as exception:
            raise "Error on logout: " + str(exception.args[0])

        finally:
            context.Reset()
