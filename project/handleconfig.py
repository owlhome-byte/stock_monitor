from configparser import ConfigParser
import os


class HandleConfig:
    def __init__(self, file='config.ini'):
        self.config_file = os.path.join(os.path.dirname(__file__), file)
        self.cf = ConfigParser()

    def get_read(self):
        try:
            self.cf.read(self.config_file)
            for section in self.cf.sections():
                yield self.cf.items(section)
        except Exception as e:
            print(e)
            raise