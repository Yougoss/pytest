#coding:utf-8
from threading import RLock,current_thread
'''
thread_local思路:

    local对象自带一些属性:__lock锁,__dict__从中获取数据,__key保存当前实例的地址作为去线程对象里拿数据的key,__args保存参数

    local对象的属性读写删除都需要变为原子操作,即加锁.__setattr__,getattribute__,__delattr__,
    (__del__,从线程__dict__中删除保存threadlocal数据的键值对)

    需要一个方法_parse(),在对local对象属性操作的时候,从线程dict中把属性拿到当前local对象中

'''
'''
错误汇总:
1-使用self.name来获取和设置属性:
    例如:
    self._local__key = key
    self._local__args = (args,kwargs)
    self._local__lock = RLock()
    这会调用此对象的__setattr__,__getattribute__由于此对象的相关方法重写过
    所以有两种情况
    在__new__中,会在定义锁之前调用这两个方法,但这两个方法有需要找到锁,因此报错
    在这两个方法中,使用 self.name进行操作会递归的调用这两个方法,无限循环

    解决方法:
    self.name = value 等对对象属性的操作一律使用
    object.__setattr__(self, name, value)
    objece.__getattribute__(self, name)

'''




class _loal_base(object):

    __slots__ = ["_local__args", "_local__lock", "_local__key"]

    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls)
        key = str(id(self))

        # self._local__key = key
        # self._local__args = (args,kwargs)
        # self._local__lock = RLock()

        object.__setattr__(self,"_local__key",key)
        object.__setattr__(self,"_local__args",kwargs)
        object.__setattr__(self,"_local__lock",RLock())


        if (args or kwargs) and (cls.__init__ is object.__init__):
            raise TypeError("不支持传入参数")

        current_thread().__dict__[key] = object.__getattribute__(self,"__dict__")

        return self

def _parse(self):
    key = object.__getattribute__(self,"_local__key")
    d = current_thread().__dict__.get(key)

    if d is None:
        d = {}
        current_thread().__dict__[key] = d
        object.__setattr__(self, "__dict__",d )

        cls = type(self)
        if cls.__init__ is not object.__init__:
            args, kwargs = self._local__args
            cls.__init__(self, *args, **kwargs)
    else:
        object.__setattr__(self, "__dict__",d )



class local(_loal_base):
    def __getattribute__(self, item):
        lock = object.__getattribute__(self, "_local__lock")
        lock.acquire()
        try:
            _parse(self)
            return object.__getattribute__(self, item)
        finally:
            lock.release()

    def __setattr__(self, key, value):
        if key == "__dict__":
            raise AttributeError("%r __dict__属性只读")%self.__class__.__name__
        lock = self._local__lock
        lock.acquire()
        try:
            _parse(self)
            self.__dict__[key] = value
        finally:
            lock.release()



    def __delattr__(self, item):
        pass

    def __del__(self):
        pass

