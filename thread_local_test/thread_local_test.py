from threading import current_thread
from thread_local_copy import local
import threading,time
data=local()
# key=local.__getattribute__(data,'_local__key')
# print key
# print current_thread().__dict__.get(key)
def thread_info(n):
    if n==1:
        info='1(main)'
    else:
        info='%s'%n
    data.name="Thread_%s"%info
    print data.__dict__,data.name
    # del data.name
    # print data.__dict__

print '----------------------------------------------'
thread_info(1)
print '----------------------------------------------'
time.sleep(1)
threads=[]
for i in range(2,10):
    t=threading.Thread(target=thread_info,args=(i,),name='Thread-%s'%i)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()


















# class Foo(object):
#     bar='spam'
# f=Foo()
# print f.__dict__,dir(f)
# f.bili='hello'
# print f.__dict__,dir(f)
# print Foo.__dict__
# print dir(Foo.__dict__)