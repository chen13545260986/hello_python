# 爬虫例子
import re
from urllib.request import urlopen


def getPage(url):
    response = urlopen(url)
    return response.read().decode('utf-8')


def parsePage(s):
    ret = re.findall(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
        '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', s, re.S)
    return ret


def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    response_html = getPage(url)
    ret = parsePage(response_html)
    print(ret)


count = 0
for i in range(10):  # 10页
    main(count)
    count += 25