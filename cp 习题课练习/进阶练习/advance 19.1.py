"""
编写一个程序，统计当前目录下每个文件类型的文件数
思路：
打开当前的文件夹
获取到当前文件夹下面所有的文件
处理我们当前的文件夹下面可能有文件夹的情况 （也要答应出来）
做出统计
"""
import os
all_files = os.listdir()#获取当前文件夹下所有文件
print(all_files)
type_dict = dict()

for each_file in all_files: # 遍历打印所有文件
    # 判断是否为文件夹
    if os.path.isdir(each_file):
        type_dict.setdefault("文件夹",0)
        type_dict["文件夹"]+=1
    else:
        ext = os.path.splitext(each_file)[1]# 获取文件的后缀
        type_dict.setdefault(ext,0)
        type_dict[ext] += 1

for each_type in type_dict:# for循环字典打印字典的键
    print(each_type)
    print("这个文件夹下面有类型{}的文件{}个".format(each_type,type_dict[each_type]))

