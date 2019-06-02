"""
编写一个程序，计算当前文件夹下面所有文件的大小
打开当前文件夹
获取到所有的文件，和文件大小
保存我们获取到的数据，然后打印出来
"""
import os
all_files = os.listdir(os.curdir) # curdir当前目录
type_dict = dict()

for each_file in all_files:
    # 判断是否为文件
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        type_dict.setdefault(each_file,file_size)

for each in type_dict:
    print("{}的大小{}".format(each,type_dict[each]))