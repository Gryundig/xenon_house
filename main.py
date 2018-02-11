#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
import time
from xenon import const
from xenon.house import XenonHouse

logging.basicConfig(
    level=logging.NOTSET,
    format='%(asctime)s %(levelname)-8s %(name)-30s %(message)s')

logger = logging.getLogger(__name__)


def main(args):
    try:
        if len(args) > 0:
            raise Exception("Invalid arguments passed")
        xenon_house = XenonHouse()
        while True:
            xenon_house.loop()
            time.sleep(const.TIMEOUT)
    except KeyboardInterrupt:
        logger.info('Exit pressed (Ctrl+C)')
        return 0
    except Exception as e:
        logger.exception(e)
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
