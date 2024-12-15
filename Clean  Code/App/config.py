import toml
from logger import Logger
logger = Logger(log_level="INFO", log_file="app.log")


def load_config():
    config_path='config/config.toml'
    config = toml.load(config_path)


    return config