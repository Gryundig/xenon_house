#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  event.py

import uuid

UNKNOWN_EVENT = uuid.uuid4()


class Event:
    def __init__(self):
        self._type = UNKNOWN_EVENT

    def get_type(self):
        return self._type

    def set_type(self, event_type):
        self._type = event_type
