#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sensor.py


class Sensor:
    def __init__(self, pin):
        self.__pin = pin

    def begin(self):
        pass

    def end(self):
        pass

    def get_pin(self):
        return self.__pin
