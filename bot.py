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
        self.name = "Default name"
        self.tag = "@"
        self.skype = Skype4Py.Skype(Events=self, Transport="dbus")

        self.plugin_classlist = []
        self.enabled_plugins = []

        self.load_settings()
        self.load_plugins()
        print("loaded plugins\n Active plugins: {}".format(self.plugin_classlist))
        if not self.skype.Client.IsRunning:
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

                if command.lower() == "help":
                    for c in self.plugin_classlist:
                        if c.tag == command:
                            c.help(msg, status)
                            break
                    else:
                        for c in self.plugin_classlist:
                            c.help(msg,status)


                #TODO: Needs rewrite
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

    def load_plugins(self):
        # print("loading plugins")
        sys.path.append("plugins")
        from baseclass import Plugin
        for root, dirs, files in os.walk("plugins"):
            candidates = [fname for fname in files if fname.endswith(".py") and not fname.startswith(("__"))]
            for c in candidates:
                if c == "baseclass.py": #hacky way to eliminate the plugin base class
                    continue
                modname = os.path.splitext(c)[0]
                module = __import__(modname)
                for cls in dir(module):
                    tmp = getattr(module, cls)
                    try:
                        if issubclass(tmp, Plugin):
                            instance = tmp(self.skype)
                            self.plugin_classlist.append(instance)
                    except:
                        pass #This is not the class you are looking for

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
        self.skype.ChangeUserStatus(Skype4Py.cusAway)

if __name__ == "__main__":
    bot = SkypeBot()
    while True:
        pass        
       

