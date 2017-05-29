#!/usr/bin/env python
# coding:utf-8

import re
import os
import requests

session = requests.Session()
username = os.getenv('USERNAME','')
password = os.getenv('PASSWORD', '')

base_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.71 Safari/537.36 OPR/35.0.2066.23 (Edition beta)', 'Referer': 'https://v2ex.com/signin'}

session.headers = base_headers

def sign():
    resp = session.get('https://v2ex.com/signin')
    u, p = re.findall(r'class="sl" name="([0-9A-Za-z]{64})"', resp.text)
    once_code = re.search(r'value="(\d+)" name="once"', resp.text).group(1)

    resp = session.post('https://v2ex.com/signin', {u: username, p: password, 'once': once_code, 'next': '/'})
    resp = session.get('https://v2ex.com/mission/daily')

    if u'每日登录奖励已领取' in resp.text:
        print(u'already get it!')
    else:
        try:
            resp = session.get('https://v2ex.com' + re.search(r'/mission/daily/redeem\?once=\d+', resp.text).group())
            print(resp.ok)
            print(u'\nget it!')
        except:
            print(u"username or password error!")
