from baseclass import Plugin
from datetime import date



class IsItFriday(Plugin):
    def __init__(self, skype):
        super(IsItFriday, self).__init__(skype)
        self.command = "isitfriday"

    def message_received(self, args, status, msg):
        if date.isoweekday(date.today()) == 5:
            msg.Chat.SendMessage("Yes it is friday. We so excited")
        else:
            msg.Chat.SendMessage("No, it is not friday")
