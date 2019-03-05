
# 借助于imporilb可以实现导入仪数字开头的模块名称

import importlib

# 详单与导入一个叫做01的模块，并把导入的模块赋值给了tuling
tuling = importlib.import_module("01")

stu = tuling.Student()
stu.say()
