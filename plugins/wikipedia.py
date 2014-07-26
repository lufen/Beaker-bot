__author__ = 'george'
import httplib
from baseclass import Plugin
from apscheduler.scheduler import Scheduler




class Wikipedia(Plugin):
    def __init__(self, skype):
        super(Wikipedia, self).__init__(skype)
        self.daily_channels = ["#stigrk85/$jvlomax;b43a0c90a2592b9b"]
        self.sched = Scheduler()
        self.sched.start()
        self.plugin_name = "wikipedia"
        self.sched.add_cron_job(self.dailyWikipedia, hour=18, minute=0, day_of_week="mon-sun")

    def message_received(self, msg, status):
        text = msg.Body
        if text[0] == "@":
            text = text[1:]
            try:
                command = text.split(" ")[0]
            except:
                print("exception in wikipedia")
                command = text
            if command.lower() == "wikipedia random":
                url = self.fetch_randwiki()
                msg.Chat.SendMessage(url)


    def fetch_randWiki(self):
        r = requests.get("http://en.wikipedia.org/wiki/Special:Random")
        return r.url

    def dailyWikipedia(self):
        for channel in self.daily_channels:
            chat = self.skype.Chat(channel)
            chat.SendMessage("Dagens random wikipedia: " + self.fetch_randWiki())
