#coding:utf-8
"""Thread-local objects.

(Note that this module provides a Python version of the threading.local
 class.  Depending on the version of Python you're using, there may be a
 faster one available.  You should always import the `local` class from
 `threading`.)

Thread-local objects support the management of thread-local data.
If you have data that you want to be local to a thread, simply create
a thread-local object and use its attributes:

  >>> mydata = local()
  >>> mydata.number = 42
  >>> mydata.number
  42

You can also access the local-object's dictionary:

  >>> mydata.__dict__
  {'number': 42}
  >>> mydata.__dict__.setdefault('widgets', [])
  []
  >>> mydata.widgets
  []

What's important about thread-local objects is that their data are
local to a thread. If we access the data in a different thread:

  >>> log = []
  >>> def f():
  ...     items = mydata.__dict__.items()
  ...     items.sort()
  ...     log.append(items)
  ...     mydata.number = 11
  ...     log.append(mydata.number)

  >>> import threading
  >>> thread = threading.Thread(target=f)
  >>> thread.start()
  >>> thread.join()
  >>> log
  [[], 11]

we get different data.  Furthermore, changes made in the other thread
don't affect data seen in this thread:

  >>> mydata.number
  42

Of course, values you get from a local object, including a __dict__
attribute, are for whatever thread was current at the time the
attribute was read.  For that reason, you generally don't want to save
these values across threads, as they apply only to the thread they
came from.

You can create custom local objects by subclassing the local class:

  >>> class MyLocal(local):
  ...     number = 2
  ...     initialized = False
  ...     def __init__(self, **kw):
  ...         if self.initialized:
  ...             raise SystemError('__init__ called too many times')
  ...         self.initialized = True
  ...         self.__dict__.update(kw)
  ...     def squared(self):
  ...         return self.number ** 2

This can be useful to support default values, methods and
initialization.  Note that if you define an __init__ method, it will be
called each time the local object is used in a separate thread.  This
is necessary to initialize each thread's dictionary.

Now if we create a local object:

  >>> mydata = MyLocal(color='red')

Now we have a default number:

  >>> mydata.number
  2

an initial color:

  >>> mydata.color
  'red'
  >>> del mydata.color

And a method that operates on the data:

  >>> mydata.squared()
  4

As before, we can access the data in a separate thread:

  >>> log = []
  >>> thread = threading.Thread(target=f)
  >>> thread.start()
  >>> thread.join()
  >>> log
  [[('color', 'red'), ('initialized', True)], 11]

without affecting this thread's data:

  >>> mydata.number
  2
  >>> mydata.color
  Traceback (most recent call last):
  ...
  AttributeError: 'MyLocal' object has no attribute 'color'

Note that subclasses can define slots, but they are not thread
local. They are shared across threads:

  >>> class MyLocal(local):
  ...     __slots__ = 'number'

  >>> mydata = MyLocal()
  >>> mydata.number = 42
  >>> mydata.color = 'red'

So, the separate thread:

  >>> thread = threading.Thread(target=f)
  >>> thread.start()
  >>> thread.join()

affects what we see:

  >>> mydata.number
  11

>>> del mydata
"""

__all__ = ["local"]

# We need to use objects from the threading module, but the threading
# module may also want to use our `local` class, if support for locals
# isn't compiled in to the `thread` module.  This creates potential problems
# with circular imports.  For that reason, we don't import `threading`
# until the bottom of this file (a hack sufficient to worm around the
# potential problems).  Note that almost all platforms do have support for
# locals in the `thread` module, and there is no circular import problem
# then, so problems introduced by fiddling the order of imports here won't
# manifest on most boxes.

class _localbase(object):
    __slots__ = '_local__key', '_local__args', '_local__lock'

    def __new__(cls, *args, **kw):
        self = object.__new__(cls)
        key = '_local__key', 'thread.local.' + str(id(self))
        #给此类实例添加属性_local__key，_local__args，_local__lock
        object.__setattr__(self, '_local__key', key)
        object.__setattr__(self, '_local__args', (args, kw))
        object.__setattr__(self, '_local__lock', RLock())

        #(args or kw)判断创建cls(即local)的实例时是否有参数
        #(cls.__init__ is object.__init__)判断cls(即local)是否重写了__init__方法
        #即此句意思为如果有参数，并且没有覆写__init__方法时抛出不支持初始化参数的方法
        if (args or kw) and (cls.__init__ is object.__init__):
            raise TypeError("Initialization arguments are not supported")

        # We need to create the thread dict in anticipation of
        # __init__ being called, to make sure we don't call it
        # again ourselves.
        #拿到对象的__dict__属性,__dict__属性会保存当前对象的部分属性（obj.name = value 赋值的都会放进对象的__dict__中）
        dict = object.__getattribute__(self, '__dict__')
        #在当前线程对象(即创建此实例的线程)的__dict__中存入 {此实例的id:此实例的__dict__} 的键值对
        current_thread().__dict__[key] = dict

        return self

def _patch(self):
    #将键值对从线程的__dict__中取出，存入local实例的__dict__中
    key = object.__getattribute__(self, '_local__key')
    d = current_thread().__dict__.get(key)
    #对于那些第一次访问ThreadLocal变量的线程来说，需要创建一个空的字典来保存私有数据，然后还要调用该变量的初始化函数。
    if d is None:
        d = {}
        current_thread().__dict__[key] = d
        object.__setattr__(self, '__dict__', d)

        # we have a new instance dict, so call out __init__ if we have
        # one
        cls = type(self)
        #如果覆写了__init__方法，则需要重新用参数初始化
        if cls.__init__ is not object.__init__:
            args, kw = object.__getattribute__(self, '_local__args')
            cls.__init__(self, *args, **kw)
            pass
    #非第一次访问
    else:
        #把current_thread().__dict__中的键值对赋值给当前local实例的__dict__中
        object.__setattr__(self, '__dict__', d)

class local(_localbase):
    def __getattribute__(self, name):
        lock = object.__getattribute__(self, '_local__lock')
        lock.acquire()
        try:
            _patch(self)
            return object.__getattribute__(self, name)
        finally:
            lock.release()

    def __setattr__(self, name, value):
        #实例的__dict__为只读，不能修改
        if name == '__dict__':
            raise AttributeError(
                "%r object attribute '__dict__' is read-only"
                % self.__class__.__name__)
        lock = object.__getattribute__(self, '_local__lock')
        lock.acquire()
        try:
            #使当前实例的__dict__指向current_thread().__dict__
            _patch(self)
            #把当前设置的键值对保存在实例的__dict__中
            return object.__setattr__(self, name, value)
        finally:
            lock.release()

    def __delattr__(self, name):
        if name == '__dict__':
            raise AttributeError(
                "%r object attribute '__dict__' is read-only"
                % self.__class__.__name__)
        lock = object.__getattribute__(self, '_local__lock')
        lock.acquire()
        try:
            _patch(self)
            return object.__delattr__(self, name)
        finally:
            lock.release()

    def __del__(self):
        import threading

        key = object.__getattribute__(self, '_local__key')

        try:
            # We use the non-locking API since we might already hold the lock
            # (__del__ can be called at any point by the cyclic GC).
            threads = threading._enumerate()
        except:
            # If enumerating the current threads fails, as it seems to do
            # during shutdown, we'll skip cleanup under the assumption
            # that there is nothing to clean up.
            return

        for thread in threads:
            try:
                __dict__ = thread.__dict__
            except AttributeError:
                # Thread is dying, rest in peace.
                continue

            if key in __dict__:
                try:
                    del __dict__[key]
                except KeyError:
                    pass # didn't have anything in this thread

from threading import current_thread, RLock
