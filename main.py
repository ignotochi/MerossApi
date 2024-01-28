from flask import Flask
from flask_cors import CORS
from meross.api.device import webToggleDeviceApi, webLoadDevicesApi
from meross.api.auth import webLogoutApi, webAuthApi, webCheckApi

app = Flask(__name__)

app.register_blueprint(webToggleDeviceApi.ToggleDeviceRoute)
app.register_blueprint(webLoadDevicesApi.LoadDevicesRoute)
app.register_blueprint(webAuthApi.AuthRoute)
app.register_blueprint(webCheckApi.CheckRoute)
app.register_blueprint(webLogoutApi.LogOutRoute)


apiCorsConfig = {
    "origins": "*",
    "methods": ["OPTIONS", "GET", "POST"],
    "allow_headers": "*"}

cors = CORS(app, resources={"/*": apiCorsConfig})

if __name__ == "__main__":
    app.run("localhost", 4449, load_dotenv=True)
