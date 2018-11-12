import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='x9_admin')

# 使用cursor()方法创建一个游标对象
cursor = conn.cursor()

# 执行sql语句
sql = "select * from dy_user where phone=%s"
# sql = "select * from dy_user where phone=%s" % '13545260986'
# cursor.execute(sql)
# 为了防止sql注入，不要自己拼接字符串，按如下方式
cursor.execute(sql,'13545260986')

# 增删改操作需要commit
# conn.commit()

# 获取结果(二维元组)
# res = cursor.fetchall()
# 获取结果(一维元组)
res = cursor.fetchone()
print(res)

# 关闭连接，cursor对象
cursor.close()
conn.close()