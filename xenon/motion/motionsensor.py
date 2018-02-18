#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  motionsensor.py

import RPi.GPIO as GPIO
from .. import config
from ..sensor import Sensor


class MotionSensor(Sensor):
    def __init__(self, callback):
        Sensor.__init__(self, config.MOTION_SENSOR_PIN)
        self.__callback = callback
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.get_pin(), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def moving_callback(self, pin):
        self.__callback(GPIO.input(pin))

    def begin(self):
        GPIO.add_event_detect(
            self.get_pin(),
            GPIO.BOTH,
            callback=self.moving_callback)
