import asyncio
import json
from ..meross.LoadDevices.LoadDevices import Devices
from ..abstractions.Device import Device
from ..abstractions.OutcomeJsonEncoder import OutcomeJsonEncoder
from ..meross.LoadDevices.LoadDeviceHelepr import LoadDeviceHelper

def searchDevices(user, passwd):
    devices = asyncio.run(Devices.LoadMerossDevices(user, passwd))

    result: Device = []

    for device in devices:
        outcome = LoadDeviceHelper.MapDevice(device)
        result.append(outcome)
        
    serializedResult = json.dumps(result, sort_keys=True, indent=4, cls = OutcomeJsonEncoder)

    return serializedResult
