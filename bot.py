from __future__ import print_function
import time
import os, sys
import Skype4Py
import ConfigParser
import atexit


class SkypeBot(object):
    def __init__(self):
        self.name = "Default name"
        self.tag = "@"
        #self.skype = Skype4Py.Skype(Events=self, Transport="dbus")
        self.skype = Skype4Py.Skype(Events=self)

        self.plugin_classlist = []
        self.enabled_plugins = []
        self.disabled_plugins = []

        self.load_settings()
        self.load_plugins()
        print("loaded plugins\n Active plugins: {}".format(self.plugin_classlist))
        if not self.skype.Client.IsRunning:
            print("skype not running, starting skype")
            self.skype.Client.Start()
            time.sleep(30)
            print("skype is now running")
        self.skype.FriendlyName = "Beaker"
        self.skype._SetTimeout = 20
        self.skype.Attach()
        print("I'm ready")
        self.skype.ChangeUserStatus(Skype4Py.cusOnline)
        atexit.register(self.on_exit)


    def MessageStatus(self, msg, status):
        if status == Skype4Py.cmsReceived and msg.Body[0] == self.tag:
            command = msg.Body.split(" ")[0][1:].lower()
            args = msg.Body.split(" ")[1:]
            for c in self.plugin_classlist:
                if c.command == command or not c.uses_command:
                    c.message_received(args, status, msg)
                    return

            #internal handling for bot spesific commands

            print("recieved message: " + msg.Body)

            if command.lower() == "help":
                for c in self.plugin_classlist:
                    if len(args) >= 1:
                        if c.command == args[0]:
                            c.help()
                            return
                else:
                    for c in self.plugin_classlist:
                        c.help(msg, status)
            elif command.lower() == "plugins":
                msg.Chat.SendMessage("Enabled plugins:")
                msg.Chat.SendMessage(print([c.command for c in self.plugin_classlist]))

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
        self.tag = str(config.get("general", "tag"))

        plugins = config.options("plugins")
        for plugin in plugins:
            if config.getboolean("plugins", plugin):
                self.enabled_plugins.append(plugin)

    def on_exit(self):
        self.skype.ChangeUserStatus(Skype4Py.cusDoNotDisturb)

if __name__ == "__main__":
    bot = SkypeBot()
    while True:
        pass        
       

