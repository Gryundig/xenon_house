#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  motionevent.py

import uuid
from ..events.event import Event

MOTION_CHANGED_EVENT = uuid.uuid4()


class MotionEvent(Event):
    def __init__(self, motion):
        self._type = MOTION_CHANGED_EVENT
        self._motion = motion

    def getMotion(self):
        return self._motion
