"""
定义一个点（point）和直线（Line）类，
使用getLen方法获取两点构成直线的长度
"""
import math
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

class line():
    def __init__(self,p1,p2):
        self.x = p1.get_x()-p2.get_x()
        self.y = p2.get_y()-p2.get_y()

        self.line = math.sqrt(self.x**2+self.y**2)

    def getline(self):
        return self.line

p1 = point(1,4)
p2 = point(4,8)
li = line(p1,p2)
print(li.getline())

#