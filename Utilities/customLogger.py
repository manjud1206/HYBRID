import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="test.log")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger