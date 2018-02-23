#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  eventshandler.py

import logging
from clock.clockeventtarget import CLOCK_EVENT_TARGET_ID
from clock.dayevent import DAY_CHANGED_EVENT_ID
from clock.hourevent import HOUR_CHANGED_EVENT_ID
from clock.minuteevent import MINUTE_CHANGED_EVENT_ID
from clock.secondevent import SECOND_CHANGED_EVENT_ID
from humiture.humitureeventtarget import HUMITURE_EVENT_TARGET_ID
from humiture.humidityevent import HUMIDITY_CHANGED_EVENT_ID
from humiture.temperatureevent import TEMPERATURE_CHANGED_EVENT_ID
from motion.motioneventtarget import MOTION_EVENT_TARGET_ID
from motion.motionevent import MOTION_CHANGED_EVENT_ID
from utils.singleton import Singleton

logger = logging.getLogger(__name__)


class EventsHandler:
    __metaclass__ = Singleton

    def __init__(self):
        self.__event_target_map = {}

    def register_event_target(self, event_target):
        event_target_id = event_target.get_id()
        logger.info('Registration of event target: ' + str(event_target_id))
        self.__event_target_map[event_target_id] = event_target

    def add_event_listener(self, event_id, event_listener):
        event_target_id = self.__get_event_target_id_by_event_id(event_id)
        if event_target_id in self.__event_target_map:
            self.__event_target_map[event_target_id].add_event_listener(event_id, event_listener)
        else:
            raise Exception("Event target " + str(event_target_id) + " is not registered")

    @staticmethod
    def __get_event_target_id_by_event_id(event_id):
        if event_id == MOTION_CHANGED_EVENT_ID:
            return MOTION_EVENT_TARGET_ID
        elif event_id == DAY_CHANGED_EVENT_ID or\
            event_id == HOUR_CHANGED_EVENT_ID or\
            event_id == MINUTE_CHANGED_EVENT_ID or\
            event_id == SECOND_CHANGED_EVENT_ID:
            return CLOCK_EVENT_TARGET_ID
        elif event_id == HUMIDITY_CHANGED_EVENT_ID or\
            event_id == TEMPERATURE_CHANGED_EVENT_ID:
            return HUMITURE_EVENT_TARGET_ID
        else:
            raise Exception("Unknown event id to convert to event target id")

    def begin(self):
        for event_target_id in self.__event_target_map:
            self.__event_target_map[event_target_id].begin()

    def loop(self):
        for event_target_id in self.__event_target_map:
            self.__event_target_map[event_target_id].loop()
            
    def end(self):
        for event_target_id in self.__event_target_map:
            self.__event_target_map[event_target_id].end()
