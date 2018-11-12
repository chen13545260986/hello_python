# 带参数的装饰器
import time

FLAG = False


def timer_out(flag):
    def timer(func):
        def inner(*args, **kwargs):
            # 判断是否要打印程序执行时间
            if flag:
                start = time.time()
                res = func(*args, **kwargs)
                end = time.time()
                print('程序执行了%d秒' % (end - start))
            else:
                res = func(*args, **kwargs)

            return res
        return inner
    return timer


@timer_out(FLAG)
def test():
    time.sleep(1)
    return 'i am test'


print(test())