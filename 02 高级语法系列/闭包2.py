def count2():
    def f(j):
        print('in f( ): id(j) = ', id(j), ' | j = ', j)
        # 函数g用来存放每次循环函数f传入的i的值 等待调用的执行
        def g():
            print('in g( ): id(j) = ', id(j), ' | j = ', j)
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        print('in count2( ): id(i) = ', id(i), ' | i = ', i)
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

F1,F2,F3 = count2()
print(F1)
print(F1())
print(F2)
print(F2())
print(F3)
print(F3())