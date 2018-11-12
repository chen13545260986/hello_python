# 生成器里面的元素只能使用一次，取完就消失
# 生成器在使用时才执行


def demo():
    for i in range(5):
        yield i


g = demo()

g1 = (i for i in g)
g2 = (i for i in g)

print(list(g1))
print(list(g2))