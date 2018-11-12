# 封装和@property
from math import pi


class Circle:
    def __init__(self,r):
        self.__r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self,new_r):
        self.__r = new_r

    @property
    def area(self):
        return self.__r**2*pi

# @property:用来装饰类里面的公共方法，使其可以通过：对象.方法名，来调用,而不需要加()
c1 = Circle(5)
print(c1.r)
print(c1.area)
print('======')
c1.r = 6
print(c1.r)
print(c1.area)
print('======')
