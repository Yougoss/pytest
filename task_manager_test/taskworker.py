#coding:utf-8

# from multiprocessing.managers import BaseManager
# import time, Queue
#
# class QueueManager(BaseManager):
#     pass
#
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')
#
# manager = QueueManager(address=('127.0.0.1',5000), authkey='123')
#
# manager.connect()
#
# task = manager.get_task_queue()
# result = manager.get_result_queue()
#
# for i in range(10):
#     try:
#         r = task.get(timeout=1)
#         print 'result is %d' % r
#         result.put(r*r)
#         print 'Put %d'%(r*r)
#         time.sleep(1)
#     except Queue.Empty:
#         print 'task queue is Empty'
#
# print 'worker over'

#-------------------------------------------------------------------------------------------------------------------#


from multiprocessing.managers import BaseManager
import time, Queue

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

manager = QueueManager(address=('127.0.0.1',5000),authkey='xly')

manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()
try:
    for i in range(12):
        res = task.get(timeout=1)
        print 'result receive %s' % res
        s = '{0} from taskworker'.format(res*res)
        result.put(s)
        print 'task put {0}*{0}={1}'.format(res,res*res)

    print 'taskworker over'
except Exception, e:
    print e
    print 'Queue is empty'