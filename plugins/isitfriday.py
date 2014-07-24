from baseclass import Plugin
from datetime import date



class IsItFriday(Plugin):
    def __init__(self, skype):
        super(IsItFriday, self).__init__(skype)
        
    def message_received(self, msg, status):
        text = msg.Body
        if text[0] == "@":
            text = text[1:] #remove the tag from the text
            command = text.split(" ")[0] #get the command
            if command.lower() == "isitfriday":
                if date.isoweekday(date.today()) == 5:
                    msg.Chat.SendMessage("Yes it is friday. We so excited")
                else:
                    msg.Chat.SendMessage("No, it is not friday")
