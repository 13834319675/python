#### 写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、
# 一个小写字母、一个大写字母

import random
import string
code = []

code.append(random.choice(string.ascii_lowercase))# 随机小写字母
code.append(random.choice(string.ascii_uppercase))# 随机大写字母
code.append(random.choice(string.digits))# 随机数字

while len(code)<6:
    code.append(random.choice(string.ascii_lowercase+string.ascii_lowercase
                              +string.ascii_letters))

print(code)

q_code = "".join(code)
print(q_code)
