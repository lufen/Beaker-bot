from baseclass import Plugin
import requests


class Codingexcuse(Plugin):
    def __init__(self, skype):
        super(IsItFriday, self).__init__(skype)
        self.url = "http://www.codingexcuses.com/"
        self.headers = {"Accept": "application/json"}
    def message_received(self, msg, status):
        text = msg.Body
        if text[0] == "@":
            text = text[1:] #remove the tag from the text
            command = text.split(" ")[0] #get the command
            if command.lower() == "codingexcuse":
                  r = requests.get(self.url, headers=self.headers)
                  msg.Chat.SendMessage(r.json["excuse"])
                
