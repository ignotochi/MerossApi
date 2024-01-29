from meross_iot.model.exception import CommandTimeoutError


class ExceptionManager:

    @staticmethod
    def timeOutExceptionOrRaise(exception: Exception, msg: str) -> None:
        if isinstance(exception, CommandTimeoutError):
            raise Exception("Error: expired session")
        else:
            raise Exception(msg)

    @staticmethod
    def catch(exception: Exception) -> str:
        if isinstance(exception, Exception) and hasattr(exception, 'args'):

            if len(exception.args) == 1:
                return exception.args[0]
            else:
                return str(exception)
        else:
            return f"Unable to read exception: {exception}"
