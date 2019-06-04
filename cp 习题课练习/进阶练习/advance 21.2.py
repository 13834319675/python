# 装饰器使用装饰器，打印函数执行的时间

import logging

LOG_FORMAT = "%(asctime)s-%(levelname)s-%(message)s"
logging.basicConfig(format=LOG_FORMAT)
# 装饰器的简单写法
def log(func):
    def wrapper(*arg,**kw):
        logging.error("this is info message")
        return func(*arg,**kw)
    return wrapper()


if __name__ == '__main__':
    @log
    def text():
        print("text done")