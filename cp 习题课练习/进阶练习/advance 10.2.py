#定义一个列表的操作类 ListInfo
#包#括的方法#

#列表元素添加: add_key()
#列表元素取值: get_key()
#列表合并: update_list(list)
#删除并且返回最后一个元素: del_key()

class listinfo():
    def __init__(self,list1):
        self.list1 = list1

    def add_key(self,key):
        self.list1.append(key)
        print(self.list1)
        return "添加成功"
    def get_list(self,index):
        if index>=0 and index<len(self.list1):
            return self.list1[index]
        else:
            return "超出列表范围"

    def updata_list(self,list2):
        self.list1.extend(list2)
        return self.list1
    def del_list(self):
        if len(self.list1)>=0:
            del_key = self.list1.pop()
            return del_key
        else:
            return "已经没有元素了"


ls = listinfo([1,2,3,4])
print(ls.add_key(5))
print(ls.get_list(3))

print(ls.updata_list([6,7,8]))
print(ls.del_list())
