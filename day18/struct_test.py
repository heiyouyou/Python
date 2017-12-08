# !/usr/bin/env python
# coding=utf-8

import struct
s = struct.pack('>I',10240099)
print s
# pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。

f = struct.unpack('IH','\xf0\xf0\xf0\xf0\x80\x80')
print f

# 根据>IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数。
# 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。


print struct.pack('hhl',1,2,3)

print struct.unpack('hhl','\x00\x01\x00\x02\x00\x00\x00\x03')

bb = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print struct.unpack('<ccIIIIIIHH',bb)