__author__ = 'george'
from baseclass import Plugin

class Reminder(Plugin):
    def __init__(self, skype):
        self.skype = skype
        pass

    def message_received(self, msg, status):
        pass