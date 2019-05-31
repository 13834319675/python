"""
假设，我们用一组tuple来表示学生的名字和成绩，
L = [("Bob",75),("Adam",92),("Bart",66),("List",88)]
用sorted()对上述列表按照名字排序
"""
l = [("Bob",75),("Adam",92),("Bart",66),("List",88)]

sorted1  = sorted(l,key=lambda x:x[1])
print(sorted1)

def By_name(n):
    t = sorted(n[0],key=str.lower)
    return t

l2 = sorted(l,key=By_name)
print(l2)

def by_score(t):
    t = sorted(range(t[1]),key=abs)
    return t

L2 = sorted(l,key=by_score)
print(L2)

l3 = sorted(l,key=lambda x:x[1],reverse=True)
print(l3)