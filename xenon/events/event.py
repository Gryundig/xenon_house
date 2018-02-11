#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  event.py

import uuid

UNKNOWN_EVENT = uuid.uuid4()

class Event():
    def __init__(self):
        self._type = UNKNOWN_EVENT

    def getType(self):
        return self._type

    def setType(self, type):
        self._type = type
