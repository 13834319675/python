import asyncio
import threading

# 使用协程
@asyncio.coroutine
def hello():
    print("hello word (%s)"%threading.currentThread())
    print("start,,,(%s)"%threading.currentThread())
    yield from asyncio.sleep(5)
    print("Done,,,(%s)"%threading.currentThread())
    print("hello again! (%s)"%threading.currentThread())

# 启动消息队列
loop = asyncio.get_event_loop()
# 定义任务
tasks = [hello(),hello()]
# asyncio 使用wait等待任务tasks队列执行完毕
loop.run_until_complete(asyncio.wait(tasks))
loop.close()