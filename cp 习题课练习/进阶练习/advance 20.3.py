"""
再加一个需求，上述题目，我们需要保存我们的文件存在的地方，到我们指定的路径
file I/O 写文件
"""
import os
start_dir = input("place input start directory:")
targer = input("enter your file name:")
backup = []

def search_file(start_dir,targer):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        if targer in each_file:
            back_up = os.getcwd()+os.sep+each_file
            backup.append(back_up)

        if os.path.isdir(each_file):
            search_file(each_file,targer)
            os.chdir(os.pardir)

    return  backup
rd = search_file(start_dir,targer)
print(rd)
f = open(os.getcwd()+os.sep+"backup.text","wb")
print(os.getcwd())
f.write("\n".join(rd).encode("utf-8"))
f.close()