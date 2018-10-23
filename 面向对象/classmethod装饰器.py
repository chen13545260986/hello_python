# @classmethod:把一个方法变成一个类中的方法，这个方法就可以直接被类调用，不需要依托任何对象
# 当这个方法的操作只涉及静态属性的时候，就应该使用@classmethod


class Goods:
    __discount = 0.5

    def __init__(self,name,price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price*self.__discount

    @classmethod
    def change_dis(cls,new_dis):
        cls.__discount = new_dis

    @staticmethod
    def welcome():
        print('welcome to buy fruits')

g1 = Goods('apple',5)
g2 = Goods('banana',2)
print(g1.price)
print(g2.price)
print('=====')
Goods.change_dis(0.8)
print(g1.price)
print(g2.price)
print('=====')


# @staticmethod:在完全面向对象的程序中，如果一个函数既和对象没有关系，也和类没有关系，那么就用@staticmethod将这个函数变成一个静态方法
# 用来将自定义函数放到类中,便于类来调用
Goods.welcome()

# 类方法和静态方法都是类调用的