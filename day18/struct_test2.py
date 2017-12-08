# !/usr/bin/env python
# -*- coding: utf-8 -*-
import struct

def bmpinfo(file):
    try:
        with open(file,'rb') as f:
            s = f.read(30)
            t = struct.unpack('<ccIIIIIIHH', s)
            if t[0] == 'B' and t[1] == 'M':
                print 'Windows of bmp: Size(%s * %s); Colornumber(%s)' % (t[6], t[7], t[9])
            elif t[0] == 'B' and t[1] == 'A':
                print 'OS of bmp: Size(%s * %s); Colornumber(%s)' % (t[6], t[7], t[9])
            else:
                print 'not bmp format'
    except IOError:
        print 'Error! Please input right filename.'
bmpinfo('test.bmp')
bmpinfo('note.txt')
bmpinfo('notew.txt')