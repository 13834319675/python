"""编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在，
如果遇到文件夹，则进入该文件夹继续搜索
input 去接受用户输入的文件名和开始搜索的路径
os.path.isdir 去判断是不是文件夹 如果是的话，
就需要进入该文件夹继续搜索，循环调用一下我们的函数来实现"""
import os
start_dir = input("请输入目录:")
targer = input("请输入要查找的文件夹:")

def search_file(start_dir,targer):
    os.chdir(start_dir) # 切换目录

    for each_file in os.listdir(os.curdir):
        if each_file == targer:
            print(os.getcwd()+os.sep+each_file)

        if os.path.isdir(each_file):
            # 如果是文件夹,递归调用函数进入
            search_file(each_file,targer)
            os.chdir(os.pardir) # 返回上级目录

search_file(start_dir,targer)