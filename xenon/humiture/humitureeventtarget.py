#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  humitureeventtarget.py

import uuid
from ..events.eventtarget import EventTarget
from humidityevent import HumidityEvent
from temperatureevent import TemperatureEvent
from dht11sensor import DHT11Sensor

HUMITURE_EVENT_TARGET_ID = uuid.uuid4()


class HumitureEventTarget(EventTarget):
    def __init__(self):
        EventTarget.__init__(self, HUMITURE_EVENT_TARGET_ID)
        self.__dht11_sensor = DHT11Sensor(self.__event_callback)
        self.__humidity = 0
        self.__temperature = 0

    def begin(self):
        self.__dht11_sensor.begin()

    def loop(self):
        self.__dht11_sensor.loop()

    def end(self):
        self.__dht11_sensor.end()

    def __event_callback(self, humidity, temperature):
        if self.__humidity != humidity:
            self.__humidity = humidity
            self._dispatch_event(HumidityEvent(humidity))
        if self.__temperature != temperature:
            self.__temperature = temperature
            self._dispatch_event(TemperatureEvent(temperature))
