from dataclasses import dataclass


@dataclass
class device:
    deviceName: str
    model: str
    firmwareVersion: str
    hardwareVersion: str
    deviceUid: str
    status: str
    ip: str
    active: bool

