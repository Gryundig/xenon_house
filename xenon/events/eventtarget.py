#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  eventtarget.py

import logging

logger = logging.getLogger(__name__)


class EventTarget:
    def __init__(self, event_target_id):
        self.__id = event_target_id
        self.__listener_map = {}

    def add_event_listener(self, event_id, event_listener):
        if event_id not in self.__listener_map:
            self.__listener_map[event_id] = [event_listener]
        else:
            self.__listener_map[event_id].append(event_listener)

    def _dispatch_event(self, event):
        event_id = event.get_id()
        if event_id in self.__listener_map:
            event_listeners = self.__listener_map[event_id]
            for eventListener in event_listeners:
                eventListener.handle_event(event)

    def get_id(self):
        return self.__id

    def begin(self):
        pass

    def loop(self):
        pass
