import asyncio
from functools import wraps


@staticmethod
def UpdateLoopManager(func):
    def wrapper(*args):   
           
            @wraps(func)
            async def wrapped(*args):
                manager = args[0]
                eventLoop = asyncio.get_event_loop()
                manager._loop = eventLoop 
                
                return await func(*args)
            
            return asyncio.run(wrapped(*args))
    return wrapper

