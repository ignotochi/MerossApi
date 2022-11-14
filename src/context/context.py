import asyncio
from cryptography.fernet import Fernet
from ..abstractions.auth import Auth
from ..resource.meross.Manager import Manager
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient


class Context:
    _fernet: Fernet
    _instance = None
    _token: str = None

    authenticated: bool = False
    manager: MerossManager = None
    client: MerossHttpClient = None

    async def NewContext(user: str, passwd: str):
        if Context._instance is None:
            # generate a key for encryption and decryption
            # You can use fernet to generate
            # the key or use random key generator
            # here I'm using fernet to generate key
            key = Fernet.generate_key()

            # Instance the Fernet class with the key
            Context._fernet = Fernet(key)

            combinedCredentials = user + "|" + passwd

            Context._instance = Context()

            await Manager.Start(user, passwd)
            
            Context.manager = Manager.manager
            
            Context.client = Manager.client

            Context.authenticated = len(Context.manager._cloud_creds.token) > 0

            if (Context.authenticated):
                Context._token = Context.__Encrypt(combinedCredentials)

        return Context._instance

    def GetToken() -> str:
        return str(Context._token)

    def __Encrypt(value: str) -> str:
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        if (value):
            return Context._fernet.encrypt(value.encode())
        else:
            return ""

    def Credentials() -> Auth:
        # decrypt the encrypted string with the
        # Fernet instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        try:
            if (Context._token and Context.authenticated == True):
                _decriptedCredentials = Context._fernet.decrypt(
                    Context._token).decode()
                _splittedCredentials = str(_decriptedCredentials).split("|")

                _credentials = Auth()
                _credentials.user = _splittedCredentials[0]
                _credentials.password = _splittedCredentials[1]

                return _credentials
            else:
                return Auth()

        except Exception as e:
            print(f'Error on get credentials: {e}')
            
    def Reset() -> None:
        Context.client = None
        Context.manager = None
        Context._instance = None
