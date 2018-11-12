"""
3协程：能够在一个线程中实现并发效果的概念
    能够规避一些任务中的IO操作
    在任务的执行过程中，检测到IO就切换到其他任务
"""

"""
爬虫的例子
"""
from urllib.request import urlopen
from gevent import monkey
monkey.patch_all()
import gevent

def get_url(url):
    res = urlopen(url)
    content = res.read().decode('utf-8')
    return len(content)

g1 = gevent.spawn(get_url,'http://www.baidu.com')
g2 = gevent.spawn(get_url,'http://www.hao123.com')
g3 = gevent.spawn(get_url,'http://www.taobao.com')
gevent.joinall([g1,g2,g3])
print(g1.value)
print(g2.value)
print(g3.value)