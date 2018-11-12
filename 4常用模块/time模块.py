# time模块

import time

# 浮点型时间
print(time.time())
# 字符串时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))
# 结构型时间
print(time.localtime())
print(time.mktime(time.localtime()))
print(time.strptime('2012-12-1', '%Y-%m-%d'))