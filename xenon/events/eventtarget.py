#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  eventtarget.py

import logging
import uuid

logger = logging.getLogger(__name__)

UNKNOWN_EVENT_TARGET = uuid.uuid4()


class EventTarget:
    def __init__(self):
        self._listener_map = {}

    def add_event_listener(self, event_type, event_listener):
        if event_type not in self._listener_map:
            self._listener_map[event_type] = [event_listener]
        else:
            self._listener_map[event_type].append(event_listener)

    def _dispatch_event(self, event):
        if event.get_type() in self._listener_map:
            event_listeners = self._listener_map[event.get_type()]
            for eventListener in event_listeners:
                eventListener.handle_event(event)

    def get_type(self):
        raise NotImplementedError

    def begin(self):
        pass

    def loop(self):
        pass
