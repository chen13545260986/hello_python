# 对于不可变数据类型，类变量最好用类操作
# 对于可变数据类型，修改是共享的，重新赋值是独立的


class Foo:
    a = 0

    def __init__(self, *args):
        self.b = args[0]
        self.c = args[1]

    def test(self):
        print(Foo.a)
        print(self.a)
        print(self.b)
        print(self.c)

f1 = Foo(1,2)
f2 = Foo(3,4)
f1.test()
f2.test()
print('======')
f1.a = 5
f2.a = 6
f1.test()
f2.test()
print('======')
Foo.a = 7
f1.test()
f2.test()