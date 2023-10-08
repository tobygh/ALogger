from logger import *

if __name__ == "__main__":
    config = Config()
    logger_config = Config()
    logger_config.path = 'log'
    logger_config.is_print = False
    logger_config.is_write = True
    config.logger_config = logger_config
    ConfigParser.set_args(config)

    logger = Logger.get_logger()
    logger.info("test: after config")