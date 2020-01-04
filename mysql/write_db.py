import pymysql

db = pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='123456',
    database='stu',
    charset='utf8'
)
# 创建游标
cur = db.cursor()
try:
    name = input("name:")
    age = input("age:")
    score = input("score:")
    sex=input("sex:")
    # time=input("time:")
    sql = "insert into class (name,age,sex,score) values ('%s',%s,'%s',%s)"%(name,age,sex,score)
    cur.execute(sql)
    # 数据库提交
    db.commit()
except Exception as e:
    db.rollback()  # 遇到问题回滚
    print(e)

# 关闭游标和数据库
cur.close()
db.close()
