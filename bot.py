from __future__ import print_function
import time
import re
import httplib
import os, sys
import Skype4Py
import ConfigParser
skype = Skype4Py.Skype()
import atexit


class SkypeBot(object):
    def __init__(self):
        self.name = "Deafult name"
        self.tag = "@"
        self.skype = Skype4Py.Skype(Events=self, Transport="dbus")

        self.plugin_classlist = []
        self.enabled_plugins = []

        self.load_settings()
        self.load_plugins()
        print("loaded plugins\n Active plugins: {}".format(self.plugin_classlist))

        if self.skype.Client.IsRunning == False:
            print("skype not running, starting skype")
            self.skype.Client.Start()
            time.sleep(30)
            print("skype is now running")
        self.skype.FriendlyName = "Skype Bot"
        self.skype._SetTimeout = 20
        self.skype.Attach()


        print("I'm ready")
        self.skype.ChangeUserStatus(Skype4Py.cusOnline)
        atexit.register(self.on_exit)
    
    def MessageStatus(self, msg, status):
        if status == Skype4Py.cmsReceived:
            for c in self.plugin_classlist:
                c.message_received(msg, status)

            text = msg.Body
            print("recieved message: " + text)
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
        # print("loading plugins")
        sys.path.append("plugins")
        for root, dirs, files in os.walk("plugins"):
            candidates = [fname for fname in files if fname.endswith(".py") and not fname.startswith(("__"))]
            for c in candidates:
                if c == "plugin.py":
                    continue
                modname = os.path.splitext(c)[0]
                module = __import__(modname)
                cls = getattr(module, modname)
                instance = cls(self.skype)
                self.plugin_classlist.append(instance)

    def load_settings(self):
        print("loading settings")
        config = ConfigParser.RawConfigParser()
        config.read("settings.conf")
        self.name = config.get("general", "name")
        self.tag = config.get("general", "tag")
        plugins = config.options("plugins")
        for plugin in plugins:
            if config.getboolean("plugins", plugin):
                self.enabled_plugins.append(plugin)

    def on_exit(self):
        print("on_exit")
        self.skype.ChangeUserStatus(Skype4Py.cusAway)

if __name__ == "__main__":
    bot = SkypeBot()
    while True:
        pass        
       

