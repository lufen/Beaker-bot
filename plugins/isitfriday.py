from baseclass import Plugin
from datetime import date



class IsItFriday(Plugin):
    def __init__(self, skype):
        super(IsItFriday, self).__init__(skype)
        self.falseMessages =["The world is still safe, Russia has not declared war yet", "http://suptg.thisisnotatrueending.com/archive/29138254/images/1388285593271.jpg", "http://www.meh.ro/original/2010_03/meh.ro3771.jpg", "http://d24w6bsrhbeh9d.buttfront.net/photo/arpBmWp_700b_v1.jpg", "http://d24w6bsrhbeh9d.buttfront.net/photo/aXb2VAv_700b.jpg", "http://d24w6bsrhbeh9d.buttfront.net/photo/aLKXd6v_700b.jpg"]
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
