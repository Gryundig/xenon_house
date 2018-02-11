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
        self._pin = config.MOTION_SENSOR_PIN
        self._callback = callback

    def begin(self):
        self._callback(True)
