# 管道
# 数据的共享 Manager dict list
# 进程池
    # cpu个数+1
    # ret = map(func,iterable)
        # 异步 自带close和join
        # 所有结果的[]
    # apply
        # 同步的:只有当func执行完之后,才会继续向下执行其他代码
        # ret = apply(func,args=())
        # 返回值就是func的return
    # apply_async
        # 异步的:当func被注册进入一个进程之后,程序就继续向下执行
        # apply_async(func,args=())
        # 返回值 : apply_async返回的对象obj
        #          为了用户能从中获取func的返回值obj.get()
        # get会阻塞直到对应的func执行完毕拿到结果
        # 使用apply_async给进程池分配任务,
        # 需要先close后join来保持多进程和主进程代码的同步性