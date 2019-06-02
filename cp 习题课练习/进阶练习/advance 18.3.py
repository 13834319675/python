"""编写一个程序，实现“全部替换”的功能

- 打开一个文件
- 把文件中 xxx这样的字符串，替换成 sss
- open 打开文件
- realine 读取文件内容
- replace 替换"""

file_name = input("请输入要打开的文件:")
rep_name = input("请输入要替换的字符:")
new_name = input("请输入替换的新的字符:")

def file_replace(file_name,rep_name,new_name):

    f = open(file_name)
    count = []

    for eachline in f:
        if rep_name in eachline:
            eachline = eachline.replace(rep_name,new_name)

        count.append(eachline)
        print(eachline)
    decide = input("是否确认替换[Y/N]")

    if decide in ["YES","Yes","Y","y"]:
        file_write = open(file_name,"w")
        file_write.write("".join(count))
        print("保存成功")
        print(count)
        file_write.close()

file_replace(file_name,rep_name,new_name)
