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


class EventsHandler:
    __metaclass__ = Singleton

    def __init__(self):
        self._event_target_map = {}

    def register_event_target(self, event_target):
        self._event_target_map[event_target.get_type()] = event_target

    def add_event_listener(self, event_type, event_listener):
        event_target_type = UNKNOWN_EVENT_TARGET
        if event_type == MOTION_CHANGED_EVENT:
            event_target_type = MOTION_EVENT_TARGET

        if event_target_type != UNKNOWN_EVENT_TARGET:
            self._event_target_map[event_target_type].add_event_listener(event_type, event_listener)
        else:
            logger.warn('Unknown event target type')

    def begin(self):
        logger.info('Begin of event handler')
        for eventTargetType in self._event_target_map:
            self._event_target_map[eventTargetType].begin()

    def loop(self):
        for eventTargetType in self._event_target_map:
            self._event_target_map[eventTargetType].loop()
