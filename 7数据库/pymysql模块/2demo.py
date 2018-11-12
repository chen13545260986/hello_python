import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='x9_admin')

# 使用cursor()方法创建一个游标对象
cursor = conn.cursor()

# sql语句
sql = "insert into dy_bank_list (name,code) value ('ceshi','AAA')"

# 执行sql语句
cursor.execute(sql)

# 获取最近的一条记录的id
print(cursor.lastrowid)

# 增删改都需要commit操作
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()