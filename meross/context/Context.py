from cryptography.fernet import Fernet
from meross.resources.manager.Manager import Manager
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.core.Singleton import Singleton
from meross.abstractions.IContext import IContext
from meross.abstractions.IManager import IManager


@Singleton.New
class Context(IContext):

    def manager(self, value):
        self.manager = value

    def authenticated(self, value):
        self.authenticated = value

    def client(self, value):
        self.client = value

    def fernet(self, value):
        self.fernet = value

    def token(self, value):
        self.token = value

    def __init__(self, token: str = None, user : str = None, passwd: str = None):

        self.fernet: Fernet
        self.token: str

        self.authenticated: bool = False
        self.client: MerossHttpClient
        self.manager: MerossManager

        if self.manager is not isinstance(self.manager, MerossManager):
            try:
                # generate a key for encryption and decryption
                # You can use fernet to generate
                # the key or use random key generator
                # here I'm using fernet to generate key
                key = Fernet.generate_key()

                # Instance the Fernet class with the key
                self.fernet = Fernet(key)

                instancedManager: IManager = Manager(user, passwd)

                self.manager = instancedManager.manager
                self.client = instancedManager.client

                if isinstance(self.manager, MerossManager) and isinstance(self.client, MerossHttpClient):
                    self.authenticated = len(self.manager.cloud_creds.token) > 0

                    if self.authenticated:
                        self.token = self.Encrypt(self.manager.cloud_creds.token)

            except Exception as exception:
                raise Exception("Error on context creation: " + str(exception.args[0]))

    def GetToken(self) -> str:
        if len(self.token) > 0:
            return str(self.token)
        else:
            return str()

    def Encrypt(self, value: str) -> str:
        # then use the Fernet class instance
        # to encrypt the string must
        # be encoded to byte string before encryption
        if len(value) > 0:
            encrypted = str(self.fernet.encrypt(value.encode()))
            return encrypted
        else:
            return str()

    def DecryptLocalToken(self) -> str:
        # decrypt the encrypted string with the
        # Fernet instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        try:
            if self.token and self.authenticated == True:
                decryptedToken = self.fernet.decrypt(self.token).decode()

                return decryptedToken
            else:
                return str()

        except Exception as exception:
            error = "DecryptLocalTokenError: " + str(exception.args[0])
            raise Exception(error)

    def Reset(self) -> None:
        Singleton.Clean(self)

