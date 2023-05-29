from datetime import datetime
from cryptography.fernet import Fernet
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.resources.manager.Manager import Manager
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.core.singleton.Singleton import Singleton
from meross.abstractions.context.IContext import IContext
from meross.abstractions.manager.IManager import IManager


@Singleton.New
class Context(IContext):

    def manager(self, value):
        self.manager = value

    def sessionActivityLastTime(self, value):
        self.sessionActivityLastTime = value

    def authenticated(self, value):
        self.authenticated = value

    def client(self, value):
        self.client = value

    def fernet(self, value):
        self.fernet = value

    def token(self, value):
        self.token = value

    def __init__(self, token: str = None, user: str = None, passwd: str = None):

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

                manager: IManager = Manager(user, passwd)

                self.manager = manager.manager
                self.client = manager.client

                if isinstance(self.manager, MerossManager) and isinstance(self.client, MerossHttpClient):
                    self.authenticated = len(self.client.cloud_credentials.token) > 0
                    self.SetSessionActivityLastTimeCheck(datetime.now())

                    if self.authenticated:
                        self.token = self.Encrypt(user + '|' + passwd)

            except Exception as exception:
                MerossLogger("Context.init").WriteErrorLog(ExceptionManager.TryToCatch(exception))
                raise Exception("Error on context creation")

    def GetToken(self) -> str:
        if len(self.token) > 0:
            return str(self.token)
        else:
            return str()

    def SetSessionActivityLastTimeCheck(self, dt: datetime) -> None:

        if type(dt) == datetime:
            self.sessionActivityLastTime = dt

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
            if self.token and self.authenticated is True:
                decryptedToken = self.fernet.decrypt(self.token).decode()

                return decryptedToken
            else:
                return str()

        except Exception as exception:
            MerossLogger("Context.DecryptLocalToken").WriteErrorLog(ExceptionManager.TryToCatch(exception))
            raise Exception("Error trying to decrypt token")

    def Reset(self) -> None:
        Singleton.Clean(self.token)
