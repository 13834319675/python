"""回数：从左向右和从右向左读都是一样的数，
例如 12321，999，请利用filter()函数"""

def equal(a,b):
    return a==b

def palindrome(n):
    s = str(n)
    for i in range(len(s)-1):
        if equal(s[i],s[len(s)-i-1]):
            continue

        return False
    return True

output = filter(palindrome,range(1,1000))
print(list(output))

l = range(1000)
l1  = filter(lambda x :str(x)[0]==str(x)[len(str(x))-1],l)
