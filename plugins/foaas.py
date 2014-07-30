from baseclass import Plugin


class FOAAS(Plugin):
    def __init__(self, skype):
        super(FOAAS, self).__init__(skype)
        self.command = "foaas"

    def message_received(self, args, status, msg):
        if len(args) == 1:
            url = "http://foaas.com/{}/{}".format(args[0], msg.FromHandle)
        if len(args) == 2:
            url = "http://foaas.com/{}/{}/{}".format(args[0], args[1], msg.FromHandle)
        msg.Chat.SendMessage(url)
        return
