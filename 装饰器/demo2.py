# 装饰器进阶
#   functools.wraps
from functools import wraps


def wrapper(func):
    @wraps(func)    # 将函数的属性__name__改为被装饰的函数的__name__
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return inner


@wrapper
def holiday():
    return '放假了'


print(holiday())
print(holiday.__name__)