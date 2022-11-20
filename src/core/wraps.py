from meross_iot.manager import MerossManager
import asyncio


@staticmethod
def UpdateLoopManager(manager: MerossManager, *args, **kw) -> None:
    eventLoop = asyncio.get_event_loop()
    manager._loop = eventLoop
