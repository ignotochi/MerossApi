from flask import Flask, request, abort
from .api import ToggleDeviceApi, LoadDevicesApi

app = Flask(__name__)
app.register_blueprint(ToggleDeviceApi.ToggleDeviceRoute)
app.register_blueprint(LoadDevicesApi.LoadDevicesRoute)



