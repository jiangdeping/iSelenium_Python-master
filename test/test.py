import configparser
import os

config = configparser.ConfigParser()
config=config.read(os.path.join(os.path.abspath(''), 'iselenium.ini'))
print(os.path.abspath('..'))
print(os.path.join(os.path.abspath('..')))
print(config)