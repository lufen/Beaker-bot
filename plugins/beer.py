#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

import requests

from baseclass import Plugin
import urllib

class Beer(Plugin):
    def __init__(self, skype):
        super(Beer, self).__init__(skype)
        self.command = "beer"

    def message_received(self, args, status, msg):
        city = " ".join(args).title().decode('utf-8')
        print urllib.quote(city.encode('utf-8'))
        r = requests.get(
            'http://beermapping.com/webservice/loccity/7829347ccd56f03274b428b2fca37c77/' + urllib.quote(city.encode('utf-8')))
        root = ET.fromstring((r.text.encode('utf-8')))
        locs = root.iter('location')
        num = 0
        for loc in locs:
            if loc[6].text != None:
                out = "Found {0}  at {1}, {2} which is a {3}".format(loc[1].text.encode('utf-8'), loc[6].text.encode('utf-8'), loc[7].text.encode('utf-8'), loc[2].text.encode('utf-8'))
                msg.Chat.SendMessage(out)
                num += 1
                if num > 3:
                    break
            else:
                msg.Chat.SendMessage("Nothing found")

    def help(self, msg):
        msg.Chat.SendMessage(
            "Usage: @beer place\nWill tell you about great places to find beer in the US")
