#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  event.py


class Event:
    def __init__(self, event_id):
        self.__id = event_id

    def get_id(self):
        return self.__id
