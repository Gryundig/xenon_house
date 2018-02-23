#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dht11sensor.py

import RPi.GPIO as GPIO
from dht11 import DHT11
from .. import config
from ..sensor import Sensor


class DHT11Sensor(Sensor):
    def __init__(self, callback):
        Sensor.__init__(self, config.DHT11_SENSOR_PIN)
        self.__callback = callback
        self.__dht11 = DHT11(self.get_pin())
        GPIO.setmode(GPIO.BCM)

    def humiture_callback(self, pin):
        humidity = 0
        temperature = 0
        self.__callback(humidity, temperature)

    def loop(self):
        result = self.__dht11.read()
        if result.is_valid():
            self.__callback(result.humidity, result.temperature)

    def end(self):
        GPIO.cleanup(self.get_pin())
