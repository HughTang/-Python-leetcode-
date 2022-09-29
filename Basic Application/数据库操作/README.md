### 数据库操作
#### 1、python中的mysql库及连接方法
- mysql.connector驱动：MySQL官方提供的驱动器
```python
# pip安装方法
python -m pip install mysql-connector
```

```python
# 导包
import mysql.connector

# 获取MySQL数据库连接
mydb = mysql.connector.connect(
    host = 'localhost',    # 数据库主机地址
    user = 'root',         # 数据库用户名
    passwd = 'root',       # 数据库密码
    database = 'test'      # 要连接的数据库名（可缺省）
)

# 获取游标
mycursor = mydb.cursor()
```
```python
# 0、若database缺省，则需要先创建数据库
# 定义创建数据库的SQL语句
sql0 = "CREATE DATABASE test"

# 执行SQL语句
mycursor.execute(sql0)

# 提交当前事务
mydb.commit()
```

```python
# 1、定义创建表、插入数据、删除数据、修改数据、删除表、修改数据表名、修改数据表字段等的SQL语句
sql1 = "CREATE TABLE IF NOT EXISTS 表名 (name VARCHAR(255), grade INT)"
sql2 = "INSERT INTO 表名(name, grade) VALUES('Tom', 100)"
sql3 = "DELETE FROM 表名 WHERE grade < 60"
sql4 = "UPDATE 表名 SET grade = 99 WHERE name = 'Tom'"
sql5 = "DROP TABLE IF EXISTS 表名"

try:
    # 执行SQL语句
    mycursor.execute(sql1)
    mycursor.execute(sql2)
    mycursor.execute(sql3)
    mycursor.execute(sql4)
    mycursor.execute(sql5)

    # 提交当前事务
    mydb.commit()
except:
    # 若上述操作出错，则回滚事务
    mydb.rollback()
```

```python
# 2、批量插入数据
# 定义批量插入的SQL语句
sql6 = " INSERT INTO 表名(name, grade) VALUES(%s, %s)"

# 定义要插入数值的元组列表（注意：必须是元组列表）
val = [
  ('Tom', 100),
  ('Jeery', 95),
  ('Roin', 96),
  ('Stack', 80),
  ('Wang', 50),
]

try:
    # 使用executemany(sql: str, val: List(set))方法进行批量插入，第二个参数是数据的元组列表
    mycursor.executemany(sql6, val)

    # 提交当前事务
    mydb.commit()
except:
    # 若上述操作出错，则回滚事务
    mydb.rollback()
```

```python
# 3、定义显示数据库、显示数据表以及查询数据的SQL语句
sql7 = "SHOW DATABASES"
SQL8 = "SHOW TABLES"
sql9 = "SELECT COUNT(*) FROM 表名 WHERE grade > 80"
sql10 = "SELECT * FROM 表名"

# （1）fetchall()的使用
# 执行查询语句N+1
mycursor.execute(sql7)
# cursor.fetchall()获取查询结果的所有行，它将所有行作为元组列表返回。如果没有要获取的记录，则返回一个空列表。
result1 = mycursor.fetchall()

# （2）fetchmany(size)的使用
# 执行查询语句N+2
mycursor.execute(sql8)
# cursor.fetchmany(size)返回size参数指定的行数，当重复调用时，此方法获取查询结果的下一组行并返回元组列表。如果没有更多行可用，则返回一个空列表。
# 这里以size=3为例，则result2中存储了查询结果的前三条数据
result2 = mycursor.fetchall(3)

# （3）fetchone()的使用
# 执行查询语句N+3
mycursor.execute(sql9)
# cursor.fetchone()返回查询结果的最前面的一个记录，如果查询结果为空则返回None。
result3 = mycursor.fetchone()

# （4）fetchall()、fetchmany(size)、fetchone()的混合使用
# 执行查询语句N+4
mycursor.execute(sql10)
# result4保存的是查询数据的前2行结果（结果为保存元组数据的列表）
result4 = mycursor.fetchmany(2)
# result5保存的是弹出前2行结果之后，剩下结果数据的前1行结果（结果不为列表，直接为元组）
result5 = mycursor.fetchone()
# result6保存的是弹出前3行结果之后，剩下的所有结果数据（结果为保存元组数据的列表）
result6 = mycursor.fetchall()
# 由于查询结果全部被弹出，所以result7为空列表
result7 = mycursor.fetchmany(4)
# 由于查询结果全部被弹出，所以result8为None
result8 = mycursor.fetchone()
```

```python
# 关闭数据库连接
mydb.close()
```

- PyMySQL库：PyMySQL是在Python3.x版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。
```python
# pip3安装方法
pip3 install PyMySQL
```

```python
# 导包
import pymysql

# 获取MySQL数据库连接
mydb = pymysql.connect(
    host = 'localhost',    # 数据库主机地址
    user = 'root',         # 数据库用户名
    passwd = 'root',       # 数据库密码
    db = 'test',           # 要连接的数据库名（不可缺省）
    port = 3306,           # MySQL服务的端口号
    charset = 'utf8'      # 编码方式，不能写成utf-8
)

# 获取游标
mycursor = mydb.cursor()
# 之后的操作与mysql.connector驱动相同
......
```

> 参考网址1：https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/

> 参考网址2：https://blog.csdn.net/qq_38384924/article/details/100101754