"""
利用map()函数，把用户输入的不规范的英文，变成首字母大写，其他小写的规范的名字：
比如说["ADMAm","LISA","JACk"] ["Admam","Lisa","Jack"]
"""
import string
def standard(s):
     l = s.lower()# 全部小写
     l = l.capitalize()#首字母大写
     print(l)
     return l

list(map(standard,["ADMAm","LISA","JACk","Admam","Lisa","Jack"]))


l = ["ADMAm","LISA","JACk","Admam","Lisa","Jack"]

l1 = map(lambda x : x.lower().capitalize(),l)
print(list(l1))