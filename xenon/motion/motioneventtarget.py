#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  motioneventtarget.py

import logging
import uuid
from ..events.eventtarget import EventTarget
from motionsensor import MotionSensor

logger = logging.getLogger(__name__)

MOTION_EVENT_TARGET = uuid.uuid4()


class MotionEventTarget(EventTarget):
    def __init__(self):
        EventTarget.__init__(self)
        self._type = MOTION_EVENT_TARGET
        self._motion_sensor = MotionSensor()

    def get_type(self):
        return self._type

    def begin(self):
        logger.info('Begin of motion event target')

    def loop(self):
        pass
