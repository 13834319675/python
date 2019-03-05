import multiprocessing
import time

# 生产者
q = multiprocessing.Queue()

def producer(sequence,q):
    print("开始生产了",time.ctime())
    n = 0
    for item in sequence:
        n = n+1
        q.put(item)
        print("我第{0}生产了{1}".format(n,item))
    print("生产者生产结束 out！")

def consumer(q):
    print("我开始消费类",time.ctime())
    n = 0
    while True:
        n = n+1
        item = q.get()
        if item is None:
            break
        print("我第{0}次消费了{1}".format(n,item))
    print("消费完了！")

if __name__ == '__main__':
    cur_q = multiprocessing.Process(target=consumer,args=(q,))

    cur_q.start()

    sequence = [i*i+i for i in range(1,6)]
    producer(sequence,q)

    q.put(None)
    cur_q.join()



