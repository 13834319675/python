import multiprocessing
import time
q = multiprocessing.Queue()

def producer(sequence, _q):
    print ("Into procuder:", time.ctime())
    for item in sequence:
        q.put(item)
        print ("put", item, "into q")
    print ("Out of procuder:", time.ctime())

def consumer(q):
    print("Into consumer:", time.ctime())
    while True:
        item = q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    print ("Out of consumer:", time.ctime()) ## 此句执行完成，再转入主进程
if __name__ == '__main__':
    cur_q = multiprocessing.Process(target=consumer,args=(q,))
    cur_q.start()

    sequence = [i for i in range(5)]
    producer(sequence,q)

    q.put(None)
    cur_q.join()




