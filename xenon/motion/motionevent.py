#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  motionevent.py

import uuid
from ..events.event import Event

MOTION_CHANGED_EVENT_ID = uuid.uuid4()


class MotionEvent(Event):
    def __init__(self, motion):
        Event.__init__(self, MOTION_CHANGED_EVENT_ID)
        self.__motion = motion

    def get_motion(self):
        return self.__motion
