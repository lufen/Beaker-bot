from baseclass import Plugin

class FOAAS(Plugin):
    def __init__(self, skype):
        super(FOAAS, self).__init__(skype)
        
    def message_received(self, msg, status):
        text = msg.Body
        if text[0] == "@":
            text = text[1:]
            try:
                command = text.split(" ")[0]
            except:
                print("exception in FOAAS")
                command = text
            if command.lower() == "foaas":
                split = text.split(" ")
                if len(split) == 2:
                    url = "http://foaas.com/{}/{}".format(split[1], msg.FromHandle)
                if len(split) == 3:
                    url = "http://foaas.com/{}/{}/{}".format(split[1], split[2], msg.FromHandle)
                msg.Chat.SendMessage(url)
                return
