# 装饰器形成的过程

# 装饰器的作用:在不修改函数的前提下，采用闭包函数的方法，增加函数功能
import time


# 装饰器函数
def get_func_exec_time(f):
    # *args:动态参数
    def inner(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print('执行时间:%d秒' % (end - start))
        return res
    return inner


# 语法糖: @装饰器函数名
@get_func_exec_time
# 被装饰的函数1
def func(a):
    time.sleep(1)
    return a


# 被装饰的函数1
def func2(a, b):
    time.sleep(1)
    return a + b


# func = get_func_exec_time(func)
# 调用被装饰的函数时，执行的是装饰器的内部函数
print(func(2))
print(func2(3, 4))

'''
原则：开发封闭原则
    开放：对扩展是开放的
    封闭：对修改是封闭的
'''


# 装饰器的固定模式,fun为被装饰的函数
def wrapper(fun):
    def inner(*args, **kwargs):
        # 在被装饰函数之前要做的事

        # 被装饰的函数
        res = fun(*args, **kwargs)

        # 在被装饰函数之后要做的事
        return res
    return inner
