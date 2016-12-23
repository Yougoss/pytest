#coding:utf-8
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return super(ModelMetaclass,cls).__new__(cls,name,bases,attrs)
        mappings={}
        for k,v in attrs.iteritems():
            if isinstance(v,Field):
                print 'Found Mapping: %s-->%s'%(k,v)
                mappings[k]=v
        for k in mappings.iterkeys():
            del attrs[k]

        attrs['__table__']=name
        attrs['__mappings__']=mappings
        return super(ModelMetaclass,cls).__new__(cls,name,bases,attrs)

class Model(object):
    __metaclass__ = ModelMetaclass
    d=dict()

    def __init__(self,**kwargs):
        for k in (k for k in kwargs if k in self.__mappings__):
            self.d[k]=kwargs[k]

    def save(self):
        fields=[]
        args=[]
        params=[]
        for k,v in self.d.iteritems():
            fields.append(k)
            if isinstance(self.__mappings__[k],StringField):
                v='"'+v+'"'
            elif isinstance(self.__mappings__[k],IntegerField):
                v=v
            args.append(str(v))

        sql='insert into %s (%s) value(%s)'%(self.__table__,','.join(fields),','.join(args))

        print sql



class Field(object):
    def __init__(self,name,datatype):
        self.name=name
        self.datatype=datatype
    def __str__(self):
        return '<%s:%s>'%(self.name,self.datatype)

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(255)')



# 此class的名字传进metaclass的name,Model传入bases参数,下面的属性和方法传进attrs(attrs默认包含一个__module__:__main__)
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')




# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()