from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print('work start',msg,os.getpid())
    time.sleep(random.random()*2)
    t__stop = time.time()
    t_time = t__stop - t_start
    print(msg,'work done',t_time)

if __name__ == '__main__':
    po = Pool(3)
    for i in range(0, 10):
        # Pool().apply_async()
        po.apply_async(worker, (i,))

    print('----start---')
    po.close()
    po.join()
    print('---end----')