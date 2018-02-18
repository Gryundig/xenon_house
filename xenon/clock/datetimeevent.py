#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  datetimeevent.py

from ..events.event import Event


class DateTimeEvent(Event):
    def __init__(self, event_id, datetime):
        Event.__init__(self, event_id)
        self.__datetime = datetime

    def get_datetime(self):
        return self.__datetime
