"""
中文Unicode案例
"""
import re
hello = "你好,世界"
s = r'[\u4e00-\u9fa5]+'
pattern = re.compile(s)

m = pattern.findall(hello)
print(m)
