from datetime import datetime
from cryptography.fernet import Fernet
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross.core.singleton.singleton import Singleton
from meross.abstractions.context.context_interface import IContext
from meross.abstractions.manager.manager_interface import IManager
from meross.manager.merossIotManager import MerossIotManager


@Singleton.New
class Context(IContext):

    def __init__(self, token: str = None, user: str = None, passwd: str = None):

        self.manager = None
        self.sessionActivityLastTimeCheck = None
        self.fernet: Fernet
        self.token: str

        self.authenticated: bool = False
        self.client: MerossHttpClient

        if self.manager is not isinstance(self.manager, MerossManager):
            try:
                # generate a key for encryption and decryption
                # You can use fernet to generate
                # the key or use random key generator
                # here I'm using fernet to generate key

                key = Fernet.generate_key()

                # Instance the Fernet class with the key
                self.fernet = Fernet(key)

                manager: IManager = MerossIotManager(user, passwd)

                self.manager = manager.manager
                self.client = manager.client

                if isinstance(self.manager, MerossManager) and isinstance(self.client, MerossHttpClient):
                    self.authenticated = len(self.client.cloud_credentials.token) > 0
                    self.setSessionActivityLastTimeCheck(datetime.now())

                    if self.authenticated:
                        self.token = self.encrypt(user + '|' + passwd)

            except Exception as exception:
                MerossLogger("Context.init").writeErrorLog(ExceptionManager.catch(exception))
                raise Exception("Error on context creation")

    def getToken(self) -> str:
        if len(self.token) > 0:
            return str(self.token)
        else:
            return str()

    def setSessionActivityLastTimeCheck(self, dt: datetime) -> None:

        if type(dt) is datetime:
            self.sessionActivityLastTimeCheck = dt

    def encrypt(self, value: str) -> str:
        # then use the Fernet class instance
        # to encrypt the string must
        # be encoded to byte string before encryption
        if len(value) > 0:
            encrypted = str(self.fernet.encrypt(value.encode()))
            return encrypted
        else:
            return str()

    def decryptLocalToken(self) -> str:
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
            MerossLogger("Context.decryptLocalToken").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception("Error trying to decrypt token")

    def reset(self) -> None:
        Singleton.clean(self.token)
