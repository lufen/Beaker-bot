__author__ = 'george'
from baseclass import Plugin
import time
class Banished(Plugin):
    def __init__(self, skype):
        super(Banished, self).__init__(skype)

    def message_received(self, msg, status):
        text = msg.Body
        if text[0] == "@":
            text = text[1:] #remove the tag from the text
            command = text.split(" ")[0] #get the command
            if command.lower() == "isbanishedoutyet":
                cur_time = time.localtime()
                if cur_time.tm_mday < 18:
                    time_left = 18 - cur_time.tm_mday
                    hours_left = 20 - cur_time.tm_hour
                    msg.Chat.SendMessage("%d days and %d hours left until banished comes out" % (time_left, hours_left))
                else:
                    msg.Chat.SendMessage("Banished is out\nhttp://store.steampowered.com/app/242920/")
