# 生成器在使用时才执行


def add(a, b):
    return a + b


def generator():
    for i in range(5):
        yield i


g = generator()

for i in [1, 10]:
    g = (add(i, j) for j in g)

"""
    i = 1
    g = (add(i, j) for j in g)
    i = 10
    g = (add(i, j) for j in (add(i, j) for j in g))
    g = (add(10, j) for j in (add(10, j) for j in (0, 1, 2, 3, 4)))
"""

print(list(g))