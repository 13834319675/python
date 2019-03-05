#coding:utf-8
# 包含有一生类
# 一个sayhello的函数
# 一个打印语句个学

class Student():
    def __init__(self,name="NoName",
                 age=18):
        self.name = name
        self.age = age


    def say (self):
        print("My name is {0}".format
              (self.name))
    def sayhello(self):
        print("HI 欢迎来到美丽的沁水")

print("我是模块p01，欢迎调用我")
