from flask import Flask
from flask_cors import CORS

from meross.api.device import ToggleDeviceApi, LoadDevicesApi
from meross.api.auth import LogOutApi, AuthApi, CheckToken

app = Flask(__name__)


app.register_blueprint(ToggleDeviceApi.ToggleDeviceRoute)
app.register_blueprint(LoadDevicesApi.LoadDevicesRoute)
app.register_blueprint(AuthApi.AuthRoute)
app.register_blueprint(CheckToken.CheckRoute)
app.register_blueprint(LogOutApi.LogOutRoute)

apiCorsConfig = {
    "origins": "*",
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": "*"}

cors = CORS(app, resources={"/*": apiCorsConfig})

if __name__ == "__main__":
    app.run("localhost", 4449, load_dotenv=True)

