#定义一个集合的操作类
#包括的方法

#集合元素添加: add_setinfo()
#集合的交集: get_intersection()
#集合的并集: get_union()
#集合的差集: del_difference()

class SetClass():
    def __init__(self,set1):
        self.set1 = set1

    def add_setinfo(self,keyname):
        self.set1.add(keyname)
        return self.set1

    def get_intersection(self,set2):
        if isinstance(set2,set):
            return self.set1 & set2
        else:
            return "这个不是集合"

    def get_union(self,set3):
        if isinstance(set3,set):
            return self.set1 | set3
        else:
            return "这个不是集合"

    def del_difference(self,set4):
        if isinstance(set4,set):
            return self.set1 - set4
        else:
            return "这个不是集合"

s = SetClass({1,2,3,4,5,6})
print(s.add_setinfo(20))
print(s.get_intersection({5,6,7,8,9,10}))
print(s.get_union({5,6,7,8,9,10}))
print(s.del_difference({5,6,7,8,9,10}))
