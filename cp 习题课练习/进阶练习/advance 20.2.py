"""
对上述题目加一些需求，模糊匹配，判断我们的target
是否包含在某一个文件中
in 去判断target这个字符串是否在文件的名字中
"""
import os
start_dtr = input("请输入目录:")
targer = input("请输入文件名:")

def search_file(start_dir,targer):
    os.chdir(start_dir)

    for each_file  in  os.listdir(os.curdir):
        if targer in each_file:
            print(os.getcwd()+os.sep+each_file)
        # 如果为文件夹
        if os.path.isdir(each_file):
            search_file(each_file,targer)
            os.chdir(os.pardir)

search_file(start_dtr,targer)