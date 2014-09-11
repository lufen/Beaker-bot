from baseclass import Plugin

class NotGonnaHappen(Plugin):
    def __init__(self, skype):
        super(NotGonnaHappen, self).__init__(skype)
        self.command = "notgonnahappen"
        

    def message_received(self, args, status, msg):
       
        msg.Chat.SendMessage("http://stream1.gifsoup.com/view/164117/not-gonna-happen-o.gif")


