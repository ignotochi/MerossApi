import asyncio
from functools import wraps
from typing import Awaitable, Any, Callable

from meross.core.logger import MerossLogger


def UpdateLoopManager(func: Callable) -> Any:
    def wrapper(*args):

        eventLoop = asyncio.get_event_loop()

        try:
            @wraps(func)
            async def wrapped(*args) -> Awaitable:
                manager = args[0]
                manager._loop = eventLoop
                return await func(*args)

            loop = asyncio.get_running_loop()

            if loop and loop.is_running():
                return loop.create_task(wrapped(*args))

            else:
                result = asyncio.run(wrapped(*args))
                return result

        except Exception as exception:
            MerossLogger("UpdateLoopManager.wrapper").WriteErrorLog(exception.args[0])

    return wrapper
