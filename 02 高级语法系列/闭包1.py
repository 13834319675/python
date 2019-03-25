#closure
def count():
    fs = []
    for i in range(1, 4):
        print('in count( ): id(i) = ',id(i), ' | i = ', i)
        def f():
             print('in f(): id(i) = ',id(i), ' | i = ', i)
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1)
print(f1())
print(f2)
print(f2())
print(f3)
print(f3())
