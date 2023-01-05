import asyncio
from datetime import datetime

from meross.abstractions.context.Context import Context
from meross.abstractions.context.IContext import IContext
from meross.abstractions.webFilters.AuhtFilter import AuthFilter
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.resources.manager.ManagerUtils import ManagerUtils
from meross.core.singleton.Singleton import Singleton
from typing import Union, List


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
            raise Exception(ExceptionManager.TryToCatch(exception))

    @staticmethod
    async def ManagerSessionIsActive(context: IContext) -> bool:
        try:
            dt: datetime = datetime.now()
            minutesBetweenNowAndLastCheck = divmod((dt - context.sessionActivityLastTime).total_seconds(), 60)[0]

            if minutesBetweenNowAndLastCheck > 30:
                testExecution = await ManagerUtils.TestConnection(context.manager, context.client)

                if testExecution is True:
                    context.SetSessionActivityLastTimeCheck(dt)
                    return True
            else:
                context.SetSessionActivityLastTimeCheck(dt)
                return True

        except Exception as exception:
            MerossLogger("AuthService.ManagerSessionIsActive").WriteErrorLog(ExceptionManager.TryToCatch(exception))
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
            MerossLogger("AuthService.ValidateUserContext").WriteErrorLog(ExceptionManager.TryToCatch(exception))
            raise Exception("Error trying to validate user context")

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
            MerossLogger("AuthService.RetrieveUserContext").WriteErrorLog(ExceptionManager.TryToCatch(exception))
            raise Exception("unrecoverable context")

    @staticmethod
    async def LogOut(context: IContext) -> object:
        try:
            loop = asyncio.get_running_loop()

            if loop and loop.is_running():
                tsk = loop.create_task(ManagerUtils.StopManagerAndLogOut(context.manager, context.client))
                return {"logout": await tsk}
            else:
                result: bool = asyncio.run(ManagerUtils.StopManagerAndLogOut(context.manager, context.client))
                return {"logout": result}

        except Exception as exception:
            raise Exception(exception.args[0])

        finally:
            context.Reset()
