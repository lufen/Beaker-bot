import time
import re
import httplib
import os
import glob
import Skype4Py


skype = Skype4Py.Skype()


class SkypeBot(object):
    def __init__(self):

        self.skype = Skype4Py.Skype(Events=self, Transport="dbus")
        if self.skype.Client.IsRunning == False:
            print "skype not running, starting skype"
            self.skype.Client.Start()
            time.sleep(30)
            print "skype is now running"
        self.skype.FriendlyName = "Skype Bot"
        self.skype.Attach()
        self.name = "Beaker"
        self.ctb = cloudToBut.CloudToBut()
        self.nsfw = nsfw.NSFW(self.skype)
        time.sleep(20)

        self.enabled_modules = ["cloudToBut, nsfw"]
        modules = map(__import__, self.enabled_modules)

        print "I'm ready"

        self.tag = "@"
    
    def MessageStatus(self, msg, status):
        if status == Skype4Py.cmsReceived:
            for module in self.enabled_modules:

            self.ctb.message_received(msg, status)
            self.nsfw.message_received(msg, status)
            text = msg.Body
            print "recieved message: " + text
           # if "cloud" in text.lower() or "butt" in text.lower():
             #   newText = self.multiple_replace(self.replacements, text)
              #  msg.Chat.SendMessage(newText)
            if text[0] == "@":
                text = text[1:] #remove the tag from the text
                command = text.split(" ")[0] #get the command
                if command.lower() == "say":
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

    def load_plugins(self):
        os.chdir("plugins")
        plugins = glob.glob("*.py")
        modules = map(__import__, plugins)

        os.chdir("..")

if __name__ == "__main__":
    bot = SkypeBot()
    while True:
        pass        
       

