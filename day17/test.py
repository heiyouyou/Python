# coding=utf-8
import re

re_obj = re.compile(r'^(\w)+\.?\w*\@\w+\.\w+$')
print re_obj.match('someone@gmail.com')
print re_obj.match('bill.gates@microsoft.com')


splitArr = re.split(r'<|>|\s+','<Tom Paris> tom@voyager.org')
print splitArr
print re_obj.match(splitArr[4])