# 实例要求：
# 读取data.txt中的数据，并将数据插入到数据库表中，并找出grade列中100出现的次数
# 考察点：文件读取、数据库连接、数据表插入、数据表查询

import mysql.connector


# 数据库连接
def connect():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database = 'test'
    )
    return mydb

# 读取文件
def read_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        data = list()
        for line in f.readlines():
            # 去掉列表中每一个元素的换行符
            line = line.strip('\n')  
            # 分割数据
            ls = line.split(',')
            # 调整数据格式
            ls[1] = int(ls[1])
            # 改为SQL可批量插入的元组格式
            data.append(tuple(ls))
    return data

if __name__ == '__main__':
    # 读数据文件
    data = read_file('C:/Users/16052/Desktop/TH/leetcode/Basic Application/实例1/data.txt')
    # 获取数据库连接
    mydb = connect()
    # 获取游标
    mycursor = mydb.cursor()
    # 建表
    sql1 = "CREATE TABLE IF NOT EXISTS student (name VARCHAR(255), grade INT)"
    # 插入数据
    sql2 = "INSERT INTO student(name, grade) VALUES(%s, %s)"
    # 查询grade为100的人数
    sql3 = "SELECT count(*) from student where grade=100"
    # 查询所有数据
    sql4 = "SELECT * from student"

    try:
        # 执行建表
        mycursor.execute(sql1)
        # 使用executemany批量插入数据
        mycursor.executemany(sql2, data)
        # 提交当前事务
        mydb.commit()
    except:
        mydb.rollback()
    
    # 执行查询grade为100的人数
    mycursor.execute(sql3)
    # 利用fetchall获取该查询结果的全部数据（结果为保存元组数据的列表）
    result1 = mycursor.fetchall()
    
    # 执行查询所有数据
    mycursor.execute(sql4)
    # 这里测试的是fetchall与fetchmany的区别和联系
    # result2保存的是查询数据的前2行结果（结果为保存元组数据的列表）
    result2 = mycursor.fetchmany(2)
    # result3保存的是弹出前2行结果之后，剩下结果数据的前1行结果（结果不为列表，直接为元组）
    result3 = mycursor.fetchone()
    # result4保存的是弹出前3行结果之后，剩下的所有结果数据（结果为保存元组数据的列表）
    result4 = mycursor.fetchall()
    # 由于查询结果全部被弹出，所以result5为空列表
    result5 = mycursor.fetchmany(1)
    # 由于查询结果全部被弹出，所以result7为None
    result6 = mycursor.fetchone()


    # 打印结果
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)


    # 关闭数据库连接
    mydb.close()