__author__ = 'george'
from baseclass import Plugin
from apscheduler.scheduler import Scheduler
import wikipedia as wiki
import requests
import urllib

class Wikipedia(Plugin):
    def __init__(self, skype):
        super(Wikipedia, self).__init__(skype)
        self.daily_channels = ["#stigrk85/$jvlomax;b43a0c90a2592b9b"]
        self.sched = Scheduler()
        self.sched.start()
        self.command = "wikipedia"
        self.sched.add_cron_job(self.dailyWikipedia, hour=18, minute=0, day_of_week="mon-sun")

    def message_received(self, args, status, msg):
        if (len(args) == 1 and args[0] == "random") or not args:
            url = self.fetch_randWiki()
            msg.Chat.SendMessage(url)
        else:
            try:
                page = wiki.wikipedia.page(" ".join(args))
                if page.url:
                    msg.Chat.SendMessage(urllib.unquote(page.url))
                else:
                    msg.Chat.SendMessage("Could not find any results for {}".format(" ".join(args)))
            except wiki.exceptions.DisambiguationError:
                msg.Chat.SendMessage("Your search is disambiguous")
            except wiki.exceptions.PageError:
                 msg.Chat.SendMessage("Could not find any results for {}".format(" ".join(args)))

    def fetch_randWiki(self):
        r = requests.get("http://en.wikipedia.org/wiki/Special:Random")
        return r.url

    def dailyWikipedia(self):
        for channel in self.daily_channels:
            chat = self.skype.Chat(channel)
            chat.SendMessage("Dagens random wikipedia: " + self.fetch_randWiki())
