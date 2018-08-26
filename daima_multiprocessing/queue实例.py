from multiprocessing import Process, Queue
import time,os,random


def write(q):
    for value in ['a','b','c']:
        print('the value is ', value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('get the value  ' , value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    q = Queue()
    qw = Process(target=write,args=(q,))
    qr = Process(target=read,args=(q,))
    # 启动子进程
    qw.start()
    qw.join()
    qr.start()
    qr.join()
    
