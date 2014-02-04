__author__ = 'george'
from abc import ABCMeta, abstractmethod

class Plugin(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def message_received(self, msg, status):
        pass

    
    def help(self):
        pass

