"""编写一个程序，比较用户输入的文件是否相同，如果不同，显示出所有不同处的行号

- f.readline()
- open()
- differ """

file1 = input("请输入第一个文件:")
file2 = input("请输入第二个文件:")
differ = []
count = 1
def file_compare(file1,file2):
    f1 = open(file1,"w")
    f2 = open(file2,"w")
    global count
    global differ
    for f1_readline in f1:
        f2_readline = f2.readline()
        if f1_readline != f2_readline:
            differ.append(count)
        count+=1

    f1.close()
    f2.close()
    return differ

dif = file_compare(file1,file2)

if len(dif) == 0:
    print("两个文件内容完全相同")
else:
    print("两个文件有%s处不同"%len(dif))
    for each in dif:
        print("%s处不一样"%dif)

