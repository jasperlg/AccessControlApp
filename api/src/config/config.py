import configparser

def getConfig(section: str):
    config = configparser.ConfigParser()
    config.read('config/config_file.ini')

    return config[section]
