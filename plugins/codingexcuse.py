from baseclass import Plugin
import requests


class Codingexcuse(Plugin):
    def __init__(self, skype):
        super(Codingexcuse, self).__init__(skype)
        self.url = "http://www.codingexcuses.com/"
        self.headers = {"Accept": "application/json"}
        self.command = "codingexcuse"

    def message_received(self, args, status, msg):
          r = requests.get(self.url, headers=self.headers)
          msg.Chat.SendMessage(r.json()["excuse"])
