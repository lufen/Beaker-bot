__author__ = 'george'
from baseclass import Plugin

class ShutUp(Plugin):
    def __init__(self, skype):
        super(ShutUp, self).__init__(skype, "shutup")

    def message_received(self, msg, status):
        pass
