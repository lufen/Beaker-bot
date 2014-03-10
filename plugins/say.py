__author__ = 'george'
from baseclass import Plugin


class Say(Plugin):
    def __init__(self, skype):
        super(Say, self).__init__(skype, "say")
    def message_received(self, msg, status):
        text = msg.Body

        if text[0] == "@":
            text = text[1:] #remove the tag from the text
            command = text.split(" ")[0] #get the command
            if command.lower() == self.command:
                repeat_start = len(command) + 1
                msg.Chat.SendMessage(text[repeat_start:])
3