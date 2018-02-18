#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minuteevent.py

import uuid
from datetimeevent import DateTimeEvent

MINUTE_CHANGED_EVENT_ID = uuid.uuid4()


class MinuteEvent(DateTimeEvent):
    def __init__(self, datetime):
        DateTimeEvent.__init__(self, MINUTE_CHANGED_EVENT_ID, datetime)
