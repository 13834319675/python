"""
用logging的四大组件来实现日志的功能
- 打应出函数执行的时间，日志的等级，日志的消息
- 用装饰器
- 不同的日志，要记录不同等级的日志消息
"""
import logging
# 设置名字和级别
logger = logging.getLogger("MyLooger")
logger.setLevel(logging.DEBUG)
# 设置两个handler处理器
# 设置debug_log的handler的文件名
debug_handler = logging.FileHandler("1024Debug")
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

error_handler = logging.FileHandler("1024Error")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
# 添加
logger.addHandler(debug_handler)
logger.addHandler(debug_handler)

# 设置装饰器
def log(func):
    def wrapper(*args,**kwargs):
        logger.debug("this is debug info")
        logger.error("this is error info")
        return func(*args,**kwargs)
    return wrapper


def loghight(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            logger.debug(text)
            logger.error(text)
            return func(*args,**kwargs)
        return wrapper
    return decorator


@log
def text():
    print("text done")

@loghight("this is notebook")
def note():
    print("notebook")

@loghight("this is main done")
def main():
    print("main done")

text()
note()
main()


