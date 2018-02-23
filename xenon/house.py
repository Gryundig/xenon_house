#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from eventshandler import EventsHandler
from monitor import Monitor
from ifttt import IFTTT
from clock.clockeventtarget import ClockEventTarget
from clock.minuteevent import MINUTE_CHANGED_EVENT_ID
from clock.secondevent import SECOND_CHANGED_EVENT_ID
from humiture.humitureeventtarget import HumitureEventTarget
from humiture.humidityevent import HUMIDITY_CHANGED_EVENT_ID
from humiture.temperatureevent import TEMPERATURE_CHANGED_EVENT_ID
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
        events_handler = EventsHandler()
        events_handler.register_event_target(ClockEventTarget())
        events_handler.register_event_target(HumitureEventTarget())
        events_handler.register_event_target(MotionEventTarget())

    @staticmethod
    def __subscribe_to_events():
        monitor = Monitor()
        events_handler = EventsHandler()
        events_handler.add_event_listener(SECOND_CHANGED_EVENT_ID, monitor)
        events_handler.add_event_listener(MOTION_CHANGED_EVENT_ID, monitor)
        events_handler.add_event_listener(HUMIDITY_CHANGED_EVENT_ID, monitor)
        events_handler.add_event_listener(TEMPERATURE_CHANGED_EVENT_ID, monitor)
        ifttt = IFTTT()
        events_handler.add_event_listener(MINUTE_CHANGED_EVENT_ID, ifttt)

    @staticmethod
    def __begin():
        EventsHandler().begin()

    @staticmethod
    def loop():
        EventsHandler().loop()

    @staticmethod
    def end():
        EventsHandler().end()
