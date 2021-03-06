import os
import configparser
import shutil

filename = os.path.join(os.path.expanduser("~"), ".iotpy", "config.ini")
if not os.path.isfile(filename):
    dir = os.path.dirname(filename)
    if not os.path.isdir(dir):
        os.makedirs(dir)
    source = os.path.join(os.path.dirname(__file__), "config.ini")
    shutil.copy(source, filename)

Config = configparser.ConfigParser()
Config.read(filename)


def get(key, value):
    """ This function returns the value for a key from config

    Parameters
    ----------
    key : str
        The key to find
    value : str
        The value to find

    Returns
    -------
    str

    """

    return Config.get(key, value)
