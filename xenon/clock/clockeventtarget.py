#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  clockeventtarget.py

import uuid
from datetime import datetime
from dayevent import DayEvent
from hourevent import HourEvent
from minuteevent import MinuteEvent
from secondevent import SecondEvent
from ..events.eventtarget import EventTarget

CLOCK_EVENT_TARGET_ID = uuid.uuid4()
DAY_ID = uuid.uuid4()
HOUR_ID = uuid.uuid4()
MINUTE_ID = uuid.uuid4()
SECOND_ID = uuid.uuid4()


class ClockEventTarget(EventTarget):
    def __init__(self):
        EventTarget.__init__(self, CLOCK_EVENT_TARGET_ID)
        self.__previous_datetime = {DAY_ID: 0, HOUR_ID: 0, MINUTE_ID: 0, SECOND_ID: 0}
        self.__event_const = {DAY_ID: DayEvent, HOUR_ID: HourEvent, MINUTE_ID: MinuteEvent, SECOND_ID: SecondEvent}

    def begin(self):
        dt = datetime.now()
        self.__previous_datetime[DAY_ID] = dt.day
        self.__previous_datetime[HOUR_ID] = dt.hour
        self.__previous_datetime[MINUTE_ID] = dt.minute
        self.__previous_datetime[SECOND_ID] = dt.second

    def loop(self):
        dt = datetime.now()
        self.__check(DAY_ID, dt.day, dt)
        self.__check(HOUR_ID, dt.hour, dt)
        self.__check(MINUTE_ID, dt.minute, dt)
        self.__check(SECOND_ID, dt.second, dt)

    def __check(self, key_value, value, dt):
        if self.__previous_datetime[key_value] != value:
            self.__previous_datetime[key_value] = value
            self._dispatch_event(self.__event_const[key_value](dt))
