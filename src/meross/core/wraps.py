import asyncio
from functools import wraps
from typing import Awaitable, Any, Callable


@staticmethod
def UpdateLoopManager(func: Callable) -> Any:
    
    def wrapper(*args):   
   
        @wraps(func)
        async def wrapped(*args) -> Awaitable:
            manager = args[0]
            eventLoop = asyncio.get_event_loop()
            manager._loop = eventLoop 
                
            return await func(*args)
            
        return asyncio.run(wrapped(*args))

    return wrapper

