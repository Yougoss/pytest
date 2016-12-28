#coding:utf-8


#-------------------------------------------------------------------------------------------------------------------#
#__slots__

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
#
# s3.weight="80kg"

# __slots__用tuple定义,类创建的实例不允许绑定不在tuple中的属性(类本身可以添加属性)
#继承的子类中没有定义__slots__时,父类的限制对子类不起作用.
#继承的子类中定义__slots__时,子类允许定义的属性就是自身和父类__slots__的叠加
#-------------------------------------------------------------------------------------------------------------------#
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

#@property的getter函数名和setter装饰器 . 前面的名字和setter函数名保持一致
#@property修饰之后可以像属性一样调用函数
#可以设置制度属性(不设置setter方法)
#-------------------------------------------------------------------------------------------------------------------#
#多重继承
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
#-------------------------------------------------------------------------------------------------------------------#
# 定制类

    #__str__(),__repr__()
    #__str__()用来设置打印返回的字符串
    #__repr__()返回程序开发者看到的字符串(命令行直接输入实例显示的值  >>> s2)

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


    #__iter__(),next()
    #__iter__()用来返回迭代对象,这里就是其本身
    #  next()  返回迭代结果,设置迭代结束的条件

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


    #__getitem__()
    #定义用[]从对象中取值的方法

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

    #__getattr__()
    #当调用对象不存在的属性时,python解释器会试图调用__getattr__()方法,动态的返回属性(也可以返回方法)

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

    #__call__(),callable()
    #使类的实例对象可以调用(如>>> s=Student() >>> s() )
    #__call__()还可以添加参数
    #callable()可以判断使否是可调用对象
    #函数是可调用对象,设置了__call__()的类创建的实例也是可调用对象

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
#-------------------------------------------------------------------------------------------------------------------#
# 单例模式
#
    #共享此类的同一个类属性,此类属性即为类的对象
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


#-------------------------------------------------------------------------------------------------------------------#
#使用元类

    #使用type()创建类
    #可以动态的创建类
    #与用class创建类完全一致,python解释器在遇到class时也是扫描class的语法之后用type来构建类
    #格式为    type(类名,继承的父类(用tuple接收),用dict()将类中方法名和对应的函数名绑定)
    #定义类方法加上修饰器即可

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




    # metaclass(元类),可用于设计ORM框架
    #__new__()方法先创建实例,__new__()返回值就是实例对象,__init__()对实例进行初始化.
    # __new__()在创建实例之前,__init__()在创建实例之后.
    #__new__()方法是在创建实例前就存在的,所以其本身是个类方法,参数为__new__(cls,*args,**kwargs)

        #示例1:新建一个Mylist类继承List并添加一个功能同append()的add()方法
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





        #示例2:用元类实现一个ORM框架

            #步骤1:定义字段数据类型(StringField,IntegerField)
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

#************关于元类以及从代码创建对象的过程***************
"""
type类可以创建类,解释器也是通过type来创建类的.
由于type可以创建类,所以可以自己定义,动态的传入参数,自定义生成类的属性,方法
因此可以用于ORM,事先不知道创建的对象需要哪些属性

解释器创建对象的过程:
解释器先遍历一遍代码,然后在创建类时将此class代码的名字(如User),父类,和定义的属性方法传给其元类__metaclass__中的(自身没有在父类中找)__new__(cls,name,bases,attrs)方法的对应参数
__metaclass__的__new__方法创建出的对象是一个类(即class User),即可以使用这个产生的类中的__new__方法来创建此类的实例对象(即object user)
在__new__创建对象之后,调用__init__方法对此对象(object u)初始化赋值

"""

#-------------------------------------------------------------------------------------------------------------------#
#测试调试,单元测试暂略
#-------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------#

#IO编程
# IO即Input和Output,由于程序和运行时的数据时在内存中驻留,所以(从磁盘,网络等)进内存叫Input,出内存叫Output
#同步和异步的区别在于是否等待IO执行的结果


#文件读写
    #open,close
    #open的mode参数
    #   r:只读模式, r+:读写模式打开,  w:清空文件,不能用file.read方法,可以用来创建文件   w+:清空文件可以用file.read方法
    #   a:追加内容,不能用read方法    a+:追加内容,可以用read方法       rU:自动探测行尾符
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

    #with
    #形如: with obj as var
    #with是对try,except,finally的一种简化操作
    #使用要求:跟在with后的对象必须有__enter__()和__exit__()方法
    #1,__enter__(self)方法首先被执行,方法返回的值赋给as后的变量(var)
    #2,执行with obj as var下方的代码块
    #3,__exit__(self,type,value,trace)方法被调用,参数分别为异常的种类,描述和堆栈追踪
    #ps:第二步执行结束或抛出异常时都会执行__exit__函数,对资源进行清理或者关闭文件都可以放在__exit__函数中

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

    #读取编码问题,写文件
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

#-------------------------------------------------------------------------------------------------------------------#
#操作文件和目录-->os模块
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


#练习:遍历当前文件目录
#os.path.isdir(x)-->x是否为文件夹
#os.listdir(path)-->路径下所有文件&文件夹
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
#-------------------------------------------------------------------------------------------------------------------#
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
#-------------------------------------------------------------------------------------------------------------------#

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

#windows下用multiprocessing创建子进程
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

#进程池
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




#进程间通信
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
#-------------------------------------------------------------------------------------------------------------------#
#线程
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

#线程的锁
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

#多线程死循环只能占用160%cpu
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


#测试python的多线程速度
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

#-------------------------------------------------------------------------------------------------------------------#
#正则匹配身份证和电话
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