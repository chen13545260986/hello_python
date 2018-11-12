# 返回本地作用域中的所有名字
print(locals())
# 返回全局作用域中的所有名字
print(globals())

print(dir(range(1, 11, 2)))
# 判断range是不是迭代器
print('__next__' in dir(range(1, 11, 2)))

# 判断一个变量是否能被调用
a = 1
print(callable(a))
print(callable(print))

# 查看方法的用法
help(str)

print('我们的祖国是花园', end='i')  # 指定输出的结束符
print(1, 2, 3, 4, 5, sep='|')  # 指定输出多个值之间的分隔符

import time
# 打印进度条
for i in range(0,101,2):
     # time.sleep(0.1)
     char_num = i//2
     # \r回到行首
     per_str = '\r%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s' % (i,'*'*char_num)
     # flush:是否开启缓冲区
     print(per_str,end='', flush=True)

# progress_Bar：专业打印进度条的模块

# exec和eval都可以执行字符串类型代码，eval有返回值，exec没有返回值
# eval只能用在你明确知道要执行的代码是什么时
# eval适合处理有结果的简单计算
# exec适合处理简单的流程控制
eval('print(123)')
exec('print(123)')
print(eval('1+2+3'))
print(exec('1+2+3'))

code = '''
for i in range(5):
    print(i)
'''
compiles = compile(code, '', 'exec')
exec(code)

# 以绝对值的结果来取最大值
print(max(1,2,3,-4,key = abs))

# 让变量原封不动的输出
print(repr(1))
print(repr('1'))

# all可迭代对象里面全为真则True，否则为False
print(all([1, '', True]))
print(all([1, 'a', True]))
# any可迭代对象里面有一个为真则True，否则为False
print(any([1, '', True]))
print(any([1, 'a', True]))

# zip拉链方法
l1 = [1,2,3,4,5]
l2 = ['a','b','c','d']
for i in zip(l1,l2):
    print(i)


# filter:用特定的函数，处理一个可迭代的对象
def is_odd(x):
    return x % 2 == 1


res = filter(is_odd,[1,4,6,7,9,12,17])
print(res)
for i in res:
    print(i)


# map:用特定的函数，遍历一个可迭代的对象
res = map(abs,[-1,-3,-4,-5])
print(res)
for i in res:
    print(i)

# filter和map的区别
# filter只管筛选，不会改变原来的值
# map值可能发生改变

l = [4,1,6,-2,5]
l.sort()
print(l)
l.sort(key=abs)
print(l)
# sorted返回一个新的,不改变原来的，但是占内存
print(sorted(l))