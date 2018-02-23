#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ifttt.py

import logging
from clock.dayevent import DAY_CHANGED_EVENT_ID
from clock.minuteevent import MINUTE_CHANGED_EVENT_ID
from events.ieventlistener import IEventListener
from utils.ifttt_maker import Ifttt

logger = logging.getLogger(__name__)


class IFTTT(IEventListener):
    def __init__(self):
        pass

    def handle_event(self, event):
        event_id = event.get_id()
        if event_id == DAY_CHANGED_EVENT_ID or event_id == MINUTE_CHANGED_EVENT_ID:
            ifttt = Ifttt("test", "haVypPSYZWnrntKjzCl_BfCRWMyxpL4Gh-6KYM0kfBA")
            ifttt.trigger()
            logger.info("ifttt")
        else:
            logger.debug("Unknown event id")
