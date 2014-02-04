import Skype4Py
import time
import re
import httplib
from apscheduler.scheduler import Scheduler
skype = Skype4Py.Skype()


class SkypeBot(object):
    def __init__(self):
        self.sched = Scheduler()
        self.sched.start()
        self.sched.add_cron_job(self.dailyNSFW, hour=18, minute=0, day_of_week="mon-sun")
        self.skype = Skype4Py.Skype(Events=self, Transport="dbus")
        if self.skype.Client.IsRunning == False:
            print "skype not running, starting skype"
            self.skype.Client.Start()
            time.sleep(60)
            print "skype is now running"
        self.skype.FriendlyName = "Skype Bot"
        self.skype.Attach()
        time.sleep(20)
        self.replacements = {"cloud": "butt", "Cloud": "Butt", "Butt":"Cloud", "butt": "cloud", "the cloud": "my butt", "The cloud": "My butt"}
        self.tag = "@"
    
    def MessageStatus(self, msg, status):
        if status == Skype4Py.cmsReceived:
            text = msg.Body
            print "recieved message: " + text
            if "cloud" in text.lower() or "butt" in text.lower():
                newText = self.multiple_replace(self.replacements, text)
                msg.Chat.SendMessage(newText)
            elif text[0] == "@":
                text = text[1:] #remove the tag from the text
                command = text.split(" ")[0] #get the command
                if command.lower() == "nsfw":
                    url = self.fetch_randNSFW()
                    msg.Chat.SendMessage(url)
                elif command.lower() == "say":
                    repeat_start = len(command) + 1
                    msg.Chat.SendMessage(text[repeat_start:])

                elif command.lower() == "help":
                    text = "Available functions \nHelp    Displays this help text\nsay    Make me say a message\nnsfw     Print a random NSFW subreddit"
                    msg.Chat.SendMessage(text)

                elif command.lower() == "shutup":
                    try:
                        down_time = int(text.split(" ")[1])
                    except:
                        msg.Chat.SendMessage("Please provide a valid integer")
                    if down_time > 3600:
                        msg.Chat.SendMessage("Please provide a time between 0 and 3600 (1 hour)")
                    else:
                        msg.Chat.SendMessage("shutting up for " + str(down_time) + " seconds")
                        time.sleep(down_time)
                elif command.lower() == "isbanishedoutyet":
                    cur_time = time.localtime()
                    if cur_time.tm_mday < 18:
                        time_left = 18-cur_time.tm_mday
                        hours_left = 23 - cur_time.tm_hour
                        msg.Chat.SendMessage("%d days and %d hours left until bansihed comes out" % (time_left, hours_left))
                    else:
                        msg.Chat.SendMessage("Banished is out\nhttp://store.steampowered.com/app/242920/")    
    def multiple_replace(self, dict, text):
        regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
        return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)
    
    def AttachmentStatus(self, status):
        if status == Skype4Py.apiAttachAvailable:
               self.skype.Attach()
    def fetch_randNSFW(self):
        conn = httplib.HTTPConnection("www.reddit.com")
        conn.request("GET", "/r/randnsfw")
        redirect = conn.getresponse().getheader("Location")
        return redirect
        
    def dailyNSFW(self):
        chat = self.skype.Chat("#stigrk85/$jvlomax;b43a0c90a2592b9b")
        chat.SendMessage("Dagens /r/randnsfw: " + self.fetch_randNSFW())

if __name__ == "__main__":
    bot = SkypeBot()
    while True:
        pass        
       

