#定义一个字典类：DictClass，完成如下功能
#删除某个key del_dict(key)
#判断某个键是否在字典里，如果在返回键对应的值，不在则返回‘not found' get_dict()
#返回键组成的列表 返回类型：list get_key()
#合并字典，并且返回合并后字典的values组成的列表，返回类型list update_dict()#

class DictClass():
    def __init__(self,dict1):
        self.dict1 = dict1

    def del_key(self,key):
        if key in self.dict1.keys():
            self.dict1.pop(key)
            return "删除成功"
        else:
            return "不存在"
    def get_dict(self):
        return self.dict1

    def get_key(self,key):
        if key in self.dict1.keys():
            print("这个键存在字典中")
            return self.dict1.keys(key)
        else:
            print("这个键不存在")

    def updata_dict(self,dict2):
        self.dict1 = dict(self.dict1,**dict2)
        return self.dict1.values()


d = DictClass({"张三":123,"李四":456})

print(d.get_dict())
print(d.get_key("王五"))
print(d.updata_dict({"王五":789}))
print(d.get_dict())
print(d.del_key("张三"))