# 多个装饰器装饰同一个函数


def wrapper1(func):
    def inner(*args, **kwargs):
        print('before wrapper1')
        res = func(*args, **kwargs)
        print('after wrapper1')
        return res
    return inner


def wrapper2(func):
    def inner(*args, **kwargs):
        print('before wrapper2')
        res = func(*args, **kwargs)
        print('after wrapper2')
        return res
    return inner


@wrapper2
@wrapper1
def test():
    print('test')
    return 'i am test'


print(test())