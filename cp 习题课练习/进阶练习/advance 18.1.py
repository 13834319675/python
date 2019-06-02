"""
编写一个程序，当用户输入文件名和行数的时候，将该文件的前N行内容打印到屏幕上

input 去接收一个文件名
input 去接收一个行数
"""
input_file = input("请输入要打开的文件夹:")
input_line = input("请输入要打印的前N行的行数:")

def line_file(input_file,input_line):

    f1 = open(input_file)

    for i in range(int(input_line)):
        print(f1.readline())

    f1.close()

line_file(input_file,input_line)