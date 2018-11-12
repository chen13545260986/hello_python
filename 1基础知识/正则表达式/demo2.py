import re

# re下常用方法
# findall:返回所有满足匹配的结果放到一个列表中
# search：从前往后，找到一个就返回，返回的变量需要调用group方法才能拿到结果，如果没有找到，group方法会报错
# match:从头开始匹配，如果正则规则从头开始可以匹配上，就返回一个变量，返回的变量需要调用group方法才能拿到结果，如果没有找到，group方法会报错
str = 'eva egon yuan'
res1 = re.findall('[a-z]+', str)
print(res1)

res2 = re.search('a', str)
print(res2)
print(res2.group())

res3 = re.match('a', str)
res4 = re.match('e', str)
print(res3)
print(res4)
print(res4.group())

# sub:用于替换字符串中的匹配项
res5 = re.sub('a', '', str)
print(res5)

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
obj = re.compile('a')
res6 = obj.search(str)
print(res6.group())

# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
res7 = re.finditer('[a-z]+', str)
print(res7)
print([i.group() for i in res7])

# split 方法按照能够匹配的子串将字符串分割后返回列表
res8 = re.split(' ', str)
print(res8)