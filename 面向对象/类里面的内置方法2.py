"""
__new__:构造方法
__init__:初始化方法
__new__在__init__前执行
"""
class A:
    __instance = None

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(cls)
        return cls.__instance

a1 = A('pig', 18)
a2 = A('cat', 19)
print(a1)
print(a2)
print('=====')

"""
__eq__
"""
class B:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if self.__dict__ == other.__dict__:
            return True
        else:
            return False

b1 = B('dog')
b2 = B('dog')
print(b1 == b2)
print('=====')

"""
__hash__
"""
class C:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

c1 = C('dog')
c2 = C('dog')
print(hash(c1))
print(hash(c2))
print('=====')
