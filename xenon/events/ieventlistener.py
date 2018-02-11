#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ieventlistener.py

from abc import ABCMeta, abstractmethod


class IEventListener():
    __metaclass__ = ABCMeta

    @abstractmethod
    def handleEvent(self, event):
        raise NotImplementedError
