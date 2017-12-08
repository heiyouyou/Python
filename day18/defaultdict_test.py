# coding=utf-8

from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print dd['key1']
# key不存在，返回默认值
print dd['key2']

# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
