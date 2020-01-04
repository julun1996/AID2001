import pymysql

db = pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='123456',
    database="stu",
    charset='utf8'
)

# 创建游标
cur = db.cursor()
# 数据库操作
sql = "select * from class where sex='m' "
cur.execute(sql)
# 获取查询结果
one_row = cur.fetchone()
print(one_row)  # 元组

many_row = cur.fetchmany(2)  # 接着上一个语句后面继续输出
print(many_row)

# 关闭游标
cur.close()
# 关闭数据库
db.close()
