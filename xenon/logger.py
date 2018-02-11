#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  logger.py

import logging
from events.ieventlistener import IEventListener
from motion.motionevent import MOTION_CHANGED_EVENT

logger = logging.getLogger(__name__)


class Logger(IEventListener):
    def __init__(self):
        pass

    def handle_event(self, event):
        event_type = event.get_type()
        if event_type == MOTION_CHANGED_EVENT:
            logger.info("Motion - " + str(event.get_motion()))
        else:
            logger.debug("Unknown event type ")
