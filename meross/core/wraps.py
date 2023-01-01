import asyncio
from functools import wraps
from typing import Awaitable, Any, Callable


def UpdateLoopManager(func: Callable) -> Any:
    def wrapper(*args):

        @wraps(func)
        async def wrapped(*args) -> Awaitable:
            manager = args[0]
            eventLoop = asyncio.get_event_loop()
            manager._loop = eventLoop

            return await func(*args)

        try:
            loop = asyncio.get_running_loop()

        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            tsk = loop.create_task(wrapped(*args))
            tsk.add_done_callback(lambda t: print(f'Task done with result={t.result()}'))

            return tsk

        else:
            result = asyncio.run(wrapped(*args))
            return result

    return wrapper
