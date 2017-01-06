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
    for i in range(10):
        res = task.get(timeout=15)
        print 'result receive %s' % res
        s = '{0} from taskworker2'.format(res*res)
        result.put(s)
        print 'task put {0}*{0}={1}'.format(res,res*res)

    print 'taskworker over'
except Queue.Empty:
    print 'Queue is empty'