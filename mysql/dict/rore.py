"""
将单词传入words数据表中
"""
import pymysql

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
# with open("dict.txt") as f:
f=open("dict.txt")
for file in f:
    # 此时file是字符串
    list_word = file.split(" ")  # 根据空格将字符串切割成列表
    # 单词
    words = list_word[0]
    # print(words)
    # 单词解释
    words_explantion = " ".join(list_word[1:]).strip()
    # print(words_explantion)
    try:
        sql="insert into words (word,explanation) values (%s,%s)"
        cur.execute(sql,(words,words_explantion))
        # 提交到数据库
        db.commit()
    except:

        db.rollback()


#关闭游标、数据库
cur.close()
db.close()