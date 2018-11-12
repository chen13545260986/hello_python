"""
反射:是用字符串类型的名字去操作变量
"""

"""反射对象中的属性和方法"""
# class A:
#     def fun(self):
#         print('is func')
#
# a = A()
# a.name = 'hello'
# name = input('>>>')
# if hasattr(a,name):
#     print(getattr(a,name))
# else:
#     print('attr is not exist')

"""反射类中的属性和方法"""
# class B:
#     name = 'B'
#
#     def func_B(self):
#         print('is func_B')
#
# name = input('>>>')
# if hasattr(B,name):
#     print(getattr(B,name))
# else:
#     print('attr is not exist')

"""反射模块中的属性和方法"""
# import my_module
# name = input('>>>')
# if hasattr(my_module,name):
#     print(getattr(my_module,name))
# else:
#     print('attr is not exist')

"""反射内置模块中的属性和方法"""
# import time
# name = input('>>>')
# if hasattr(time,name):
#     print(getattr(time,name))
# else:
#     print('attr is not exist')

"""反射自己模块中的变量和方法"""
# year = 2018
#
# def hello():
#     print('hello world')
#
# import sys
# name = input('>>>')
# if hasattr(sys.modules[__name__],name):
#     print(getattr(sys.modules[__name__],name))
# else:
#     print('attr is not exist')

"""
setattr
delattr
"""
class C:
    pass

c = C()
setattr(c,'name','hello')
setattr(C,'name','world')
print(c.name)
print(C.name)
print('=====')
delattr(c,'name')
print(c.name)   # 删除对象里面的属性后，默认会去读类里面的属性
delattr(C,'name')
print(C.name)
