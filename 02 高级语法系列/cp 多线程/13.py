import time
import threading
import queue
# 生产者 消费者模型
queue1 = queue.Queue()

class Producer(threading.Thread):
    def run(self):
        global queue1
        count = 0
        while True:
            # qsize返回queue内容长度
            if queue1.qsize() < 1000:
                for i in range(100):
                    count = count +1
                    msg = '生成产品'+str(count)
                    # put是网queue中放入一个值
                    queue1.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue1
        while True:
            if queue1.qsize() > 100:
                for i in range(3):
                    # get是从queue中取出一个值
                    # 取出3个值
                    msg = self.name + '消费了 '+queue1.get()
                    print(msg)
            time.sleep(1)
if __name__ == '__main__':
    for i in range(500):
        queue1.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()


