# !/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from HTMLParser import HTMLParser

class PyEventParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)       
        self._count = 0
        self._events = dict()
        self._flag = None

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs.__contains__(('class', 'event-title')):
            self._count += 1
            self._events[self._count] = dict()
            self._flag = 'event-title'
        if tag == 'time':
            self._flag = 'time'
        if tag == 'span' and attrs.__contains__(('class', 'event-location')):
            self._flag = 'event-location'

    def handle_data(self, data):
        if self._flag == 'event-title':
            self._events[self._count][self._flag] = data
        if self._flag == 'time':
            self._events[self._count][self._flag] = data
        if self._flag == 'event-location':
            self._events[self._count][self._flag] = data
        self._flag = None

    def event_list(self):
        print u'近期关于Python的会议有：', self._count, u'个，具体如下：'
        for event in self._events.values():
            print "title:",event['event-title']
            print "time:",event['time'], '\t'
            print "place:",event['event-location']
            print '-------------------------------------------------------------------------'


try:
    parser = PyEventParser()
    # 获取远程页面数据
    pypage = urllib.urlopen('https://www.python.org/events/python-events/')
    pyhtml = pypage.read()
except IOError,e:
    print 'IOError:', e
else:
    parser.feed(pyhtml)
    parser.event_list()
finally:
    pypage.close()