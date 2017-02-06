# coding:utf-8


# -------------------------------------------------------------------------------------------------------------------#
# __slots__

# class Student1(object):
#     name="student1"
#
# s1=Student1()
# s2=Student1()
# print s1.name,s2.name
#
# Student1.age=16
# print s1.age,s2.age
#
# s1.score=90
# print s1.score
#
#
# class Student2(object):
#     __slots__=("name","age")
#     name="Student2"
# s3=Student2()
# s4=Student2()
# print s3.name,s4.name
#
# Student2.age=26
# Student2.score=95
# print s3.age,s4.age
# print s3.score,s4.score
# #
# s3.weight="80kg"

# __slots__用tuple定义,类创建的实例不允许绑定不在tuple中的属性(类本身可以添加属性)
# 继承的子类中没有定义__slots__时,父类的限制对子类不起作用.
# 继承的子类中定义__slots__时,子类允许定义的属性就是自身和父类__slots__的叠加
# -------------------------------------------------------------------------------------------------------------------#
# @property

    #思考题

# class Screen(object):
#
#     @property
#     def width(self):
#         return self._width
#     @property
#     def height(self):
#         return self._height
#     @width.setter
#     def width(self,value):
#         self._width=value
#     @height.setter
#     def height(self,value):
#         self._height=value
#
#     @property
#     def resolution(self):
#         return self._width*self._height
#
# # test:
# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)
# assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# @property的getter函数名和setter装饰器 . 前面的名字和setter函数名保持一致
# @property修饰之后可以像属性一样调用函数
# 可以设置制度属性(不设置setter方法)
# -------------------------------------------------------------------------------------------------------------------#
# 多重继承
"""
                Animal
                  |
          ------------------
          |                |
        Mammal            Bird
          |                |
      -----------      ----------
      |         |      |        |
     Dog       Bat   Ostrich  Parrot

"""
# class Animal(object):
#     def inherit(self):
#         print "Inherit from Animal"
#
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
#
# class RunnableMixln(object):
#     def inherit(self):
#         print "Inherit from Runnable"
#     def move(self):
#         print "Running..."
#
# class FlyableMixln(object):
#     def inherit(self):
#         print "Inherit from Flyable"
#     def move(self):
#         print "Flying~~~"
#
# class Dog(Mammal,RunnableMixln):
#     pass
#
# class Bat(Mammal,FlyableMixln):
#     pass
#
# class Ostrich(Bird,RunnableMixln):
#     pass
#
# class Parrot(Bird,FlyableMixln):
#     pass
#
# d=Dog()
# b=Bat()
# o=Ostrich()
# p=Parrot()
#
# d.move(),b.move(),o.move(),p.move()
# d.inherit(),b.inherit(),o.inherit(),p.inherit()

# 设计类的继承关系事,通常主线都是单一继承下来的,通过多重继承来添加额外的功能,这种设计称之为Mixln
# 多重继承时,有重复的属性时,按继承顺序从左到右,优先深度(去第一个继承类的所有父类寻找完之后再找第二个类)
# -------------------------------------------------------------------------------------------------------------------#
# 定制类

#   __str__(),__repr__()
#   __str__()用来设置打印返回的字符串
#   __repr__()返回程序开发者看到的字符串(命令行直接输入实例显示的值  >>> s2)

# class Student1(object):
#     def __init__(self,name):
#         self.name=name
# print Student1('xly')
# print str(Student1('xly'))
# s=Student1('xly2')
# print repr(s)
#
# class Student2(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
#     __repr__=__str__
#
# print Student2('xly3')
# print str(Student2('xly3'))
# s2=Student2('xly4')
# print repr(s2)


#    __iter__(),next()
#    __iter__()用来返回迭代对象,这里就是其本身
#    next()  返回迭代结果,设置迭代结束的条件

# class Fib(object):
#     def __init__(self):
#         self.a, self.b=0,1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 1000:
#             raise StopIteration()
#         return self.a
# li=list()
# for i in Fib():
#     li.append(i)
# print li


#   __getitem__()
#   定义用[]从对象中取值的方法

# class Fib2(object):
#     def __getitem__(self, item):
#         if isinstance(item,int):#实现按下标取元素的功能
#             a,b=1,1
#             for x in range(item):
#                 a,b=b,a+b
#             return a
#         elif isinstance(item,slice):#实现切片功能
#             start = item.start
#             stop = item.stop
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#         else:
#             pass#还可以添加字典的按key取value的功能,以及切片的step参数和负数的处理
#
# li2=list()
# for i in range(20):
#     li2.append(Fib2()[i])
# print li2
# print Fib2()[5:20]

#   __getattr__()
#   当调用对象不存在的属性时,python解释器会试图调用__getattr__()方法,动态的返回属性(也可以返回方法)

# class Chain(object):
#     def __init__(self,path=''):
#         self.path=path
#
#     def __getattr__(self, item):
#         return Chain('%s/%s'%(self.path,item))
#
#     def __call__(self, arg):
#         return Chain('%s/%s'%(self.path,arg))
#
#     def __str__(self):
#         return self.path
#
# print Chain().static.template.login.users('xly').index
#
# class Student(object):
#     def __getattr__(self, item):
#         if item == "age":
#             return lambda:25
#         raise AttributeError('\'Student\' object has no attribute \'%s\''%item)#对于其它未定义的属性依旧抛出异常
#
# print Student().age()#__getattr__返回值为函数时调用

#    __call__(),callable()
#    使类的实例对象可以调用(如>>> s=Student() >>> s() )
#    __call__()还可以添加参数
#    callable()可以判断使否是可调用对象
#    函数是可调用对象,设置了__call__()的类创建的实例也是可调用对象

# class Student(object):
#     def __init__(self,name):
#         self.name=name
#
#     def __call__(self,age=""):
#         return '__call__:'+self.name+"--age-"+age
#
#     def __str__(self):
#         return '__str__:'+self.name
#
# s=Student('xly')
# print s
# print s()
# print s("28")
#
# class Student2(object):
#     def __init__(self,name):
#         self.name=name
#
#     def __str__(self):
#         return '__str__:'+self.name
#
# s2=Student2('xly2')
#
#
# print 'Student1 callable:',callable(s)
# print 'Student2 callable:',callable(s2)
# print abs
# print 'function callable:',callable(abs)
# -------------------------------------------------------------------------------------------------------------------#
# 单例模式
#
#    共享此类的同一个类属性,此类属性即为类的对象
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'instance'):
#             cls.instance=super(Singleton,cls).__new__(cls)
#         return cls.instance
#
# s1=Singleton()
# s2=Singleton()
# s1.test="test1"
#
# print s1.test,s2.test
# print s1==s2

#     #装饰器形式的单例
# def single_decorate(cls):
#     instances={}
#     def single(*args,**kwargs):
#         if cls not in instances.keys():
#             instances[cls]=cls(*args,**kwargs)
#         return instances[cls]
#     return single
#
# @single_decorate
# class MySingleTest(object):
#     pass
#
# t1=MySingleTest()
# t2=MySingleTest()
#
# t1.test='test1'
# print t1.test,t2.test
# print t1==t2


# -------------------------------------------------------------------------------------------------------------------#
# 使用元类

#    使用type()创建类
#    可以动态的创建类
#    与用class创建类完全一致,python解释器在遇到class时也是扫描class的语法之后用type来构建类
#    格式为    type(类名,继承的父类(用tuple接收),用dict()将类中方法名和对应的函数名绑定)
#    定义类方法加上修饰器即可

"""
下述两种写法并无区别
class Hello(object):
    def hello(self,name='world'):
        print "Hello,%s"%name

h=Hello()
h.hello()
"""
# @classmethod
# def classfn(cls,name="World"):
#     print "ClassMethod: Hello, %s"%name
#
#
# def fn(self,name='world'):
#     print "Hello,%s"%name
#
# Hello=type('Hell',(object,),dict(hello=fn,class_hello=classfn))
#
# h=Hello()
#
# h.hello()
# Hello.class_hello()
# print h
# print Hello


#    metaclass(元类),可用于设计ORM框架
#    __new__()方法先创建实例,__new__()返回值就是实例对象,__init__()对实例进行初始化.
#    __new__()在创建实例之前,__init__()在创建实例之后.
#    __new__()方法是在创建实例前就存在的,所以其本身是个类方法,参数为__new__(cls,*args,**kwargs)

#    示例1:新建一个Mylist类继承List并添加一个功能同append()的add()方法
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         return type.__new__(cls,name,bases,dict(add = lambda self,value: self.append(value)))
#
# class Mylist(list):
#     __metaclass__ = ListMetaclass
#
# L=Mylist()
# print L
# L.add(25)
# print L


#        示例2:用元类实现一个ORM框架

#            步骤1:定义字段数据类型(StringField,IntegerField)
#
# class Field(object):
#
#     def __init__(self,name,column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s:%s>'%(self.name,self.column_type)
#
# class StringField(Field):
#
#     def __init__(self,name):
#         super(StringField,self).__init__(name,'varchar(100)')
#
# class IntegerField(Field):
#
#     def __init__(self,name):
#         super(IntegerField,self).__init__(name,'bigint')
#
#
#
#             #步骤2:编写ModelMetclass
# class ModelMetaclass(type):
#     def __new__(cls, name,bases,attrs):
#         if name == 'Model':
#             return type.__new__(cls,name,bases,attrs)
#         mappings=dict()
#         for k,v in attrs.iteritems():
#             if isinstance(v,Field):
#                 print 'Found Mapping: %s-->%s'%(k,v)
#                 mappings[k]=v
#         for k in mappings.iterkeys():
#             attrs.pop(k)
#
#         attrs['__table__']=name
#         attrs['__mappings__']=mappings
#         return type.__new__(cls,name,bases,attrs)
#
# class Model(dict):
#     __metaclass__ = ModelMetaclass
#
#     def __init__(self,**kwargs):
#         super(Model,self).__init__(**kwargs)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'"%key)
#
#     def __setattr__(self, key, value):
#         self[key]=value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k,v in self.__mappings__.iteritems():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self,k,None))
#
#         sql = 'insert into %s (%s) values (%s)'%(self.__table__, ','.join(fields), ','.join(params))
#         print ('SQL: %s'%sql)
#         print ('args: %s'%str(args))
#     def myprint(self):
#         print 'Model print'
#
#
# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#     def myprint(self):
#         print 'User test'
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()
# print 'id='+str(u['id'])
# u.myprint()

# ************关于元类以及从代码创建对象的过程***************
"""
type类可以创建类,解释器也是通过type来创建类的.
由于type可以创建类,所以可以自己定义,动态的传入参数,自定义生成类的属性,方法
因此可以用于ORM,事先不知道创建的对象需要哪些属性

解释器创建对象的过程:
解释器先遍历一遍代码,然后在创建类时将此class代码的名字(如User),父类,和定义的属性方法传给其元类__metaclass__中的(自身没有在父类中找)__new__(cls,name,bases,attrs)方法的对应参数
__metaclass__的__new__方法创建出的对象是一个类(即class User),即可以使用这个产生的类中的__new__方法来创建此类的实例对象(即object user)
在__new__创建对象之后,调用__init__方法对此对象(object u)初始化赋值

"""

# -------------------------------------------------------------------------------------------------------------------#
# 测试调试,单元测试暂略
# -------------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------------------------------------#

# IO编程
# IO即Input和Output,由于程序和运行时的数据时在内存中驻留,所以(从磁盘,网络等)进内存叫Input,出内存叫Output
# 同步和异步的区别在于是否等待IO执行的结果


# 文件读写
#    open,close
#    open的mode参数
#        r:只读模式, r+:读写模式打开,  w:清空文件,不能用file.read方法,可以用来创建文件   w+:清空文件可以用file.read方法
#        a:追加内容,不能用read方法    a+:追加内容,可以用read方法       rU:自动探测行尾符
# f=None
# try:
#     f=open('/Users/xly/Documents/IOtest.txt','r')
#     print f.read()
#
# except IOError,e:
#      raise IOError('IOERROR')
# finally:
#     if f:
#         f.close()
#
#
# with open('/Users/xly/Documents/IOtest.txt','r') as f2:
#     print f2.read()

#    with
#    形如: with obj as var
#    with是对try,except,finally的一种简化操作
#    使用要求:跟在with后的对象必须有__enter__()和__exit__()方法
#    1,__enter__(self)方法首先被执行,方法返回的值赋给as后的变量(var)
#    2,执行with obj as var下方的代码块
#    3,__exit__(self,type,value,trace)方法被调用,参数分别为异常的种类,描述和堆栈追踪
#    ps:第二步执行结束或抛出异常时都会执行__exit__函数,对资源进行清理或者关闭文件都可以放在__exit__函数中

# class Withclass(object):
#     def __enter__(self):
#         print "in enter"
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print "in exit"
#         print "close file"
#         print '(type,value,trace)=>%s---%s---%s'%(exc_type,exc_val,exc_tb)
#
#     def raise_exception(self):
#         n=1/0
#         return n
#
#     def no_exception(self):
#         n=255
#         return n
# #有异常需要处理还是需要except
# try:
#     with Withclass() as test:
#         test.raise_exception()
# except StandardError,e:
#     pass
#
# with Withclass() as test:
#     test.no_exception()

#    读取编码问题,写文件
# with open('/Users/xly/Documents/IOtest.txt') as f:
#     while True:
#         text=f.read(1)
#         if text=='':
#             break
#         print text
#     print 'END'

# with open('/Users/xly/Documents/IOtest.txt','rb') as f:
#     while True:
#         #行末带有换行符\n,用strip去掉
#         text=f.readline().strip()
#         if text=='':
#             break
#         print text.decode('gbk')
#     print 'END'
#
# import codecs
# with codecs.open('/Users/xly/Documents/IOtest.txt','r','gbk') as f:
#     while True:
#         text=f.readline().strip()
#         if text=='':
#             break
#         print text
#     print 'END'
#
# with codecs.open('/Users/xly/Documents/IOtest.txt','w','gbk') as f:
#    f.write('Hello World \n 2nd line \n 第三行'.decode('utf-8'))

# -------------------------------------------------------------------------------------------------------------------#
# 操作文件和目录-->os模块
# import os
# print os.name
# print os.uname()
# print '系统参数:',os.environ
# print '获取指定参数:',os.getenv('PATH')
# print '当前目录绝对路径:',os.path.abspath('.')#.表示当前目录,..表示上一级目录
# print '合并路径:',os.path.join('/Users/xly','testdir/testdir2')#会根据系统调用不同的路径分隔符
#
# # os.mkdir('/Users/xly/testdir')#创建文件夹
# # open('/Users/xly/testdir/test.txt','w').close()#创建文件
# # os.rename('/Users/xly/testdir/test.txt','/Users/xly/testdir/test.py')
# # os.remove('/Users/xly/testdir/test.py')#删除文件
# # os.rmdir('/Users/xly/testdir')#删除文件夹
#
# print '拆分路径:',os.path.split('/User/xly/testdir/file.txt')
# print '获取后缀名:',os.path.splitext('/User/xly/testdir/file.txt')


# 练习:遍历当前文件目录
# os.path.isdir(x)-->x是否为文件夹
# os.listdir(path)-->路径下所有文件&文件夹
# print os.listdir('.')
#
# def search(path,n=-1):
#     files=os.listdir(path)
#     files_path=[]
#     for file in files:
#         file_path=os.path.join(path,file)
#         files_path.append(file_path)
#     n+=1
#     for file in files_path:
#         if not os.path.isdir(file):
#             print predash(n)+os.path.split(file)[1]
#         else:
#             new_path=os.path.join(path,file)
#             print predash(n).replace('|','▼')+os.path.split(new_path)[1]
#             search(new_path,n)
# def predash(n):
#     dash='|---'
#     for i in range(n):
#         dash=dash+'---'
#     return dash
# search('/Users/xly/Pyprojects/pytest')
# -------------------------------------------------------------------------------------------------------------------#
#json
# import json
# d ={
#     'name':'Bob',
#     'age':20,
#     'score':88
# }
# print d
# d_str=json.dumps(d)
# print d_str
# d_new=json.loads(d_str)
#
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#
# s=Student('xly',27,100)
#
# def stuedent2dict(s):
#     d={
#         'name':s.name,
#         'age':s.age,
#         'score':s.score
#     }
#     return d
#
# s_str=json.dumps(s,default=stuedent2dict)
# print s_str
#
# def dict2student(d):
#     s=Student(d['name'],d['age'],d['score'])
#     return s
# s_obj=json.loads(s_str,object_hook=dict2student)
# print s_obj
# -------------------------------------------------------------------------------------------------------------------#

import os
# unix/linux下提供fork()创建子进程
# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()
# if pid==0:
#     print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
#
#     pid = os.fork()#在主进程中再开一个进程
#     if pid==0:
#         print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
#     else:
#         print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

# windows下用multiprocessing创建子进程
# from multiprocessing import Process
#
# def run_proc(name):
#     print 'Run child process %s(%s)...'%(name,os.getpid())
#
# if __name__ == '__main__':
#     print 'Parent process %s.'%os.getpid()
#     p = Process(target=run_proc,args=('test',))
#     print 'Process will start.'
#     p.start()
#     p.join()
#     print 'Process end'

# 进程池
from multiprocessing import Pool
import os,time,random

# def long_time_task(name):
#     print 'Run task %s(%s)...'%(name,os.getpid())
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds.'%(name,(end - start))
# if __name__ == '__main__':
#     print 'parent process %s'%os.getpid()
#     #Pool默认大小为cpu核数,
#     p=Pool(5)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print 'Waiting for all sub process done...'
#     #调用join回等待所有子进程执行完毕,调用join 之前必须调用close
#     p.close()
#     p.join()
#     print 'All subprocesses done'




# 进程间通信
from multiprocessing import Process,Queue
import os, time, random
# #
# def write(q):
#     for value in ['A','B','C']:
#         print 'Put %s into queue...'%value
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     while True:
#         value=q.get(True)
#         print 'Get %s from queue'%value
#
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read,args=(q,))
#
#     pw.start()
#
#     pr.start()
#
#     pw.join()
#     #强制终止子进程
#     pr.terminate()
# -------------------------------------------------------------------------------------------------------------------#
# 线程
# import time,threading
#
# #创建一个线程
# def loop():
#     print 'thread %s is running ...'%threading.current_thread().name
#     n=0
#     while n<5:
#         n=n+1
#         print 'thread %s >>> %s'%(threading.current_thread().name,n)
#         time.sleep(1)
#     print 'thread %s ended.'%threading.current_thread().name
#
# print 'thread %s is running...' %threading.current_thread().name
# t=threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print 'thread %s ended.'%threading.current_thread().name

# 线程的锁
# import time, threading
#
# # 假定这是你的银行存款:
# balance = 0
# lock=threading.Lock()
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance

# 多线程死循环只能占用160%cpu
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()


# 测试python的多线程速度
#
# import threading
#     #计时器
# def timer(f):
#     def count(*args,**kwargs):
#         start=time.time()
#         res=f(*args,**kwargs)
#         end=time.time()
#         print 'total time : {}'.format(end-start)
#         return res
#     return count
#
# num=10000000
#
#
#     # 循环计算任务
# def loop(n):
#     for i in range(n):
#         i=1^1
#
#     #单线程顺序运行两次,每次运算次数num
# @timer
# def single_thread():
#     t1=threading.Thread(target=loop,args=(num,))
#     t1.start()
#     t1.join()
#     t2=threading.Thread(target=loop,args=(num,))
#     t2.start()
#     t2.join()
#     print "single_thread end"
#
#     #多线程完成
# @timer
# def multi_thread():
#     t1=threading.Thread(target=loop,args=(num,))
#     t2=threading.Thread(target=loop,args=(num,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print "multi_thread end"
#
# single_thread()
# multi_thread()

# -------------------------------------------------------------------------------------------------------------------#
# 正则匹配身份证和电话
# import re
#
# ID_re=r'^([1-9]\d{5}[12])\d{3}(0[1-9]|1[012])(0[1-9]|1[0-9]|2[0-9]|3[01])\d{3}[0-9xX]$'
# test_ID='420602198907271571'
# if re.match(ID_re,test_ID):
#     print 'ID True'
# else:
#     print 'ID False'
#
# r'^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}'
# phone_re=r'^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}'
# test_phone='15800502039'
# if re.match(phone_re,test_phone):
#     print 'phone True'
# else:
#     print 'phone False'


# -------------------------------------------------------------------------------------------------------------------
# 正则表达式
'''
匹配字符:
    \d  匹配一个数字
    \w  匹配一个字母或数字
    \s  匹配一个空白符(空格,tab)
    .   匹配任意字符
    []  表示范围            如:[0-9a-zA-Z\_]可以匹配一个字母数字或者下划线
    [^] 不包含             如:[^a-z]可以匹配不在a-z中的任意一个字符

字符数量:
    *   表示任意个,包括0
    +   表示至少一个      如:\s+表示至少一个空格,可以匹配' ','    '等
    ?   表示0个或1个
    {}  表示具体数量范围    如:\d{3}表示三个数字,\d{3,8}表示3到8个数字

逻辑表达:
    [A|B]匹配A或B      如:[p|Python]可以匹配python和Python


字符位置
    ^   表示开头
    $   表示结尾

分组
    ()  可用于re的group函数中,获取分组匹配的信息    如:^(\d{3})-(\d{3,8})$


'''
import re
# match(r'正则', 字符串)     判断字符串是否符合正则表达式,成功返回一个match对象
# search(r'正则', 字符串)    从字符串中寻找一个符合正则表达式的match对象
# findall(r'正则', 字符串)   寻找字符串中所有符合正则表达式的groups的列表

# #re.match(),匹配成功返回一个match对象,失败返回None
# print re.match(r'^\d{3}-\d{3,8}$', '010-12345')
# print re.match(r'^\d{3}-\d{8}$', '010-12345')

# # re.split()切分字符串时可以使用正则表达式
# print 'a b  c    d'.split(' ')
# print re.split(r'\s+','a b  c    d')
# print re.split(r'[\d\s]+', 'a3rfjirj329rfj 23 23 j39 3 32nh923 tfa  ')

# # group()可以提取子字符串,groups返回分组的list,group(0)永远返回字符串本身,group(i)返回分组第i个元素
# m = re.match(r'^(\d{3})-(\d{3,8})', '010-12345')
# print m
# print m.groups()
# print m.group(0), m.group(1), m.group(2)
#
# t = "11:01:05"
# m = re.match(r'^([0-1][0-9]|2[0-3])\:([0-5][0-9]|[0-9])\:([0-5][0-9]|[0-9])$', t)
# print m.groups()


# # 贪婪匹配,默认尽可能多的匹配,如果要少匹配,在后面加?
# print re.match(r'^(\d+)(0*)$', '102300').groups()
# print re.match(r'^(\d+?)(\d+?)', '102300').groups()


# # re.compile()预编译正则表达式,生成regular expression对象,调用时不用给出正则字符串
# re_phone = re.compile(r'^(\d{3})\-(\d{3,8})$')
# print re_phone.match('010-12345').groups()

# # 匹配多行
# single_line_str = "Return a 2-tuple containing (new_string, number)."
#
# multi_lines_str = """Return a 2-tuple containing (new_string, number).
#     new_string is the string obtained by replacing the leftmost
#     non-overlapping occurrences of the pattern in the source
#     string by the replacement repl.  number is the number of
#     substitutions that were made. repl can be either a string or a
#     callable; if a string, backslash escapes in it are processed.
#     If it is a callable, it's passed the match object and must
#     return a replacement string to be used."""
#
# re_multilines = re.compile(r'(new)_(string)')
# re_multilines2 = re.compile(r'(new)_(string)')
#
# print re_multilines.match(single_line_str)
# print re_multilines.search(multi_lines_str).groups()
# print re_multilines2.findall(multi_lines_str)




# # 练习
# re_mail = re.compile(r'^([\w\.\-\_]*)@(\w*)\.\w*$')
# print re_mail.match('bill.gates@microsoft.com').groups()
# -------------------------------------------------------------------------------------------------------------------
# collections

#  namedtuple可以穿凿一个tuple的子类,可以命名类名和属性名,既可以通过角标取元素,也可以通过属性名取元素

import collections
# point = collections.namedtuple('Point', ['x', 'y'])
# p = point(1, 2)
# print point
# print p
# print p.x, p.y
# print p[0], p[1]
# print p._asdict(), p._asdict()['x']
# print p._replace(x=100)
# print p

# q = collections.deque(['a', 'b', 'c'])
# print q
# q.append('x')
# q.extend(['y', 'z'])
# print q
# q.appendleft('1')
# q.extendleft(['2', '3'])
# print q
# q.pop()
# print q
# q.popleft()
# print q
# q.append('1')
# print q
# q.remove('1')
# print q
# q.reverse()
# print q
# print q. count('y')

# dd = collections.defaultdict(lambda: 'A keyerror happens')
# print dd['a']


# od = collections.OrderedDict()
# od['x'] = 1
# od['y'] = 2
# od['z'] = 3
# print od
# print od.keys()
#
# d = dict()
# d['x'] = 1
# d['y'] = 2
# d['z'] = 3
# print d
# print d.keys()


# class LastUpdatedOrderedDict(collections.OrderedDict):
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         flag = 0 if key in self.keys() else 1
#         if self._capacity - flag < len(self):
#             last = self.popitem(last=False)
#         if not flag:
#             del self[key]
#             print 'set:', (key, value)
#         else:
#             print 'add:', (key, value)
#         super(LastUpdatedOrderedDict, self).__setitem__(key, value)


# from collections import OrderedDict
#
# class LastUpdatedOrderedDict(OrderedDict):
#
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print 'remove:', last
#         if containsKey:
#             del self[key]
#             print 'set:', (key, value)
#         else:
#             print 'add:', (key, value)
#         OrderedDict.__setitem__(self, key, value)
# luod = LastUpdatedOrderedDict(3)
# luod['x'] = 1
# print luod
# luod['y'] = 2
# print luod
# luod['z'] = 3
# print luod
# luod['x'] = 4
# print luod
# luod['a'] = 5
# print luod

# c = collections.Counter('asdfaewgvcfewafarwf')
# print c
# print c['f']
# print list(c.elements())
# print c.most_common(3)

# -------------------------------------------------------------------------------------------------------------------
# base64
import base64
#
# 使用base64编码的原因:
# ascii 0~31和127(共33个)为控制字符或通信专用字符(为不可见字符),32~126(共95个)是可见字符,后128称为扩展ascii码
# 对于不可见字符,不同的设备可能会有不同的处理方式,对于网络传输(传输中含有图片,音频等文件,这些文件转成二进制传输通常含有不可见字符)
# 为了不可见字符不被错误的处理,就先把数据用base64编码,全部变为可见字符
#
# base64编码的思路:
# 将数据转为二进制后,每三个字节为一组,一个字节8bit位.共24位.将24位分为4份,每份6位.然后在6位的前面补两个0,则变成了4个字节,每个字节最高的
# 两位为0(即不超过63).然后对应base64的编码表全转为可见字符.如果数据不为3字节的倍数,将余数(1或2)的比特位用0补齐(8或16bit补成12或18bit)
# 转为2到3个字节的base编码表的字符,剩下的用=补齐(base64编码好的文件字节数位4的倍数)
#
# base64编码表:
# 0~25: A~Z,  26~51: a~z, 52~61: 0~9,   62: +,  63: /
#
# 示例:
# 数据字符串:         ly
# 转成ascii:         108 121
# 转成二进制:         0110 1100  0111 1001
# 每6bit在前面加00:   0001 1011  0000 0111  001001
# 位数不足用0补齐:     0001 1011  0000 0111  00100100
# 转成十进制:        27  7   36
# 转成base64:       b  H  k
# 不足4位用=补齐:     bHk=
#
# 验证:
# print 'ly base64 ', base64.b64encode('ly')
# 对base64编码的定位:
# 不算安全领域的加密解密, 不能直接一眼认出
# 编解码速度非常快
# 适合用于http, mime协议下快速传输数据

# s_base64 = base64.b64encode(r'binary\x00string')
# print s_base64
# print base64.b64encode('binary\\x00string')
# s_ascii = base64.b64decode(s_base64)
# print s_ascii


# def safe_base64_decode(s):
#     while len(s) % 4 != 0:
#         s += '='
#     return base64.b64decode(s)
#
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# print('Pass')

# -------------------------------------------------------------------------------------------------------------------
# struct
# 大端,小端字节序.网络序都是大端字节序,主机序既有大端也有小端
# 大端:高位字节放地址低位
# 小端:低位字节放地址低位
# struct用处时将python数据类型和二进制数据类型的转换(用于和其他平台进行交互)
'''
struct常用的格式
format                      c中数据类型                  python中数据类型                 标准大小
c                           char                        长度为1的字符串                  1
b                           signed char                 整型                            1
B                           unsigned char               整型                            1
?                           _Bool                       bool                            1
h                           short                       整型                             2
H                           unsigned int                整型                             2
i                           int                         整型                             4
I                           unsigned int                整型                             4
l                           long                        整型                             4
L                           unsigned long               整型                             4
q                           long long                   整型                             8
Q                           unsigned long long          整型                             8
f                           float                       浮点                             4
d                           double                      浮点                             8
s                           char[]                      字符串
p                           char[]                      字符串
P                           void *                      整型

'''

# n = 10240099
# b1 = (n & 0xff000000) >> 24
# b2 = (n & 0xff0000) >> 16
# b3 = (n & 0xff00) >> 8
# b4 = (n & 0xff) >> 0
# l = [b1, b2, b3, b4]
# cl = map(chr, l)
# print l, cl
# print ''.join(cl), repr(''.join(cl))
#
# import struct
# print struct.pack('>I', 10240099), repr(struct.pack('>I', 10240099))
# print struct.pack('<I', 10240099), repr(struct.pack('<I', 10240099))
# import binascii
# import os, struct
# abspath = os.path.abspath('.')
# img_path = os.path.join(abspath, 'img/bmp_test.bmp')
# with open(img_path, 'rb') as img:
#     s = img.read(30)
#     print binascii.b2a_hex(s)
#     print struct.unpack('<ccIIIIIIHH', s)
# sb = '42 4d 96 05 13 00 00 00 00 00 36 00 00 00 28 00 00 00 7c 02 00 00 16 fe ff ff 01 00 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 3e ae 5b ff 3d aa 59 ff'
# sl = sb.split(' ')
# sl2 = []
# for s in sl:
#     s = hex(int(s, 16))
#     sl2.append(s)
# print sl2
#
# print repr('你好')
# print '\xe4\xbd\xa0'
#
# img_path2 = os.path.join(abspath, 'img/Picture1.bmp')
# with open(img_path2, 'rb') as img:
#     s = img.read(30)
#     print repr(s)
#     print struct.unpack('<ccIIIIIIHH', s)
#
# img_path3 = os.path.join(abspath, 'img/Picture2.bmp')
# with open(img_path3, 'rb') as img:
#     s = img.read(30)
#     print repr(s)
#     print struct.unpack('<ccIIIIIIHH', s)
#
#
# img_path4 = os.path.join(abspath, 'img/QQ截图asdfasdfa.bmp')
# with open(img_path4, 'rb') as img:
#     s = img.read(30)
#     print repr(s)
#     print struct.unpack('<ccIIIIIIHH', s)

# -------------------------------------------------------------------------------------------------------------------
# hashlib
# 常见摘要算法有   md5, sha1, sha256, sha512 使用方法类似越后面的越安全,但是越慢
# 摘要算法不算加密算法,因为不能反推明文,只能用于防篡改.
# 摘要算法的单向性使其可以再不储存明文口令的情况下验证用户口令

# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?')
# print (md5.hexdigest())
#
#
# db = {}
#
#
# def get_md5(s):
#     md5 = hashlib.md5()
#     md5.update(s)
#     return md5.hexdigest()
#
#
# def register(name, password):
#     db[name] = get_md5(name + 'the salt' + password)
#
#
# def login(name, password):
#     if db[name] == get_md5(name + 'the salt' + password):
#         print '%s login success' % name
#     else:
#         print '%s password error' % name
#
#
# register('xly', '12345')
# register('xxx', '12345')
#
# login('xxx', '1234')
# login('xxx', '12345')
# print db
# -------------------------------------------------------------------------------------------------------------------
# itertools

# import itertools
# for key, group in itertools.groupby('AaaBBbcCAAa', lambda x: x.lower()):
#     print(key, list(group))

# -------------------------------------------------------------------------------------------------------------------
# XML解析
# from xml.parsers.expat import ParserCreate
#
#
# # sax解析xml
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.returns_unicode = True
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)
#
#
# # 生成xml
# def encode(s):
#     return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
# L = list()
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
# print ''.join(L)


# import urllib
# from xml.parsers.expat import ParserCreate
# # 解析天气预报
# # 百度天气
# '''
# 形如:
# <CityWeatherResponse>
#     <status>success</status>
#     <currentCity>上海</currentCity>
#     <results>
#         <result>
#         <date>周四 01月19日 (实时：8℃)</date>
#         <dayPictureUrl>
#         http://api.map.baidu.com/images/weather/day/yin.png
#         </dayPictureUrl>
#         <nightPictureUrl>
#         http://api.map.baidu.com/images/weather/night/duoyun.png
#         </nightPictureUrl>
#         <weather>阴转多云</weather>
#         <wind>北风微风</wind>
#         <temperature>9 ~ 0℃</temperature>
#         </result>
#         <result>...</result>
#         <result>...</result>
#         <result>...</result>
#     </results>
# </CityWeatherResponse>
#
# '''
# import re
# xml = ''
# try:
#     page = urllib.urlopen('http://api.map.baidu.com/telematics/v2/weather?location=%E4%B8%8A%E6%B5%B7&ak=B8aced94da0b345579f481a1294c9094')
#     xml = page.read()
# finally:
#     page.close()
# # print xml
#
#
# class BaiduWeatherSaxHandler(object):
#     def __init__(self):
#         self._weather = dict()
#         self._count = 0
#         self._current_element = ''
#
#     def start_element(self, name, attrs):
#         if name == 'result':
#             self._count += 1
#             self._weather[self._count] = dict()
#         self._current_element = name
#
#     def end_element(self, name):
#         pass
#
#     def char_data(self, text):
#         # 排除换行符和空白内容
#         re_str = '^[\n|\s]+$'
#         if self._current_element and not re.match(re_str, text) and self._weather:
#             self._weather[self._count][self._current_element] = text
#
#     def show_weather(self):
#         for v in self._weather.values():
#             print v['date'], '\t'*(7-len(v['date'])), v['temperature'], v['weather'], v['wind']
#
# handler = BaiduWeatherSaxHandler()
# parser = ParserCreate()
#
# parser.returns_unicode = True
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
#
#
# parser.Parse(xml)
#
# handler.show_weather()
#
# # 中国天气网
# '''
# 形如:
# <china dn="day">
#     <city quName="黑龙江" pyName="heilongjiang" cityname="哈尔滨" state1="1" state2="0" stateDetailed="多云转晴" tem1="-12" tem2="-25" windState="西南风3-4级转北风小于3级"/>
#     <city quName="吉林" pyName="jilin" cityname="长春" state1="1" state2="1" stateDetailed="多云" tem1="-10" tem2="-21" windState="西北风小于3级"/>
#     <city quName="辽宁" pyName="liaoning" cityname="沈阳" state1="1" state2="1" stateDetailed="多云" tem1="-6" tem2="-18" windState="北风小于3级转3-4级"/>
#     <city quName="海南" pyName="hainan" cityname="海口" state1="1" state2="3" stateDetailed="多云转阵雨" tem1="24" tem2="18" windState="东风转东北风3-4级"/>
# </china>
# '''
#
# china_xml = ''
# try:
#     page = urllib.urlopen('http://flash.weather.com.cn/wmaps/xml/china.xml')
#     china_xml = page.read()
# finally:
#     page.close()
#
#
# class ChinaWeatherSaxHandler(object):
#     def __init__(self):
#         self._weather = dict()
#
#     def start_element(self, name, attrs):
#         if attrs.get('cityname'):
#             self._weather[attrs['cityname']] = attrs
#
#     def end_element(self, name):
#         pass
#
#     def char_data(self, text):
#         pass
#
#     def show_weather(self):
#         for v in self._weather.values():
#             print v['cityname'] + '\t', v['tem2'] + '~' + v['tem1'] + '\t', v['stateDetailed'] + '\t', v['windState']
#
# handler = ChinaWeatherSaxHandler()
# parser = ParserCreate()
#
# parser.returns_unicode = True
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
#
# parser.Parse(china_xml)# handler.show_weather()

# -------------------------------------------------------------------------------------------------------------------
# 复习单例模式和__new__方法的参数以及ORM实现复习

# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls.instance
#
#     def __init__(self, *args, **kwargs):
#         # 单例模式__new__方法带参数的时候也要覆写__init__增加参数,否则报错
#         pass
#
# s1 = Singleton()
# s2 = Singleton()
# s1.test = 'test1'
# print s2.test

# class Field(object):
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s: %s>' % (self.name, self.column_type)
#
#
# class IntegerField(Field):
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')
#
#
# class StringField(Field):
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(120)')
#
#
# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if cls == 'Model':
#             return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
#         mapping = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 mapping[k] = v
#         for k in mapping.keys():
#             del attrs[k]
#         attrs['__tablename__'] = name
#         attrs['__mapping__'] = mapping
#         return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)
#
#
# class Model(object):
#     __metaclass__ = ModelMetaclass
#     d = dict()
#
#     def __init__(self, **kwargs):
#         for k in (k for k in kwargs if k in self.__mapping__):
#             self.d[k] = kwargs[k]
#
#     def save(self):
#         field = []
#         args = []
#         for k, v in self.__mapping__.items():
#             field.append(k)
#             if isinstance(v, StringField):
#                 args.append('"{0}"'.format(self.d[k]))
#             elif isinstance(v, IntegerField):
#                 args.append('{0}'.format(self.d[k]))
#         sql = 'insert into %s (%s) value(%s)' % (self.__tablename__, ','.join(field), ','.join(args) )
#         print sql
#
#
# class User(Model):
#     id = IntegerField('id')
#     name = StringField('name')
#     pswd = StringField('pswd')
#
#
# u = User(id=123, name='xly', pswd='mypswd')
# u.save()

# object和type的__new__方法接收的参数不同
# T.__new__(S, *more) S(T的子类)实例(实例可以是类也可以是类创建的对象)
# class ObjectSubclass(dict):
#     pass
# o = dict.__new__(ObjectSubclass)
# print isinstance(o, dict)
#
#
# class TypeSubclass(type):
#     pass
#
#
# def hello():
#     return 'hello'
# #               type的子类       生成的类的名称   生成类创建对象的父类  类中定义的属性和方法
# t = type.__new__(TypeSubclass, 'typesubclass', (dict,), dict(hello=hello))
# print isinstance(t, TypeSubclass)
# print isinstance(t, dict), isinstance(t(), dict)

# -------------------------------------------------------------------------------------------------------------------
# HTMLParser

# HTML实体:
# 在 HTML 中，某些字符是预留的。
# 在 HTML 中不能使用小于号（<）和大于号（>），这是因为浏览器会误认为它们是标签。
# 如果希望正确地显示预留字符，我们必须在 HTML 源代码中使用字符实体（character entities）
# 字符实体的使用方法 &entity_name 或者  &#entity_number 或者 &#xhex_number(十六进制数字)
# 都称为character reference,第一种称为 character entity reference ,后面两种称为 numeric character reference
# 在html显示小于号  &lt          或者  &#60            或者 &#x3c

'''

解析HTML时,可以继承内置的HTMLParser类,覆写其中以handle_开头的函数

handle_starttag:    处理开始标签,形如<xx>
handle_endtag:      处理结束标签,形如</xx>
handle_startendtag: 处理开始结束标签,形如<xx/>
handle_data:        处理数据,即<xx>data</xx>间的数据
handle_comment:     处理注释,形如<!--comment-->
handle_entityref:   处理特殊字符,以#&开始的,一般为内码表现的字符
handle_charref:     处理特殊字符,以&开始的,如&lt
handle_decl:        处理<!开头的,形如<!DOCTYPE html>
handle_pi:          处理形如<?instruction>

'''
# from HTMLParser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print('data')
#
#     def handle_comment(self, data):
#         print('<!-- -->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

# urlopen经常打开失败,数据处理还没完成,暂时留着
# import urllib
# from HTMLParser import HTMLParser
#
# try:
#     page = urllib.urlopen('https://www.python.org/events/python-events/')
#     html = page.read()
# finally:
#     page.close()
#
# print html
#
# class MyHTMLParser(HTMLParser):
#     # 经典类继承时__init__不能用super,而且self要作为__init__的第一个参数
#     def __init__(self):
#         self.enter_list = False
#         self.tag_name = ''
#         self.conference = dict()
#         self.count = 0
#         HTMLParser.__init__(self)
#
#     def handle_starttag(self, tag, attrs):
#         for attr in attrs:
#             if attr[0] == 'class' and attr[1] == 'list-recent-events menu':
#                 self.tag_name = tag
#                 self.enter_list = True
#
#             if self.enter_list and tag == 'li':
#                 self.count += 1
#                 self.conference[self.count] = dict()
#
#     def handle_endtag(self, tag):
#         if self.tag_name and tag == self.tag_name:
#             self.enter_list = False
#             self.tag_name = ''
#
#     def handle_data(self, data):
#         if self.enter_list:
#             if self.lasttag == 'a':
#                 if not self.conference[self.count].get('Title'):
#                     self.conference[self.count]['Title'] = ''
#                 self.conference[self.count]['Title'] += data.strip()
#
#     def handle_entityref(self, name):
#         if self.enter_list and name == 'ndash':
#             # print '-'
#             pass
#
#
# parser = MyHTMLParser()
# parser.feed(html)
#
# print parser.conference

# -------------------------------------------------------------------------------------------------------------------
# python实现汉诺塔

# def hanoi(n, start, end, medium):
#     if n == 1:
#         print '%s --> %s' % (start, end)
#     elif n > 1:
#         hanoi(n-1, start, medium, end)
#         print '%s --> %s' % (start, end)
#         hanoi(n-1, medium, end, start)
# hanoi(3, 'A', 'C', 'B')


# def swap(l, i, j):
#     temp = l[i]
#     l[i] = l[j]
#     l[j] = temp
#
#
# def bubble_sort(l):
#     for i in range(len(l)):
#         for j in range(i, len(l)):
#             if l[i] > l[j]:
#                 swap(l, i, j)
#
#
# def quick_sort(l, start, end):
#     if start >= end:
#         return l
#     tag = l[start]
#     left = start
#     right = end
#     while start < end:
#         while start < end and l[end] >= tag:
#             end -= 1
#         l[start] = l[end]
#         while start < end and l[start] <= tag:
#             start += 1
#         l[end] = l[start]
#         quick_sort(l, left, end-1)
#         quick_sort(l, start+1, right)
#     return l
#
# l = [1561, 315, 684, 1654, 1651]
# l2 = [3, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 3]
# bubble_sort(l)
# print l
#
#
# print quick_sort(l2, 0, len(l2)-1)

# 10个数字分成两组各为5的数组,使他们和的差值最小
# def diff(l1, l2):
#     sum1 = 0
#     sum2 = 0
#     for i in l1:
#         sum1 += i
#     for i in l2:
#         sum2 += i
#     return sum2 - sum1
#
# # 差值最小的两个数分别放在两个数组中,有错误
# def split_group(l):
#     group1 = list()
#     group2 = list()
#     sum_diff = 0
#     count = 0
#     while len(l) > 0:
#         g1 = l.pop()
#         diff = None
#         for j in range(len(l)):
#             if not diff:
#                 diff = abs(l[j] - g1)
#                 index = j
#             elif abs(l[j] - g1) < diff:
#                 diff = abs(l[j] - g1)
#                 index = j
#         g2 = l.pop(index)
#         if sum_diff * diff >= 0:
#             group2.append(g1)
#             group1.append(g2)
#         else:
#             group1.append(g1)
#             group2.append(g2)
#
#
#
#         sum_diff += diff
#     return group1, group2
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random_list = [random.randint(0, 1000) for x in range(10)]
# print random_list
# print split_group(random_list[:]), 'Diff is ', diff(*split_group(random_list[:]))
#
#
# # 穷举法
# def enum_split_group(nums):
#     sum_diff = None
#     for i in range(1024):
#         binary_str = bin(i)
#         format_str = binary_str[2:]
#         l = map(int, format_str)
#         bin_sum = 0
#         for j in l:
#             bin_sum += j
#         if bin_sum == 5:
#             format_str = '00000{0}'.format(format_str)[-10:]
#             group1 = list()
#             group2 = list()
#
#             for j in range(len(format_str)):
#                 if int(format_str[j]):
#                     group1.append(nums[j])
#                 else:
#                     group2.append(nums[j])
#             if not sum_diff:
#                 sum_diff = abs(diff(group1, group2))
#                 result_group1, result_group2 = group1, group2
#             elif abs(diff(group1, group2)) < sum_diff:
#                 sum_diff = abs(diff(group1, group2))
#                 result_group1, result_group2 = group1, group2
#     return result_group1, result_group2, 'Diff is ', sum_diff
#
#
# print enum_split_group(random_list)

# -------------------------------------------------------------------------------------------------------------------
# 图形界面Tkinter

# from Tkinter import *
# import tkMessageBox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         tkMessageBox.showinfo('Message', 'Hello, %s' % name)
#
#
# app = Application()
# app.master.title('GUI Test')
# app.mainloop()

# -------------------------------------------------------------------------------------------------------------------
# 当年某道没做出来的面试题
# 找零问题,给出找零的金额,和货币的面值list.求有多少种方法

# charge = 5
# face_values = [1, 2, 3]

# 两种面额的组合方式
# count = 0
# d = dict()
# for i in range(len(face_values)):
#     if charge % face_values[i] == 0:
#         print face_values[i], charge/face_values[i]
#         count += 1
#         d[count] = {face_values[i]: charge/face_values[i]}
#
#     for n in range(charge/face_values[i]):
#         for j in range(i+1, len(face_values)):
#             if (charge - n * face_values[i]) % face_values[j] == 0:
#                 print face_values[i], n, face_values[j], (charge - n * face_values[i]) / face_values[j]
#                 count += 1
#                 d[count] = {face_values[i]: n, face_values[j]: (charge - n * face_values[i]) / face_values[j]}
#
#
# for key, value in d.items():
#     s = ''
#     for k, v in value.items():
#         s += '{0}*{1}+'.format(k, v)
#     s = s[:-1]
#     print key, s

# charge = 5
# face_values = [1, 2, 3]
# count_of_charge = [0 for x in range(len(face_values))]
# distinct_count = list()
#
# def odd_charge(charge, face_values, count_of_charge, j=0):
#     if charge < 0:
#         # print False, count_of_charge
#         pass
#     elif charge == 0:
#         print True, count_of_charge
#         # distinct_count.append(count_of_charge)
#     elif charge > 0:
#         for i in range(j, len(face_values)):
#             new_charge = charge - face_values[i]
#             count_of_charge_copy = count_of_charge[:]
#             count_of_charge_copy[i] += 1
#             odd_charge(new_charge, face_values, count_of_charge_copy, i)
#
#
# odd_charge(charge, face_values, count_of_charge)

# -------------------------------------------------------------------------------------------------------------------
# socket
'''
TCP:
    创建socket对象(ipv4,TCP):
    s = socket.sockt(socket.AF_INET, socket.SOCKET_STREAM)

    服务端绑定地址和接口并监听:
    s.bind(('127.0.0.1',9999))
    s.listen(5)
    服务端接收客户端的连接(客户端的socket对象和客户端地址):
    client_sock, client_addr = s.accept()

    客户端连接到服务端:
    s.connect(('127.0.0.1', 9999))

<<<<<<< HEAD
    socket对象发送信息:
    s.send(data)
    socket接收信息(1024为每次接收的大小):
    s.recv(1024)
=======

def odd_charge(charge, face_values, count_of_charge, j=0):
    if charge < 0:
        # print False, count_of_charge
        pass
    elif charge == 0:
        print True, count_of_charge
        # distinct_count.append(count_of_charge)
    elif charge > 0:
        for i in range(j, len(face_values)):    # 从上次递归的i开始防止重复出现。如 5-1-1-1-2和5-2-1-1-1，相同面值的数量是一样的，但是减去的顺序不一样
            new_charge = charge - face_values[i]
            count_of_charge_copy = count_of_charge[:]   # 切片取复制一份list，避免都在原list上修改
            count_of_charge_copy[i] += 1
            odd_charge(new_charge, face_values, count_of_charge_copy, i)
>>>>>>> 2d231e4294f905cf946c1e0e769fe77cd3d2c381

    TCP服务端客户端连接思路:
    1 服务端创建server_socket监听指定端口.
    2 客户端创建client_socket用connect()向服务器发起连接
    3 服务端用accept()接收客户端的client_socket对象和客户端的地址端口
    4 服务端和客户端使用client_socket的send()和recv()进行通信
UDP:
    UDP不需要监听和连接

    创建socket对象(ipv4, UDP):
    s = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)

    服务端绑定端口:
    s.bind(('127.0.0.1', 9999))

    socket通信:
    data, address = s.recvform(1024)
    s.recv(1024)
    s.sendto(data, address)


'''

# TCP
# import socket
#
# # 客户端socket访问sina
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET: IPv4网络协议,    SOCK_STREAM: 有保障的面向连接socket(TCP)
# s.connect(('www.sina.com.cn', 80))
# s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# receive_buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         receive_buffer.append(d)
#     else:
#         break
# s.close()
# data = ''.join(receive_buffer)
# head, html = data.split('\r\n\r\n', 1)
# path = '/Users/xly/Documents/sina.html'
# with open(path, 'w') as f:
#     f.write(html)


# 客户端服务端见socket_test


# -------------------------------------------------------------------------------------------------------------------
# SMTP发送邮件
'''
构造一个邮件对象就是一个Messag对象
如果构造一个MIMEText对象，就表示一个文本邮件对象
如果构造一个MIMEImage对象，就表示一个作为附件的图片
要把多个对象组合起来，就用MIMEMultipart对象
而MIMEBase可以表示任何对象

它们的继承关系如下：
Message
 MIMEBase
    --MIMEMultipart
    --MIMENonMultipart
        --MIMEMessage
        --MIMEText
        --MIMEImage
'''



# 简单的邮件
# from email.mime.text import MIMEText
# # 正文内容
# msg = MIMEText('Hello, this msg send by python', 'plain', 'utf-8')
#
# from_addr = '171538166@qq.com'
# password = 'tjsdwcgpvzqsbide'
# smtp_server = 'smtp.qq.com'
# to_addr = '15800502039@163.com'
#
# import smtplib
# server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()


# 一般的邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import os


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# 发送邮箱的账号密码以及smtp服务器地址, 收件人邮箱地址
from_addr = '171538166@qq.com'
password = 'tjsdwcgpvzqsbide'
smtp_server = ('smtp.qq.com', 465)
to_addr = '15800502039@163.com'

# # 邮件正文,文本为plain,也可以用html
# msg = MIMEText('Hello, this msg is sent by python', 'plain', 'utf-8')

# 添加附件用MIMEMultipart, 往其中添加MIMEText作为正文, MIMEBase作为附件
msg = MIMEMultipart()
msg.attach(MIMEText(
    '''<h1>Hello, this msg is sent by python with attachment</h1>
    <a href='https://www.baidu.com'>Baidu</a><br/>
    <img src='https://a-ssl.duitang.com/uploads/item/201604/11/20160411124911_xG3rt.png'/><br/>
    <img src='cid:0'/><br/>
    <img src='cid:1'/><br/>
    <img src='cid:2'/><br/>
    ''', 'html', 'utf-8'))
img_paths = []
img_name = ['pic_test.jpg', 'bmp_test.bmp', 'Picture1.bmp']
relative_path = os.path.join(os.getcwd(), 'img')
for n in img_name:
    img_path = os.path.join(relative_path, n)
    img_paths.append(img_path)

img_id = 0
for img_path in img_paths:
    with open(img_path, 'rb') as img:
        # 设置附件的MIME和文件名
        attachment = MIMEBase('image', img_path.split('.')[-1], filename=img_path.split(os.sep)[-1])
        # 附件必要的头信息
        # 指示用户代理如何显示附件
        attachment.add_header('Content-Disposition', 'attachment', filename=img_path.split(os.sep)[-1])
        # 附件的content_id可以用来把附件内嵌到邮件正文里,因为有些邮箱不支持在邮件界面打开外部链接
        attachment.add_header('Content-ID', '<{0}>'.format(img_id))
        img_id += 1
        attachment.add_header('X-Attachment-Id', '0')
        # 附件内容读进来
        attachment.set_payload(img.read())
        # 使用base64编码
        encoders.encode_base64(attachment)
        # 添加附件到MIMEMultipart
        msg.attach(attachment)


# 邮件的发件人,收件人,主题信息
msg['From'] = _format_addr(u'xly的qq邮箱 <%s>' % from_addr)
msg['To'] = _format_addr(u'xly的网易邮箱 <%s>' % to_addr)
msg['Subject'] = Header(u'SMTP test……', 'utf-8').encode()


server = smtplib.SMTP_SSL(*smtp_server)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()







