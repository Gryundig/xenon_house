#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  monitor.py

import logging
from events.ieventlistener import IEventListener
from clock.secondevent import SECOND_CHANGED_EVENT_ID
from motion.motionevent import MOTION_CHANGED_EVENT_ID

logger = logging.getLogger(__name__)


class Monitor(IEventListener):
    def __init__(self):
        pass

    def handle_event(self, event):
        event_id = event.get_id()
        if event_id == MOTION_CHANGED_EVENT_ID:
            logger.info("Motion - " + str(event.get_motion()))
        elif event_id == SECOND_CHANGED_EVENT_ID:
            logger.info("Time - " + str(event.get_datetime()))
        else:
            logger.debug("Unknown event id")
