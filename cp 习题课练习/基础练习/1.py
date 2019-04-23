class listinfo():
    def __init__(self,list_val):
        self.list_val = list_val

    def add_list(self,key_name):
        self.list_val.append(key_name)
        print(self.list_val)
        return "添加成功"

list1 = listinfo([1,2,3,4])
print(list1.add_list(6))

