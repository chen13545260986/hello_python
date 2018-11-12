# 面向对象的三大特性：继承，多态，封装


# 继承:减少了代码的重复。继承表达的是一种子类是父类的关系
class A:    # 父类
    pass


class B:
    pass


# 单继承
class Ason(A):  # 子类
    pass


# 多继承
class ABson(A,B):
    pass

print(ABson.mro())

# 单继承 ： 子类有的用子类 子类没有用父类
# 多继承中，我们子类的对象调用一个方法，默认是就近原则，找的顺序是什么？
# 经典类中 深度优先
# 新式类中 广度优先
# python2.7 新式类和经典类共存，新式类要继承object
# python3   只有新式类，默认继承object
# 经典类和新式类还有一个区别  mro方法只在新式类中存在
# super 只在python3中存在
# super的本质 ：不是单纯找父类 而是根据调用者的节点位置的广度优先顺序来的