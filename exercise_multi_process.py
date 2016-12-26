#coding:utf-8


# fork
#os.fork()返回两个值,0为子进程,非0为父进程

import os,time,random
def run(n):
    for _ in xrange(100000000):
        x=1^1
    print 'function run in process %s is over'%os.getpid()
    return n

def cost_time_task(i):
    print 'Run Task %s'%i
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print 'Task in process %s cost %0.2f seconds.argument i = %s'%(os.getpid(),end-start,i)

def process_unlock_print(i):
    print "It's process %s"%os.getpid(),i

def process_lock_print(l,i):
    l.acquire()
    print "It's process %s"%i,i
    l.release()

# pid = os.fork()
# if pid == 0:
#     print 'I({0}) am child of process {1}'.format(os.getpid(),os.getppid())
#     run()
# else:
#     pid2 = os.fork()
#     if pid2 == 0:
#         print 'I({0}) am child of process {1}'.format(os.getpid(),os.getppid())
#     else:
#         print 'I am father process {}'.format(os.getpid())



#multiprocessing
#创建子进程时,传入执行函数和参数就可以创建一个进程实例
#start()为启动进程
#   start和run的区别:start()开启一个新的进程,在获得cpu时间片的时候运行类中的run()方法.直接运行run方法的话依然是在主进程下执行
#join()可以等待子进程结束后再继续往下进行,常用于进程间的同步
#terminate()强行结束子进程

# from multiprocessing import Process
# p=Process(target=run,args=('hello',))
# p.start()
# p.join()
# print 'main process %s over'%os.getpid()

#使用Lock运行多进程

    #不使用锁可能造成输出混在一起
# from multiprocessing import Process
# for i in range(30):
#     p=Process(target=process_unlock_print,args=(i,))
#     p.start()
#     # p.run()

    #使用锁进行多进程
# from multiprocessing import Process,Lock
# lock=Lock()
# for i in range(30):
#     p=Process(target=process_lock_print,args=(lock,i))
#     p.start()


#使用Pool运行多进程
#Pool对象调用join会等待所有的子进程执行完毕
#调用join前必须调用close,调用close后,不能再往Pool中添加进程
#Pool默认大小是CPU核数
# from multiprocessing import Pool
# p=Pool()
# for i in range(5):
#     p.apply_async(cost_time_task,args=(i,))
# p.close()
# p.join()


#进程间传递消息
#Queue适合多生产者多消费者,Pipe适合两个进程间通信

    #Queue
    #Queue(maxsize=10)队列长度可以为有限或无限,如果maxsize<1则为无限,默认maxsize=0
    #put(val)将val添加到Queue的尾部
    #get()从Queue头部获取一个数据,并在Queue中把它删除.
    #   默认参数block为True,如果队列为空且block为True,
    #   get会调用线程暂停直至有项目可以用,
    #   如果队列为空且block为False则会引发Empty异常
    #empty()判断Queue中是否还有元素

# from multiprocessing import Process
# #多进程使用队列通讯,必须是multiprocessing中的Queue,python自带的Queue模块不能在进程中传递数据,自带的Queue模式可以用在多线程中
# from multiprocessing import Queue
# # from Queue import Queue
# def write(queue,num):
#     for i in range(num):
#         print 'try write value %s'%i
#         queue.put(i)
#         print 'write value {0} finished,queue size is {1}'.format(i,1)
#         time.sleep(random.random())
#
# def read(queue):
#     while True:
#         value=queue.get()
#         print 'read value %s'%value
#
# q=Queue()
# n=10
# pw=Process(target=write,args=(q,n))
# pr=Process(target=read,args=(q,))
# pw.start()
# pr.start()
# pw.join()
# if q.empty():
#     pr.terminate()


    #Pipe
    #默认参数duplex为True表示双向,改为False为单项
    #Pipe()返回一个通道的两端,用send()发送数据recv()接收数据,close()关闭通道
# from multiprocessing import Process,Pipe
#
# def p1_msg(pipe,msg):
#     pipe.send(msg)
#     print 'p1 send %s,receive %s'%(msg,pipe.recv())
# def p2_msg(pipe,msg):
#     pipe.send(msg)
#     print 'p2 receive %s,send %s',(pipe.recv(),msg)
# p1_conn,p2_conn=Pipe()
# for i in range(10):
#     p1=Process(target=p1_msg,args=(p1_conn,i))
#     p2=Process(target=p2_msg,args=(p2_conn,-i))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
# p1_conn.close()
# p2_conn.close()

#------------------------------------------------------------------------------------------
#练习:生产者消费者问题
# from multiprocessing import Process,Queue,Lock
# import os
#
# class Producer(Process):
#     def __init__(self,q,l,n):
#         super(Producer, self).__init__()
#         self._lock=l
#         self._queue=q
#         self._num=n
#
#     def run(self):
#         while True:
#             self._lock.acquire()
#             if not self._queue.full():
#                 n=self._num.get()+1
#                 self._num.put(n)
#                 self._queue.put('production_%s'%n)
#                 print 'production_%s by Producer %s.'%(n,os.getpid())
#                 self._lock.release()
#             else:
#                 print 'Producer %s rest for a moment.'%os.getpid()
#                 self._lock.release()
#                 time.sleep(random.random())
#
#
# class Consumer(Process):
#     def __init__(self,q,l,):
#         super(Consumer, self).__init__()
#         self._lock=l
#         self._queue=q
#
#     def run(self):
#         while True:
#             self._lock.acquire()
#             if not self._queue.empty():
#                 production=self._queue.get()
#                 print '%s has been bought by Consumer %s.'%(production,os.getpid())
#                 self._lock.release()
#             else:
#                 print 'Consumer %s can buy nothing.'%os.getpid()
#                 self._lock.release()
#                 time.sleep(random.random())
# lock=Lock()
# queue=Queue(maxsize=10)
# num_queue=Queue()
# num_queue.put(0)
#
# producer_list=[]
# consumer_list=[]
# for i in range(2):
#     producer_list.append(Producer(queue,lock,num_queue))
#     consumer_list.append(Consumer(queue,lock))
#
# for p in producer_list:
#     p.start()
# for c in consumer_list:
#     c.start()
#
# time.sleep(5)
# for p in producer_list:
#     p.terminate()
# for c in consumer_list:
#     c.terminate()




#------------------------------------------------------------------------------------------
#signal
# import signal
# import os
# import time

# break_flag=False
# def receive_signal(signum, stack):
#     global break_flag
#     print 'Received:', signum
#     break_flag=True
#
# # 注册信号处理程序
# signal.signal(signal.SIGINT, receive_signal)
# signal.signal(signal.SIGTERM, receive_signal)
#
# # 打印这个进程的PID方便使用kill传递信号
#
# print 'My PID is:', os.getpid()
#
# # 等待信号，有信号发生时则调用信号处理程序
# while True:
#     if break_flag:
#         break;
#     print 'Waiting...'
#     time.sleep(3)


#用信号终止进程
# from multiprocessing import Process
# import os
# import signal
# import time
# def loop():
#     while True:
#         i=1^1
#
# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess,self).__init__()
#     def run(self):
#         loop()
# p=MyProcess()
# p.start()
# time.sleep(3)
# os.kill(p.pid,signal.SIGTERM)
