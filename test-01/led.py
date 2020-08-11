#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

makerobo_pins = (11,12)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(makerobo_pins,GPIO.OUT)

GPIO.output(makerobo_pins,GPIO.HIGH)
time.sleep(5)
GPIO.output(makerobo_pins,GPIO.LOW)
