from meross_iot.model.exception import CommandTimeoutError


class CustomException:

    @staticmethod
    def TimeOutExceptionOrRaise(exception: Exception, msg: str) -> None:
        if isinstance(exception, CommandTimeoutError):
            raise Exception("Error: expired session")
        else:
            raise Exception(msg)
