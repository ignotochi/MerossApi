import asyncio
from typing import Union
from datetime import datetime
from meross.core.singleton.singleton import Singleton
from meross.abstractions.context.context import Context
from meross.abstractions.context.context_interface import IContext
from meross.abstractions.webFilters.auhtFilter import AuthFilter
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.manager.manager import Manager


class AuthService:

    @staticmethod
    def createContext(auth: AuthFilter) -> object:
        try:
            if len(auth.credentials.user) > 0 and len(auth.credentials.password) > 0:
                context: IContext = Context(None, auth.credentials.user, auth.credentials.password)
                return {"token": context.getToken()}
            else:
                return {"token": str()}

        except Exception as exception:
            raise Exception(ExceptionManager.catch(exception))

    @staticmethod
    async def managerSessionIsActive(context: IContext) -> bool:
        try:
            dt: datetime = datetime.now()
            minutesBetweenNowAndLastCheck = divmod((dt - context.sessionActivityLastTimeCheck).total_seconds(), 60)[0]
            context.setSessionActivityLastTimeCheck(dt)

            if minutesBetweenNowAndLastCheck > 30:
                testExecution = await Manager.testManagerConnection(context.manager, context.client)
                return testExecution

            else:
                return True

        except Exception as exception:
            MerossLogger("AuthService.managerSessionIsActive").writeErrorLog(ExceptionManager.catch(exception))
            return False

    @staticmethod
    async def validateUserContext(token: str) -> object:
        try:
            if len(token) > 0:
                context: IContext = await AuthService.retrieveUserContext(token)

                if context is not None and \
                        await AuthService.managerSessionIsActive(context) and context.getToken() == token:
                    return {"token": context.getToken()}

                else:
                    if context is not None:
                        context.reset()
                        return {"token": str()}

                    elif context is None:
                        return {"token": str()}
            else:
                return {"token": str()}

        except Exception as exception:
            MerossLogger("AuthService.validateUserContext").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception("Error trying to validate user context")

    @staticmethod
    async def retrieveUserContext(token: str) -> Union[IContext, None]:
        try:
            contextToken = Singleton.get(token)

            if contextToken is not None:
                context: IContext = Singleton.get(token)['Context']

                if context is not None and context.getToken() == token \
                        and await AuthService.managerSessionIsActive(context):
                    return context
                else:
                    return None
            else:
                return None

        except Exception as exception:
            MerossLogger("AuthService.retrieveUserContext").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception("unrecoverable context")

    @staticmethod
    async def logOut(context: IContext) -> object:
        try:
            loop = asyncio.get_running_loop()

            if loop and loop.is_running():
                tsk = loop.create_task(Manager.stopManagerAndLogOut(context.manager, context.client))

                result = await tsk

                return {"logout": result}
            else:
                result: bool = asyncio.run(Manager.stopManagerAndLogOut(context.manager, context.client))
                return {"logout": result}

        except Exception as exception:
            raise Exception(exception.args[0])

        finally:
            context.reset()
