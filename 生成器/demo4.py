# 各种推导式: 生成器，列表，集合，字典
"""
    遍历操作
    筛选操作
"""

# 1、列表推导式

# 30以内所有能被3整除的数的平方
l1 = [i * i for i in range(30) if i % 3 == 0]
print(l1)

# 找嵌套列表中名字含有两个e
names = [
    ['tom', 'billy', 'jefferson', 'andrew', 'wesley', 'steven', 'joe'],
    ['alice', 'jill', 'ann', 'jennifer', 'sherry', 'eva']
]
l2 = [name for lst in names for name in lst if name.count('e') == 2]
print(l2)

# 2、字典列表式

# 例一：将一个字典的key和value对调
d1 = {'a': 10, 'b': 20}
d2 = {d1[key]: key for key in d1.keys()}
print(d2)

# 例二：合并字典中大小写键的值为小写
d3 = {'a': 10, 'b': 20, 'A': 30, 'B': 40}
d4 = {key.lower(): d3.get(key.lower(), 0) + d3.get(key.upper(), 0) for key in d3}
print(d4)

# 3、集合推导式(集合有去重性，相当于一种特殊的列表)

# 集合中值的平方
s1 = {1, -1, 2}
s2 = {i**2 for i in s1}
print(s2)
