#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config.py
#
#               Name        Header      Name
#               3.3v        1|2         5v
#               GPIO2 SDA1  3|4         5v
#               GPIO3 SCL1  5|6         GND
#               GPIO4       7|8         GPIO14 UART.TXD     <- MOTION_SENSOR_PIN
#               GND         9|10        GPIO15 UART.RXD
#               GPIO17      11|12       GPIO18              <- DHT11_SENSOR_PIN
#               GPIO27      13|14       GND
#               GPIO22      15|16       GPIO23
#               3.3v        17|18       GPIO24
#               GPIO10 MOSI 19|20       GND
#               GPIO9 MIS0  21|22       GPIO25
#               GPIO11 SCLK 23|24       GPIO8 CE0
#               GND         25|26       GPIO7 CE1
#               SDA0        27|28       SCL0
#               GPIO5       29|30       GND
#               GPIO6       31|32       GPIO12
#               GPIO13      33|34       GND
#               GPIO19      35|36       GPIO16
#               GPIO26      37|38       GPIO20
#               GND         39|40       GPIO21

MOTION_SENSOR_PIN = 14
DHT11_SENSOR_PIN = 18
