import logging


class MerossLogger:

    def __init__(self, name):
        self.logger = None
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filename = f"./meross/logs/Meross_{name}.log"
        log_handler = logging.FileHandler(filename)
        log_handler.setLevel(logging.DEBUG)
        log_handler.setFormatter(log_format)

        self.logger.addHandler(log_handler)

    def WriteDebugLog(self, msg):
        self.logger.debug(f"{msg}")

    def WriteInfoLog(self, msg):
        self.logger.info(f"{msg}")

    def WriteErrorLog(self, msg):
        self.logger.error(f"{msg}")

    def WriteWarningLog(self, msg):
        self.logger.warning(f"{msg}")


