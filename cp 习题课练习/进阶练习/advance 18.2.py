""""
我们在上一道题的基础上，增加一点功能，使用户可以随意的输入需要显示的行数

- 12:42
- :
- :9

用以上的形式来表示我们想要打印的起始和结束的行数"""
input_file = input(("请输入要打开的文件:"))
input_line = input("要打印的行数(格式为[1:9]):")

def print_line(input_file,input_line):
    f1 = open(input_file)
    # 分割
    begin,end = input_line.split(":")

    if begin == "":
        begin = 1
    if end == "":
        end = -1

    begin = int(begin)-1
    end = int(end)
    lines = end-begin
    for i in range(begin):
        f1.readline()
    # 消耗掉begin之前的行数
    if lines<0:
        print(f1.read())
    else:
        for j in range(int(lines)):
            print(f1.readline())
    f1.close()

print_line(input_file,input_line)

