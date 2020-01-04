"""
编写一个程序模拟注册和登录的过程
"""
import pymysql


def selete_memu():
    select_number = int(input("请选择: 1>>注册---2>>登录"))
    if select_number == 1:
        do_post()
    else:
        do_login()


def do_post():
    """
    注册函数
    :return:
    """
    user = input("请输入用户名:")
    password = input("请输入用户名密码:")
    # 用户不存在
    if not connect_select(user):
        if connect_insert(user, password):
            print("注册成功")
        else:
            print("注册失败")
    else:  # 数据库存在这个用户名
        print("用户名已存在")
        return


def do_login():
    """
    登录代码
    :return:
    """
    username = input("请输入用户名：")
    password = input("请输入用户名密码")
    connect_login(username, password)


def connect_login(username, password):
    """
    数据库连接--完成用户名查询功能
    :return:
    """
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password='123456',
        database='user',
        charset='utf8'
    )
    # 创建游标
    cur = db.cursor()
    # 查询数据库
    try:
        sql = "select username,password from users where username='%s'" % (username)
        cur.execute(sql)
    except:
        db.rollback()
        print("登录失败")
    # 查询结果
    data = cur.fetchone()
    # print(data)
    if password == data[1]:
        print("登录成功")
    else:
        print("登录失败")
    # 关闭游标和数据库
    cur.close()
    db.close()


def connect_select(username):
    """
    数据库连接--完成用户名查询功能
    :return:
    """
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password='123456',
        database='user',
        charset='utf8'
    )
    # 创建游标
    cur = db.cursor()
    # 查询数据库
    sql = "select * from users where username='%s'" % (username)
    cur.execute(sql)
    # 查询结果
    data = cur.fetchone()
    # 关闭游标和数据库
    cur.close()
    db.close()
    return data


def connect_insert(user, password):
    """
    数据库链接---完成数据库插入操作
    :param user:
    :param password:
    :return:
    """
    result = False
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password='123456',
        database='user',
        charset='utf8'
    )
    # 创建游标
    cur = db.cursor()
    # 插入数据库
    try:
        sql = "insert into users(username,password)values(%s,%s)"
        cur.execute(sql, (user, password))
        result = True
    except:
        db.rollback()
    # 提交数据库
    db.commit()
    # 关闭游标和数据库
    cur.close()
    db.close()
    # 返回插入结果
    return result


if __name__ == '__main__':
    selete_memu()
