#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hourevent.py

import uuid
from datetimeevent import DateTimeEvent

HOUR_CHANGED_EVENT_ID = uuid.uuid4()


class HourEvent(DateTimeEvent):
    def __init__(self, datetime):
        DateTimeEvent.__init__(self, HOUR_CHANGED_EVENT_ID, datetime)
