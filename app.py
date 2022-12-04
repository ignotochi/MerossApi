from flask import Flask
from meross.api.Device import ToggleDeviceApi, LoadDevicesApi
from meross.api.auth import LogOutApi, AuthApi

app = Flask(__name__)

app.register_blueprint(ToggleDeviceApi.ToggleDeviceRoute)
app.register_blueprint(LoadDevicesApi.LoadDevicesRoute)
app.register_blueprint(AuthApi.AuthRoute)
app.register_blueprint(LogOutApi.LogOutRoute)

if __name__ == "__main__":
    app.run("localhost", 4449, load_dotenv=True)
