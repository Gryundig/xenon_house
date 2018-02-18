#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  secondevent.py

import uuid
from datetimeevent import DateTimeEvent

SECOND_CHANGED_EVENT_ID = uuid.uuid4()


class SecondEvent(DateTimeEvent):
    def __init__(self, datetime):
        DateTimeEvent.__init__(self, SECOND_CHANGED_EVENT_ID, datetime)
