import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath('..'), 'iselenium.ini'))
print(config.get('driver', 'chrome_driver'))
print(config.get('driver', 'using_headless'))