#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  eventtarget.py

import logging
import uuid

logger = logging.getLogger(__name__)

UNKNOWN_EVENT_TARGET = uuid.uuid4()


class EventTarget():
    def __init__(self):
        self._listenerMap = {}

    def addEventListener(self, type, eventListener):
        if type not in self._listenerMap:
            self._listenerMap[type] = [eventListener]
        else:
            self._listenerMap[type].append(eventListener)

    def dispatchEvent(self, event):
        if event.getType() in self._listenerMap:
            eventListeners = self._listenerMap[event.getType()]
            for eventListener in eventListeners:
                eventListener.handleEvent(event)

    def getType(self):
        pass

    def begin(self):
        logger.info('Begin of event target')

    def loop(self):
        pass
