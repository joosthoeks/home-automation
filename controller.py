#!/usr/bin/env python3


# Import Built-Ins:
import configparser
from datetime import datetime as dt
import os
import time

# Import Third-Party:

# Import Homebrew:
from actions import Actions


class Controller:

    def __init__(self):
        config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_file)
        self.actions = Actions()

    def run(self):

        while True:

            self.do_action1()
            self.do_action2()


controller = Controller()
controller.run()
