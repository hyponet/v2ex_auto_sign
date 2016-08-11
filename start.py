#!/usr/bin/env python
# coding=utf-8
import time

from sign import sign


if __name__ == '__main__':
    SLEEPTIME = 60 * 60 * 24

    while True:
        print ("Start : %s" % time.ctime())
        sign()
        time.sleep(SLEEPTIME)
        print ("End : %s" % time.ctime())
