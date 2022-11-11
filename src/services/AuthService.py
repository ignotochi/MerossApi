import asyncio
from ..context.context import Context
from ..abstractions.filters.AuthFilter import AuthFilter
from ..abstractions.auth import Auth


def AuthService(authFilter: AuthFilter) -> str:
    try:
        credentials: Auth = authFilter.credentials

        Context.NewContext(credentials.user, credentials.password)
        
        token = Context.GetToken()
                
        if (token): 
            authFilter = None
            credentials = None
            return token
                
    except Exception as e:
        print(f'Error Auth Service: {e}')

