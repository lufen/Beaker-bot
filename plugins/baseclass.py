from __future__ import print_function
from abc import ABCMeta, abstractmethod


class Plugin(object):
    __metaclass__ = ABCMeta

    def __init__(self, skype, command=""):
        self.skype = skype
        self.command = command


    @abstractmethod
    def message_received(self, msg, status):
        pass

    def help(self, msg, status):
        text = "{} Has not implemented a help function".format(self.__class__.__name__)
        msg.Chat.SendMessage(text)


