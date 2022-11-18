import asyncio
from cryptography.fernet import Fernet
from ..abstractions.auth import Auth
from ..resources.manager.Manager import Manager
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from ..core.Singleton import Singleton

@Singleton
class Context(object):

    __fernet: Fernet = None
    __localToken: str = None

    authenticated: bool = False
    client: MerossHttpClient = None
    manager: MerossManager = None

    @classmethod
    def __init__(cls, user: str, passwd: str):
        if cls.manager is None:
            try:
                # generate a key for encryption and decryption
                # You can use fernet to generate
                # the key or use random key generator
                # here I'm using fernet to generate key
                key = Fernet.generate_key()

                # Instance the Fernet class with the key
                cls.__fernet = Fernet(key)

                cls.manager = Manager(user, passwd).manager

                cls.authenticated = len(cls.manager._cloud_creds.token) > 0

                if (cls.authenticated):
                    cls.__localToken = cls.__Encrypt(
                        cls.manager._cloud_creds.token)
            
            except Exception as exception:
                raise  

    @staticmethod
    def GetToken() -> str:
        if (Context.__localToken != None):
            return str(Context.__localToken)
        else:
            return None

    @staticmethod
    def __Encrypt(value: str) -> str:
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        if (value):
            return Context.__fernet.encrypt(value.encode())
        else:
            return ""

    @staticmethod
    def DecryptLocalToken() -> str:
        # decrypt the encrypted string with the
        # Fernet instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        try:
            if (Context.__localToken and Context.authenticated == True):
                decriptedToken = Context.__fernet.decrypt(
                    Context.__localToken).decode()

                return decriptedToken
            else:
                return None

        except Exception as exception:
            return {"DecryptLocalTokenError" : exception.args[0]}

    @classmethod
    def Reset(cls) -> None:
        cls.__localToken = None
        cls.__fernet = None
        cls.authenticated = False
        cls.manager.Reset()
        cls.manager = None
