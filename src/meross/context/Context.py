from cryptography.fernet import Fernet
from meross.resources.manager.Manager import Manager
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.core.Singleton import Singleton
from meross.abstractions.iContext import IContext
from meross.abstractions.IManager import IManager

@Singleton
class Context(IContext):

    @classmethod
    def __init__(cls, user: str, passwd: str):

        cls.__fernet: Fernet
        cls.__localToken: str

        cls.authenticated: bool = False
        cls.client: MerossHttpClient
        cls.manager: MerossManager

        if cls.manager is not isinstance(cls.manager, MerossManager):
            try:
                # generate a key for encryption and decryption
                # You can use fernet to generate
                # the key or use random key generator
                # here I'm using fernet to generate key
                key = Fernet.generate_key()

                # Instance the Fernet class with the key
                cls.__fernet = Fernet(key)
                
                _manager: IManager = Manager(user, passwd)

                cls.manager = _manager.manager          
                cls.client = _manager.client

                if (isinstance(cls.manager, MerossManager) and isinstance(cls.client, MerossHttpClient)):
                    cls.authenticated = len(cls.manager._cloud_creds.token) > 0

                    if (cls.authenticated):
                        cls.__localToken = cls.__Encrypt(cls.manager._cloud_creds.token)
            
            except Exception as exception:
                raise Exception("Error on context creation: " + str(exception.args[0]))

    @classmethod
    def GetToken(cls) -> str:
        if len(cls.__localToken) > 0:
            return str(cls.__localToken)
        else:
            return str()

    @classmethod
    def __Encrypt(cls, value: str) -> str:
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        if len(value) > 0:
            encripted = str(cls.__fernet.encrypt(value.encode()))
            return encripted
        else:
            return str()

    @classmethod
    def DecryptLocalToken(cls) -> str:
        # decrypt the encrypted string with the
        # Fernet instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        try:
            if (cls.__localToken and cls.authenticated == True):
                decriptedToken = cls.__fernet.decrypt(cls.__localToken).decode()

                return decriptedToken
            else:
                return str()

        except Exception as exception:
            error = "DecryptLocalTokenError: " +  str(exception.args[0])
            raise Exception(error)
    
    @classmethod
    def Reset(cls) -> None:
        del cls.__localToken
        del cls.__fernet
        del cls.authenticated
        del cls.manager
        del cls.client
        Singleton.Clean(cls)    
        mng = Manager()
        mng.Reset()
