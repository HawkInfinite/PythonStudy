# coding: utf-8

import codecs
import MySQLdb

# 将方法抽象,只需输入路径和表名即可执行sql语句,前提是路径正确及数据库和表名都存在


def insert_data(pathtotxt, tablename):
    # 初始化执行语句
    values = ""
    sql_cur = ""
    insert_cur = 'insert into name values("'
    insert_cur = insert_cur.replace('name', tablename)
    with codecs.open(pathtotxt, 'r', 'utf-8') as DeptFile:
        for line in DeptFile.readlines():
            #line = line.strip('\n')                        # 去除两端的换行符
            #values = values.replace(' ', '","')            # 找到数据中的空格并替换成","
            values = line.strip('\n').replace(' ', '","')   # 保存文档中的数据
            sql_cur = insert_cur + values + '")'            # 构成sql的执行语句
            # print (sql_cur)
            cur.execute(sql_cur)                      # 执行sql语句
            conn.commit()                             # 因为是增加操作,所以每次添加都要提交

if __name__ == '__main__':
    # 连接数据库
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        charset='utf8',
        db='university',
    )
    # 获取数据库执行游标
    cur = conn.cursor()
    # 执行方法
    insert_data("/home/infinite/Documents/第四次作业/university/department.txt", "department")
    insert_data("/home/infinite/Documents/第四次作业/university/student.txt", "student")
    insert_data("/home/infinite/Documents/第四次作业/university/exam.txt", "exam")
    # 关闭数据库
    cur.close()
