'''
V2
处理js加密代码
'''

'''
通过查找，能找到js代码中操作代码

1. 这个是计算salt的公式 r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
2. sign: n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
md5一共需要四个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，第二个是。。。。。
第二个参数就是输入的要查找的单词'''