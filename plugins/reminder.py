__author__ = 'george'
from baseclass import Plugin

class Reminder(Plugin):
    def __init__(self, skype):
        super(Reminder, self).__init__(skype, "remind me")

        pass

    def message_received(self, msg, status):
        pass