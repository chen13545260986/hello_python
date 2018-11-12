"""
同步:提交一个任务之后要等待这个任务执行完毕
异步:只管提交任务,不等待这个任务执行完毕就可以做其他事情
阻塞的有： recv recvfrom accept

IO多路复用
    select机制:Windows和linux上都有，都是操作系统轮询每一个被监听的项,看是否有读操作
    poll机制:只有linux上有，它可以监听的对象比select机制可以监听的多
        select和poll的共同点：随着监听项的增多,导致效率降低
    epoll机制：只有linux上有
"""









