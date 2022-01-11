import configparser
import os

config = configparser.ConfigParser()
config=config.read(os.path.join(os.path.abspath('..'), 'iselenium.ini'))
print(config)