from baseclass import Plugin

class LMGTFY(Plugin):
    def __init__(self, skype):
        super(LMGTFY, self).__init__(skype)
        self.command = "lmgtfy"
        self.url = "http://lmgtfy.com/?q="

    def message_received(self, args, status, msg):
        url = self.url + "+".join(args)
        msg.Chat.SendMessage(url)


