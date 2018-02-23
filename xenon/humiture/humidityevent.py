#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  humidityevent.py

import uuid
from ..events.event import Event

HUMIDITY_CHANGED_EVENT_ID = uuid.uuid4()


class HumidityEvent(Event):
    def __init__(self, humidity):
        Event.__init__(self, HUMIDITY_CHANGED_EVENT_ID)
        self.__humidity = humidity

    def get_humidity(self):
        return self.__humidity
