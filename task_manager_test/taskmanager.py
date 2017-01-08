#coding:utf-8
# import random, time, Queue
# from multiprocessing.managers import BaseManager
#
# task_queue = Queue.Queue()
# result_queue = Queue.Queue()
#
# class QueueManager(BaseManager):
#     pass
#
#
# QueueManager.register('get_task_queue', lambda : task_queue)
# QueueManager.register('get_result_queue', lambda : result_queue)
#
# manager = QueueManager(address=('', 5000), authkey='123')
# try:
#     manager.start()
#
#     task = manager.get_task_queue()
#     result = manager.get_result_queue()
#
#     for i in range(10):
#         n = random.randint(0, 1000)
#         print ('Put task %d...' % n)
#         task.put(n)
#
#     print 'Put finished...Wait for get'
#
#
#     for i in range(10):
#         r = result.get(timeout = 1)
#         print 'Result is %s' % r
#
#     print 'task over'
# finally:
#     manager.shutdown()



#-------------------------------------------------------------------------------------------------------------------#


import random, time, Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',lambda : task_queue)
QueueManager.register('get_result_queue',lambda : result_queue)

manager = QueueManager(address=('127.0.0.1',5000),authkey='xly')

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()
for i in range(10):
    n = random.randint(0,1000)
    time.sleep(0.01)
    task.put(i)
    print 'put %s in task' % i

for i in range(10):
    n = result.get(timeout=10)
    print 'get %s from result' % n

manager.shutdown()
print 'taskmanager over'















