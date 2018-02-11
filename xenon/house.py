#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from eventshandler import EventsHandler
from logger import Logger
from motion.motioneventtarget import MotionEventTarget
from motion.motionevent import MOTION_CHANGED_EVENT_ID

logger = logging.getLogger(__name__)


class XenonHouse:
    def __init__(self):
        logger.info('XenonHouse initialization')
        self.__register_event_targets()
        self.__subscribe_to_events()
        self.__begin()

    @staticmethod
    def __register_event_targets():
        EventsHandler().register_event_target(MotionEventTarget())

    @staticmethod
    def __subscribe_to_events():
        EventsHandler().add_event_listener(MOTION_CHANGED_EVENT_ID, Logger())

    @staticmethod
    def __begin():
        EventsHandler().begin()

    @staticmethod
    def loop():
        EventsHandler().loop()
