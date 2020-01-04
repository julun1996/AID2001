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
    database="dict",
    charset='utf8'
)
#创建游标
cur=db.cursor()
sql = "insert into words (word,explanation) values (%s,%s)"
f=open("dict.txt")
for file in f:
    tupl=re.findall(r'(\S+)\s+(.*)',file)[0]
    print(tupl)
    # try:
    #     cur.execute(sql,tupl)
    #     db.commit()
    # except:
    #     db.rollback()




#关闭游标、数据库
cur.close()
db.close()