"""
# 正则表达式match的示例
"""
import re
# 以下正则分了两个组,用小括号为单位
s = r'([a-z]+) ([A-Z]+)'
pattern = re.compile(s,re.I) # re.I表示忽略大小写
m = pattern.match("Hello world wide web")

# goup[0]表示的事返回整个字符串的
s = m.group(0)
print(s)

s = m.span(0) # 返回匹配成功的整个字符串的整个跨度
print(s)

s = m.group(1) # 返回第一个分组的匹配成功的字符串
print(s)

s = m.span(1) # 返回一个匹配成功的字符串的跨度
print(s)

s = m.group()
print(s)
