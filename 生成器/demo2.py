# 生成器函数进阶
# send获取下一个值的效果同__next__基本一致
# 只是在获取下一个值的时候，给上一个yield的位置传递一个数据
"""
使用send的注意事项:
    1、需在执行至少一次__next__之后才能使用
    2、最后一个yield不能获取到外部的值
"""


def generator():
    print(123)
    content = yield 1
    print(content)
    print(456)
    yield 2
    yield


g = generator()
print(g.__next__())
print(g.send('hello'))
print(g.send('hello'))