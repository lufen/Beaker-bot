#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import urllib

import requests

from baseclass import Plugin


class Food(Plugin):
    def __init__(self, skype):
        super(Food, self).__init__(skype)
        self.command = "food"

    def message_received(self, args, status, msg):
        r = requests.get('http://www.reciperoulette.tv/ajax_recipe.php?&_=1412254726389')
        data = r.text
        start = data.find("twitter.com")
        stop = data.find("images/twitter.png")
        food = data[start:stop].split("=")[1].split("&")[0]
        url = data[start:stop].split("url=")[1].split("\" ")[0]
        msg.Chat.SendMessage("You will have {0}".format(food))
        msg.Chat.SendMessage(url)

    def help(self, msg):
        msg.Chat.SendMessage(
            "Usage: @food\nWill tell you whats for dinner")
