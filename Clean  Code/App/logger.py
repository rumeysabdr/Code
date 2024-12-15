from loguru import logger

class Logger:
    def __init__(self,log_level="INFO",log_file="app.log"):
        logger.remove()
        logger.add(log_file,level=log_level,rotation="1 MB")

    def log_info(self,message):
        logger.info(message)

    def log_error(self, message):
        logger.error(message)

    #def log_warning(self, message):
        #logger.warning(message)

    #def log_debug(self, message):
        #logger.debug(message)

    #def log_success(self, message):
        #logger.success(message)

    #def log_exception(self, message):
        #logger.exception(message)