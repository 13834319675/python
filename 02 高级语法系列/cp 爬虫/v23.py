"""
python中的正则表达式是re
使用的大致步骤
1.comple函数将正则表达式的字符串变为一个pattern对象
2.通过pattern对象的一些方法对文本进行匹配,匹配结果是一个match对象
3.用match对象的方法,对结果进行操纵
"""

import re
# \d表示以数字
# 后面＋号表示这个数字可以出现一次或者多次
s = r"\d+" # r表示后面是原生字符串,不需要转义
# 返回pattern对象
pattern = re.compile(s)
# 返回一个match对象
# 默认找一个匹配就返回
m = pattern.match("one12two2three3")
print(type(m))
# 默认匹配从头开始,返回结果是NOne
print(m)

# 返回一个match对象
# 从给定的区间开始查找
m = pattern.match("one12two2three3",3,10)
print(m)
print(m.start())
print(m.span())
print(m.group())
print(m.end())