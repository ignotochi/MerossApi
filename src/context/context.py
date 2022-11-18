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
                
                _manager = Manager(user, passwd)

                cls.manager = _manager.manager
                
                cls.client = _manager.client

                cls.authenticated = len(cls.manager._cloud_creds.token) > 0

                if (cls.authenticated):
                    cls.__localToken = cls.__Encrypt(cls.manager._cloud_creds.token)
            
            except Exception as exception:
                raise  

    @classmethod
    def GetToken(cls) -> str:
        if (cls.__localToken != None):
            return str(cls.__localToken)
        else:
            return None

    @classmethod
    def __Encrypt(cls, value: str) -> str:
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        if (value):
            return cls.__fernet.encrypt(value.encode())
        else:
            return ""

    @classmethod
    def DecryptLocalToken(cls) -> str:
        # decrypt the encrypted string with the
        # Fernet instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        try:
            if (cls.__localToken and cls.authenticated == True):
                decriptedToken = cls.__fernet.decrypt(
                    cls.__localToken).decode()

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
        cls.manager = None
