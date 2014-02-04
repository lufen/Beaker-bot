__author__ = 'george'
from abc import abstractmethod

class Module(object):
    def __init__(self):
        pass

    @abstractmethod
    def message_received(self, msg, status):
        pass

