import asyncio
from ..context.context import Context
from ..abstractions.filters.Credentials import Credentials
from ..abstractions.auth import Auth
from ..resources.manager.ManagerUtils import ManagerUtils
from meross_iot.manager import MerossManager


class AuthService:

    @staticmethod
    def CreateContext(auth: Credentials) -> str:
        try:
            newContextRequired: bool = (isinstance(Context, object) and not hasattr(Context, 'manager'))

            if (newContextRequired):
                context = Context(auth.credentials.user, auth.credentials.password)
                auth.Reset()
                return context.GetToken()

            else:
                return {"Auth": "User already authenticated"}

        except Exception as exception:
            return {"CreateContextError" : exception.args[0]}

    @staticmethod
    def ValidateApiToken(token: str) -> bool:
        try:        
            context = Context()
            
            if (isinstance(context, object) and hasattr(context, 'authenticated') and context.authenticated == True):
                
                validLocalToken: bool = context.manager._cloud_creds.token == context.DecryptLocalToken()

                if (validLocalToken):
                    return (context.authenticated == True and validLocalToken == True)
            else:
                return False

        except Exception as exception:
            return {"ValidateApiTokenError" : exception.args[0]}

    @staticmethod
    def LogOut() -> bool:
        context = Context()
        result = asyncio.run(ManagerUtils.StopManagerAndLogOut(context.manager, context.client))
        context.Reset()
        return {"disconnected": result}
