#coding:utf-8

#---------------------------------------------------------------------------------------------
#多线程
# import threading
#
# def do_sth():
#     print "%s start"%threading.currentThread().name
#     for i in range(5):
#         print "%s loop %s"%(threading.currentThread().name,i)
#     print "%s end"%threading.currentThread().name
# threads=[]
# for i in range(5):
#     t=threading.Thread(target=do_sth)
#     threads.append(t)
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()

#---------------------------------------------------------------------------------------------
#多线程修改同一个数据,没加锁

# import threading
#
# balance=0
#
# def change_it(n):
#     global balance
#     balance=balance+n
#     balance=balance-n
#
# def run(n):
#     for i in range(100000):
#         change_it(n)
#
# t1=threading.Thread(target=run,args=(5,))
# t2=threading.Thread(target=run,args=(12,))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print balance

#---------------------------------------------------------------------------------------------
#线程锁
#
# import threading
#
# lock=threading.Lock()
#
# balance=0
#
# def change_it(n):
#     global balance
#     balance+=n
#     balance-=n
#
# def run(n,l):
#     for i in range(100000):
#         l.acquire()
#         try:
#             change_it(n)
#         finally:
#             l.release()
#
# t1=threading.Thread(target=run,args=(5,lock))
# t2=threading.Thread(target=run,args=(8,lock))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance


#---------------------------------------------------------------------------------------------
#线程的等待和唤醒(生产者消费者)
    #守护线程   守护线程会在主线程结束后跟着结束,可以优雅的停止无限循环的子线程T-T
        #setDaemon(True)
    #condition  条件变量condition相比lock添加了wait和notify的方法.condition参数可以接收Lock或Rlock对象,不传参数时自己内部创建一个Lock
        #acquire    同lock.acquire
        #release    同lock.release
        #wait       线程释放锁并休眠直到被同一个condition的其他线程notify为止.如果当前线程调用此方法时没有获得锁,抛出异常
        #notify     唤醒相同condition一个或更多(默认参数n=1)线程,如果当前线程调用此方法时没又获得锁,抛出异常
        #notifyAll  唤醒相同condition所有线程,如果当前线程调用此方法时没又获得锁,抛出异常




import threading,Queue,time

class Producer(threading.Thread):
    def __init__(self,q,n,c):
        super(Producer,self).__init__()
        self.queue=q
        self.num=n
        self.condition=c
    def run(self):
        while True:
            self.condition.acquire()
            if not self.queue.full():
                n=self.num.get()+1
                self.num.put(n)
                production="production_%s"%n
                self.queue.put(production)
                print "%s by Producer %s.There are %s in warehouse"%(production,threading.currentThread().name,self.queue.qsize())
                time.sleep(0.1)
                self.condition.notifyAll()
                self.condition.release()
            else:
                print "%s wait for a moment"%threading.currentThread().name
                self.condition.wait()

class Consumer(threading.Thread):
    def __init__(self,q,c):
        super(Consumer,self).__init__()
        self.queue=q
        self.condition=c
    def run(self):
        while True:
            self.condition.acquire()
            if not self.queue.empty():
                production=self.queue.get()
                print "%s buy %s.There are %s in warehouse"%(threading.currentThread().name,production,self.queue.qsize())
                time.sleep(0.1)
                self.condition.notifyAll()
                self.condition.release()
            else:
                print "%s has nothing can be bought!"%threading.currentThread().name
                self.condition.wait()

queue=Queue.Queue(maxsize=10)
condition=threading.Condition()
num=Queue.Queue(maxsize=1)
num.put(0)
pro_list=[]
for i in range(3):
    p=Producer(queue,num,condition)
    c=Consumer(queue,condition)
    pro_list.append(p)
    pro_list.append(c)

for p in pro_list:
    p.setDaemon(True)
    p.start()
time.sleep(5)
#---------------------------------------------------------------------------------------------
#threadlocal
from threading import local
