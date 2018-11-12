# 生成器函数：惰性运算


# 只要含有yeild关键字的函数都是生成器函数
# yield不能和return共用，且需要写在函数内部
def generator():
    print(1)
    yield 'a'
    print(2)
    yield 'b'
    yield 'c'


# 生成器函数执行之后会得到一个生成器作为返回值
res = generator()
print(res)
# 执行生成器里面的代码
# print('first:', res.__next__())
# 再次执行生成器里面的代码
# print('second:', res.__next__())
# 第三次执行生成器里面的代码
# print('third:', res.__next__())

for i in res:
    print(i)
