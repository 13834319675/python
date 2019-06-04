# 使用装饰器 根据不同的函数输入不同的内容

# 一般装饰器
import logging
"""def log(func):
    def warpper(*args,**kwargs):
        logging.error("this is info massage")
        return func(*args,**kwargs)
    return warpper()

@log
def text():
    print("text done")"""

LOG_FOMAt = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FOMAt)

def log(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            logging.error(text)
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log("text done")
def text():
    print("text")

@log("main done")
def main():
    print("main")

text()
main()