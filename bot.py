import Skype4Py
import time
import re
import httplib
skype = Skype4Py.Skype()


class SkypeBot(object):
    def __init__(self):
        self.skype = Skype4Py.Skype(Events=self, Transport="dbus")
        if self.skype.Client.IsRunning == False:
            print "skype not running, starting skype"
            self.skype.Client.Start()
            time.sleep(60)
            print "skype is now running"
        self.skype.FriendlyName = "Skype Bot"
        self.skype.Attach()
        self.tag = "@"
        self.replacements = {"cloud": "butt", "Cloud": "Butt", "Butt":"Cloud", "butt": "cloud", "the cloud": "my butt", "The cloud": "My butt"}
    def MessageStatus(self, msg, status):
        if status == Skype4Py.cmsReceived:
            text = msg.Body
            if "butt" in text.lower() or "butt" in text.lower():
                newText = self.multiple_replace(self.replacements, text)
                msg.Chat.SendMessage(newText)
            if text.lower() == "@nsfw":
                url = self.fetch_randNSFW()
                msg.Chat.SendMessage(url)
            if "@say:" in text.lower():
                msg.chat.SendMessage(text.strip("@say:")
                   
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
        


if __name__ == "__main__":
    bot = SkypeBot()
    while True:
        
        while True:
            pass

