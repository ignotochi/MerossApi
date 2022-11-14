import asyncio
import os
from ..context.context import Context
from ..abstractions.filters.Credentials import Credentials
from ..abstractions.auth import Auth
from ..resource.meross.ManagerUtils import ManagerUtils


@staticmethod
def AuthService(auth: Credentials) -> str:
    try:
        asyncio.run(Context.NewContext(auth.credentials.user, auth.credentials.password))

        auth.Reset()

        token = Context.GetToken()

        if (token):
            return token

    except Exception as e:
        print(f'Error Auth Service: {e}')


@staticmethod
def ValidateApiToken(token: str) -> bool:
    try:
        contextToken = Context.GetToken()

        if (contextToken):
            return (Context.authenticated == True) and (contextToken == token)
        else:
            raise Exception("Context Token invalid")

    except Exception as e:
        print(f'Error on validation token: {e}')

@staticmethod
def LogOut() -> bool:
    result = asyncio.run(ManagerUtils.StopManagerAndLogOut(Context.manager, Context.client))
    Context.Reset()
    
    return result
    
