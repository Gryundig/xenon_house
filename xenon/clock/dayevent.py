#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dayevent.py

import uuid
from datetimeevent import DateTimeEvent

DAY_CHANGED_EVENT_ID = uuid.uuid4()


class DayEvent(DateTimeEvent):
    def __init__(self, datetime):
        DateTimeEvent.__init__(self, DAY_CHANGED_EVENT_ID, datetime)
