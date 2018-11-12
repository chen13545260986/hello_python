# 函数默认参数，重复调用会共享同一变量
def get_list(l=[]):
    l.append(1)
    return l


print(get_list())
print(get_list())
print(get_list())