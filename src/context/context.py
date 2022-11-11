from cryptography.fernet import Fernet
from ..abstractions.auth import Auth


class Context:
    _fernet: Fernet
    _instance = None
    _token: str = None

    def NewContext(user: str, passwd: str):
        if Context._instance is None:
            # generate a key for encryption and decryption
            # You can use fernet to generate
            # the key or use random key generator
            # here I'm using fernet to generate key
            key = Fernet.generate_key()

            # Instance the Fernet class with the key
            Context._fernet = Fernet(key)

            _combinedCredentials = user + "|" + passwd

            Context._instance = Context()

            Context._token = Context.__Encrypt(_combinedCredentials)

            return Context._instance
        else:
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

    def Credentials() -> str:
        # decrypt the encrypted string with the
        # Fernet instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        if (Context._token):
            _decriptedCredentials = Context._fernet.decrypt(Context._token).decode()
            _splittedCredentials = str(_decriptedCredentials).split("|")
          
            _credentials = Auth()  
            _credentials.user = _splittedCredentials[0]
            _credentials.password = _splittedCredentials[1]
            
            return _credentials
        else:
            return ""
