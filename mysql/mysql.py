import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password="123456",
    database="stu",
    charset="utf8"
)

# 创建游标
cur = db.cursor()
# 数据库操作
cur.execute("insert into class values (6,'Levi',11,'m',98,'2019-01-01')")

# 数据库提交
db.commit()
# 关闭游标和数据库
cur.close()
db.close()
