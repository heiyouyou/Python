# !/usr/bin/env python
# coding=utf-8

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

# 实现HTMLParser类的几种方法
class MyHTMLParser(HTMLParser):

        # 匹配单开始标签
    def handle_starttag(self, tag, attrs):
        print('<%s> attrs:%s' % (tag,str(attrs)))
        print attrs

        # 匹配单结束标签
    def handle_endtag(self, tag):
        print('</%s>' % tag)

        # 匹配单标签
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
        # 匹配标签内的内容
    def handle_data(self, data):
        print('data: %s' % data)
        # 匹配注释
    def handle_comment(self, data):
        print('<!-- --> %s' % data)
        # 匹配转义字符，如：&nbsp;
    def handle_entityref(self, name):
        print('&%s;' % name)
        # 匹配如何：&#1234
    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><!-- comment --><p>Some <a href=\"#\" title="a tag!">html</a> tutorial...&nbsp;&#1234;<br>END</p></body></html>')
parser.feed('<<p style="color:red;">this is p tag!</p>')

# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。