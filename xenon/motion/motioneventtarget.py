#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  motioneventtarget.py

import logging
import uuid
from ..events.eventtarget import EventTarget
from motionevent import MotionEvent
from motionsensor import MotionSensor

logger = logging.getLogger(__name__)

MOTION_EVENT_TARGET_ID = uuid.uuid4()


class MotionEventTarget(EventTarget):
    def __init__(self):
        EventTarget.__init__(self, MOTION_EVENT_TARGET_ID)
        self.__motion_sensor = MotionSensor(self.__event_callback)

    def begin(self):
        self.__motion_sensor.begin()

    def __event_callback(self, motion):
        self._dispatch_event(MotionEvent(motion))
