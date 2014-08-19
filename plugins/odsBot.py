from baseclass import Plugin
from random import randint

class NSFW(Plugin):
    def __init__(self, skype):
        super(NSFW, self).__init__(skype)

        self.command = "odsbot"
        self.sched.add_cron_job(self.dailyNSFW, hour=19, minute=0, day_of_week="mon-sun")

    def message_received(self, args, status, msg):
        text = args[0].lower()
        if "stig" in text and "work" in text and not "not" in text:
            retval = '[OdsBot]: Odds that "{}" -> {}:{}'.format(text, randint(1,10), randint(10000,1000000))
        elif "jørn" in text:
            retval = '[OdsBot]: Odds that "{}" -> {}:{}'.format(text, randint(10000,1000000), randint(1,10))
        else:
            retval = '[OdsBot]: Odds that "{}" -> {}:{}'.format(text, randint(1,10), randint(100,500))
        msg.Chat.SendMessage(retval)

    def help(self,msg):
        msg.Chat.SendMessage('Usage: @odsbot ["Statment to evaluate"] (including  quotes)')