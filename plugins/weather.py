#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests, json
from baseclass import Plugin


class Weather(Plugin):
    def __init__(self, skype):
        super(Weather, self).__init__(skype)
        self.command = "weather"

    def message_received(self, args, status, msg):
        if len(args) < 1:
            city = 'Tromsø'.decode('utf-8')
        else:
            city = " ".join(args).title().decode('utf-8')
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric')

        data = json.loads(r.text)
        try:
            weather = "Input: "+ city + ", searched for: "+str(data['name']) + ': ' + str(data['main']['temp']) + '°C '.decode('utf-8') + data['weather'][0]['main']
            msg.Chat.SendMessage(weather)
        except:
            msg.Chat.SendMessage("City was not found!")
