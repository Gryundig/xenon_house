#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from eventshandler import EventsHandler
from logger import Logger
from motion.motioneventtarget import MotionEventTarget
from motion.motionevent import MOTION_CHANGED_EVENT

logger = logging.getLogger(__name__)


class XenonHouse():
    def __init__(self):
        logger.info('XenonHouse initialization')
        self._register_event_targets()
        self._subscribe_to_events()
        self._begin()

    @staticmethod
    def _register_event_targets():
        logger.info('Registration of event targets') 
        EventsHandler().registerEventTarget(MotionEventTarget())

    @staticmethod
    def  _subscribe_to_events():
        EventsHandler().addEventListener(MOTION_CHANGED_EVENT, Logger())

    @staticmethod
    def _begin():
        EventsHandler().begin()

    @staticmethod
    def loop():
        EventsHandler().loop()
        logger.info('loop')
