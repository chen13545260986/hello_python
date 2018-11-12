import requests
from bs4 import BeautifulSoup

# 请求url获取内容
res = requests.get("https://b.faloo.com/y/0/0/0/0/0/0/1.html")
res.encoding = 'gbk'

# 用BeautifulSoup类处理成方便操作的对象
soup = BeautifulSoup(res.text, 'html.parser')

# 获取指定的标签
div_list = soup.find_all(name='div', attrs={'class': 'l_bar'})
for div in div_list:
    print(div.find(name='img').get('src'))