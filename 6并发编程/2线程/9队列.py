import queue

# q = queue.Queue()  # 队列 先进先出
# q.put(1)
# print(q.get())
# q.put_nowait(2)
# print(q.get_nowait())

# q = queue.LifoQueue()  # 栈 先进后出
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())

q = queue.PriorityQueue()  # 优先级队列
q.put((20,'a'))
q.put((10,'b'))
q.put((30,'c'))
q.put((-5,'d'))
q.put((1,'?'))
print(q.get())