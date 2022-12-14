from meross_iot.model.exception import CommandTimeoutError


class ExceptionManager:

    @staticmethod
    def TimeOutExceptionOrRaise(exception: Exception, msg: str) -> None:
        if isinstance(exception, CommandTimeoutError):
            raise Exception("Error: expired session")
        else:
            raise Exception(msg)

    @staticmethod
    def TryToCatch(exception: Exception) -> str:
        if isinstance(exception, Exception) and hasattr(exception, 'args'):

            if len(exception.args) is 1:
                return exception.args[0]
            else:
                return str(exception)
        else:
            return f"Unable to read exception: {exception}"
