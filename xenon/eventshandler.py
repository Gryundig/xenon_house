#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  eventshandler.py

import logging
from events.eventtarget import UNKNOWN_EVENT_TARGET
from motion.motioneventtarget import MOTION_EVENT_TARGET
from motion.motionevent import MOTION_CHANGED_EVENT
from singleton import Singleton

logger = logging.getLogger(__name__)


class EventsHandler():
    __metaclass__ = Singleton

    def __init__(self):
        self.eventTargetMap = {}

    def registerEventTarget(self, eventTarget):
        self.eventTargetMap[eventTarget.getType()] = eventTarget

    def addEventListener(self, type, eventListener):
        eventTargetType = UNKNOWN_EVENT_TARGET
        if type == MOTION_CHANGED_EVENT:
            eventTargetType = MOTION_EVENT_TARGET

        if eventTargetType != UNKNOWN_EVENT_TARGET:
            self.eventTargetMap[eventTargetType].addEventListener(type, eventListener)
        else:
            logger.warn('Unknown event target type')

    def begin(self):
        logger.info('Begin of event handler')
        for eventTargetType in self.eventTargetMap:
            self.eventTargetMap[eventTargetType].begin()

    def loop(self):
        for eventTargetType in self.eventTargetMap:
            self.eventTargetMap[eventTargetType].loop()
