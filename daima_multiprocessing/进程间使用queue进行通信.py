from multiprocessing import Queue


q = Queue()
q.put('message1')
q.put('message2')
print(q.full())
q.put('message3')
print(q.full())

try:
    q.put('message4',True,2)
except:
    print('manle', q.qsize())
# 执行原理：如果添加不上，则会一直在外排队等待；
# 这里的2，表示下一次尝试的等待秒数，如果加不上就程序结束
# 把put改为put_nowait功能，则直接尝试。

try:
    q.put_nowait('message4')
except:
    print('male', q.qsize())

# 推荐方式：先判断队列是否已满再写入，先判断队列是否为空之前再读取
if not q.full():
    q.put_nowait('message4')

print('----', q.qsize())

if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())



