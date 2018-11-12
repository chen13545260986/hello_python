# 生成器表达式和列表推导式

# 列表推导式
l = ['鸡蛋%d' % i for i in range(10)]
print(l)

# 生成器表达式
g = (i for i in range(10))
print(g)

for i in g:
    print(i)

g2 = (i*i for i in range(10))

for i in g2:
    print(i)
"""
区别：
    1、括号不一样
    2、返回值不一样,生成器表达式几乎不占用内存
"""