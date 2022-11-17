import asyncio
import os
from ..context.context import Context
from ..abstractions.filters.Credentials import Credentials
from ..abstractions.auth import Auth
from ..resources.meross.ManagerUtils import ManagerUtils


class AuthService:

    @staticmethod
    def CreateContext(auth: Credentials) -> str:
        try:
            newContextRequired: bool = (Context.authenticated == False and Context.GetToken() == None )
            
            if (newContextRequired):
                Context(auth.credentials.user, auth.credentials.password)
                auth.Reset()
                return Context.GetToken()
            
            else:
                return { "authenticated":"True" }

        except Exception as e:
            print(f'Error Auth Service: {e}')

    @staticmethod
    def ValidateApiToken(token: str) -> bool:
        try:
            validLocalToken: bool = Context.managerTools.manager._cloud_creds.token == Context.DecryptLocalToken()

            if (validLocalToken):
                return (Context.authenticated == True and validLocalToken == True)
            else:
                raise Exception("Invalid local token")

        except Exception as e:
            print(f'Error on validation token: {e}')

    @staticmethod
    def LogOut() -> bool:
        result = asyncio.run(ManagerUtils.StopManagerAndLogOut(Context.managerTools.client))
        Context.Reset()
        return {"disconnected": result }
