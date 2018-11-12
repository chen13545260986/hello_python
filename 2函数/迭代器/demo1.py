# 迭代器

# 只要是含有__iter__方法的都是可迭代的---可迭代协议
# 迭代器协议：内部含有__next__和__iter__方法的就是迭代器
"""
迭代器的好处：
    1、一个一个的取值
    2、节省内存空间
"""

l = [1, 2, 3]
# 这是迭代器
iterator = l.__iter__()

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
