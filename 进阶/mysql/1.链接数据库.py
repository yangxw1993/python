import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", port=3306, user="root", password="", database="python_db", charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
list1 = cursor.execute("SELECT * FROM student")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

for item in range(list1):
    result = cursor.fetchone()
    print(result)

# 关闭数据库连接
db.close()