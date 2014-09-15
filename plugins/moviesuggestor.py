import re
import urllib
from baseclass import Plugin


class MovieSuggest(Plugin):
    def __init__(self, skype):
        super(MovieSuggest, self).__init__(skype)
        self.command = "suggestmovie"

    def message_received(self, args, status, msg):
        socket = urllib.urlopen("http://www.suggestmemovie.com/")
        htmlSource = socket.read()
        socket.close()
        movie = re.findall('<h1>((?:.|\\n)*?)</h1>', htmlSource)
        score = re.findall('<span style="font-size: 25px; font-weight:bold;">((?:.|\\n)*?)</span>', htmlSource)
        youtube = re.findall('<param name="movie" value="((?:.|\\n)*?)?version=3&rel=1&fs=1&iv_load_policy=3&modestbranding=1&autohide=1"></param>', htmlSource)
        message = movie[0] + " Imdb score " + score[0] + "/10 " + youtube[0][:-1]
        msg.Chat.SendMessage(message)
        return
