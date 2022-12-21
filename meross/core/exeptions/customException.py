from meross_iot.model.exception import CommandTimeoutError


class CustomException:

    @staticmethod
    def TimeOutExceptionOrRaise(exception: Exception) -> None:
        if isinstance(exception, CommandTimeoutError):
            raise Exception("Error: expired session")
        else:
            raise Exception(exception.args[0])
