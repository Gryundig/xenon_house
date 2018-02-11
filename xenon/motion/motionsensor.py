#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  motionsensor.py

import logging
from .. import config
from ..sensor import Sensor

logger = logging.getLogger(__name__)


class MotionSensor(Sensor):
    def __init__(self, callback):
        Sensor.__init__(self, config.MOTION_SENSOR_PIN)
        self.__callback = callback

    def begin(self):
        self.__callback(True)
