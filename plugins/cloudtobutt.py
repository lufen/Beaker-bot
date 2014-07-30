import re
from baseclass import Plugin

class CloudToButt(Plugin):
    def __init__(self, skype):
        super(CloudToButt, self).__init__(skype)
        self.replacements = {"cloud": "butt", "Cloud": "Butt", "Butt":"Cloud", "butt": "cloud", "the cloud": "my butt", "The cloud": "My butt"}
        self.command = "cloud2butt"
        self.uses_commad = False

    def message_received(self, args, status, msg):
        text = msg.Body
        if "cloud" in text.lower() or "butt" in text.lower():
            newText = self.multiple_replace(self.replacements, text)
            msg.Chat.SendMessage(newText)

    def multiple_replace(self, dict, text):
        regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
        return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)