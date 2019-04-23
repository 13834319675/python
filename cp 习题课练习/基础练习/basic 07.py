# append 和extend
a = [1,2,3,4,5]
a.append([6,7,8])
print(a)
a.extend([9,10])
print(a)
a.insert(3,22)
print(a)

member = ["图灵","的","周老师","是最帅的"]
member.insert(1,99)
member.insert(3,999)
member.insert(5,9999)
member.append(55)
print(member)

ls = [1, [1, 2, ['老王']], 3, 5, 8, 13, 18]
ls[1][2][0] ="陈鹏"
print(ls)

# 列表生成式

l1  = [(x,y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print(l1)

l2 = []
for x in range(10):
    for y in range(10):
        if x%2 == 0 and y%2!=0:
            l2.append([x,y])
print(l2)