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
            Context(auth.credentials.user, auth.credentials.password)
            
            auth.Reset()

            token = Context.GetToken()

            if (token):
                return token

        except Exception as e:
            print(f'Error Auth Service: {e}')

    @staticmethod
    def ValidateApiToken(token: str) -> bool:
        try:
            validLocalToken: bool = Context.manager._cloud_creds.token == Context.DecryptLocalToken()

            if (validLocalToken):
                return (Context.authenticated == True and validLocalToken == True)
            else:
                raise Exception("Invalid local token")

        except Exception as e:
            print(f'Error on validation token: {e}')

    @staticmethod
    def LogOut() -> bool:
        result = asyncio.run(ManagerUtils.StopManagerAndLogOut(
            Context.manager, Context.client))
        Context.Reset()

        return result
