import requests
from multiprocessing import Pool

def get(url):
    res = requests.get(url)
    if res.status_code == 200:
        return url,res.content.decode('utf-8')

def call_back(args):
    url,content = args
    print(url,len(content))

if __name__ == '__main__':
    u = "http://www.baidu.com"
    # 创建进程池
    p = Pool(5)
    # 异步执行进程
    p.apply_async(get,args=(u,),callback=call_back)
    # 关闭进程池
    p.close()
    # 感知进程池中的进程的结束
    p.join()