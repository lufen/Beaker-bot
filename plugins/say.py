__author__ = 'george'
from baseclass import Plugin


class Say(Plugin):
    def __init__(self, skype):
        super(Say, self).__init__(skype, "say")
        self.command = "say"

    def message_received(self, args, status, msg):
        msg.Chat.SendMessage(" ".join(args))
3