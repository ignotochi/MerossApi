import asyncio
from meross.context.Context import Context
from meross.abstractions.filters.Credentials import Credentials
from meross.resources.manager.ManagerUtils import ManagerUtils


class AuthService:
    
    context: Context = None

    @classmethod
    def CreateContext(cls, auth: Credentials) -> str:
        try:
            newContextRequired: bool = (cls.context == None or cls.context.authenticated == False)

            if (newContextRequired):
                cls.context = Context(auth.credentials.user, auth.credentials.password)
                return cls.context.GetToken()

            else:
                return {"Auth": "User already authenticated"}

        except Exception as exception:
            return {"CreateContextError" : exception.args[0]}

    @classmethod
    def ValidateApiToken(cls, token: str) -> bool:
        try:                    
            if (cls.context != None and cls.context.authenticated == True):
                
                validLocalToken: bool = token == cls.context.GetToken() 

                if (validLocalToken):
                    return (cls.context.authenticated == True and validLocalToken == True)
            else:
                return False

        except Exception as exception:
            return {"ValidateApiTokenError" : exception.args[0]}

    @classmethod
    def LogOut(cls) -> bool: 
        result = asyncio.run(ManagerUtils.StopManagerAndLogOut(cls.context.manager, cls.context.client))
        cls.context.Reset()
        return {"disconnected": result}
