#!/usr/bin/env python
# coding=utf-8
import time

from sign import sign

"""
一个可以放在后台执行的死循环，
每执行一次便会SLEEP一天，从而实现每天自动备份数据库，
但是DaoCloud的胶囊主机如果长时间不访问会挂起，因此这个并不适用
"""

if __name__ == '__main__':
    SLEEPTIME = 60 * 60 * 24

    while True:
        print ("Start : %s" % time.ctime())
        sign()
        time.sleep(SLEEPTIME)
        print ("End : %s" % time.ctime())
