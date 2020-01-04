"""
将单词传入words数据表中
"""
import pymysql
import re

# 创建数据库对象
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="stu",
    charset='utf8'
)
# 创建游标
cur = db.cursor()

# with open("image.jpg", 'rb') as f:
#     data = f.read()
# try:
#     sql = "insert into images values (1,'jd',%s)"
#     cur.execute(sql, [data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 提取图片
sql = "select name from class "
cur.execute(sql)

data = cur.fetchmany(3)
print(data)
# with open("gg.jpg", 'wb')as f:
#     f.write(data[0])



# 关闭游标、数据库
cur.close()
db.close()
