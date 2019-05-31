"""
编写一个程序，接受用户输入的内容，并且保存为新的文件

如果用户单独输入 :w

表示文件保存退出
"""

file_name = input("请用户输入文件名:")

def file_write(file_name):
    f = open(file_name,"w")
    print("输入内容,单独输入:w,保存退出")

    while True:
        user_write = input("输入:")
        if user_write != ":w":
            f.write("%s\n"%user_write)
            print(user_write)
        else:
            break
    f.close()

file_write(file_name)