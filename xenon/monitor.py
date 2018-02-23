#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  monitor.py

import logging
from events.ieventlistener import IEventListener
from clock.secondevent import SECOND_CHANGED_EVENT_ID
from humiture.humidityevent import HUMIDITY_CHANGED_EVENT_ID
from humiture.temperatureevent import TEMPERATURE_CHANGED_EVENT_ID
from motion.motionevent import MOTION_CHANGED_EVENT_ID

logger = logging.getLogger(__name__)


class Monitor(IEventListener):
    def __init__(self):
        pass

    def handle_event(self, event):
        event_id = event.get_id()
        if event_id == SECOND_CHANGED_EVENT_ID:
            logger.info("Time: " + event.get_datetime().strftime("%H:%M:%S"))
        elif event_id == HUMIDITY_CHANGED_EVENT_ID:
            logger.info("Humidity: %d%%" % event.get_humidity())
        elif event_id == TEMPERATURE_CHANGED_EVENT_ID:
            logger.info("Temperature: %d°C" % event.get_temperature())
        elif event_id == MOTION_CHANGED_EVENT_ID:
            logger.info("Motion: " + str(event.get_motion()))
        else:
            logger.debug("Unknown event id")
