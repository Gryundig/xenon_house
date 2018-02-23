#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  temperatureevent.py

import uuid
from ..events.event import Event

TEMPERATURE_CHANGED_EVENT_ID = uuid.uuid4()


class TemperatureEvent(Event):
    def __init__(self, temperature):
        Event.__init__(self, TEMPERATURE_CHANGED_EVENT_ID)
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature
