from dataclasses import dataclass

@dataclass()
class Device:
    deviceName: str
    deviceType: str
    firmwareVersion: str
    hardwareVersion: str
    deviceUid: str
    status: str


