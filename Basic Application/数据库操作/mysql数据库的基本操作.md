# mysql数据库的基本操作
## 1、基本常识：

**表格组成**：
- 表头(header): 每一列的名称（第一行），由字段1，字段2，…字段n组成；
- 列(col): 具有相同数据类型的数据的集合；
- 行(row): 每一行用来描述某条记录的具体信息;值(value)：行的具体信息, 每个值必须与该列的数据类型相同；
- 键(key)： 键的值在当前列中具有唯一性。 

**主键**：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。 

**外键**：外键用于关联两个表。 

**复合键**：复合键（组合键）将多个列作为一个索引键，一般用于复合索引。

**SQL语言的分类**

**（1）数据定义语言（DDL）：后面需要加“TABLE 表名”**
- CREATE：创建表以及其他的对象结构；
- ALTER：修改表；
- DROP：删除表结构；
- TRUNCATE：删除表中的数据，删除表中全部数据。

**（2）数据操作语言（DML）：后面只需要加“表名”，不用加TABLE**
- INSERT：将数据插入到表中；
- UPDATE：修改表中数据；
- DELETE：删除表中数据。

**（3）数据查询语言（DQL）：后面只需要加“表名”，不用加TABLE**
- SELECT：查询表中数据。

**（4）数据控制语言（DCL）**
- GRANT 权限 ON 表名 TO 用户：授予权限；
- REOVOKE：收回权限；
- CREATE USER：创建用户。

**（5）事务控制语言（TCL）**
- COMMIT：提交； 
- ROLLBACK：回滚。

## 2、连接和管理mysql数据库

**（1）命令行操作连接mysql**

如果我们要登录本机的 MySQL 数据库，只需要输入以下命令即可：

```
mysql -u root -p
```

按回车确认, 如果安装正确且 MySQL 正在运行, 会得到以下响应: Enter password: 

**（2）使用python脚本连接mysql** 

使用 mysql-connector，它是 MySQL 官方提供的驱动器。这样便连接了mysql数据库。注意：创建数据库连接的时候，如果直接连接某个数据库（可添加参数database=数据库名）。

```python
import mysql.connector
mydb = mysql.connector.connect( 
	host="localhost", # 数据库主机地址 
	user="yourusername", # 数据库用户名 
	passwd="yourpassword" # 数据库密码 
) 
```

**（3）管理mysql**
- **SHOW DATABASES**：列出 MySQL 数据库管理系统的数据库列表。
- **USE 数据库名**：选择要操作的Mysql数据库，使用该命令后所有Mysql命令都只针对该数据库。
- **SHOW TABLES**：显示某数据库的所有表。
- **SHOW COLUMNS FROM 数据表名**：显示数据表有哪些属性（表头），属性的数据类型，是否为主键 ，是否为 NULL，默认值等。
- **SHOW INDEX FROM 数据表名**：显示数据表详细的索引信息，包括PRIMARY KEY（主键）。 

**（4）为某数据库添加mysql用户的两种方法**：

```sql
/* 方法1 */
use 数据库名; 
INSERT INTO user(host, user, password, select_priv, insert_priv, update_priv) VALUES('localhost', 'guest', MD5('guest123'), 'Y', 'Y', 'Y');
-- 刷新后重新载入授权表
FLUSH PRIVILEGES;
-- 查看guest的用户信息
SELECT host, user, password FROM user WHERE user = 'guest';
```

```sql
/* 方法2 */
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP 
	ON TUTORIALS.* 
	TO 'zara'@'localhost' 
	IDENTIFIED BY 'zara123';
```
> 更多DCL相关语句，可见网址：http://c.biancheng.net/mysql/100/

## 3、数据定义语言（Data Definition Language，DDL）

DDL主要是对数据库及数据表进行操作，关键字如下：
- **CREATE**：创建数据库、数据表以及其他的对象结构；
- **DROP**：删除数据库、数据表；
- **ALTER**：修改数据表名/表字段；

### 3.1 数据库

**（1）创建数据库**
```sql
CREATE DATABASE 数据库名;
```

**（2）删除数据库**

```sql
DROP DATABASE 数据库名;
```

### 3.2 数据表

**（1）创建数据表**

创建MySQL数据表需要以下信息： 数据表名，属性名，定义每个属性的数据类型，定义主键等。

**语法**
```sql
CREATE TABLE 数据表名 (表头名 对应数据类型);
```
```sql
CREATE TABLE 数据表名( 
	id INT NOT NULL AUTO_INCREMENT, 
	title VARCHAR(100) NOT NULL, 
	author VARCHAR(40) NOT NULL, 
	submission_date DATE, 
	PRIMARY KEY (id)     /*定义主键*/
)
```

**（2）主键设置**

创建表的时候我们一般都会设置一个主键（PRIMARY KEY）。我们可以使用“**INT AUTO_INCREMENT PRIMARY KEY**”语句来创建一个主键，主键起始值为1，逐步递增。 

**①在创建表的过程中定义主键**

```sql
CREATE TABLE 数据表名(
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(255), 
	url VARCHAR(255)
)
```

**②在表创建之后再添加主键**

```sql
ALTER TABLE 数据表名 ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY
```

**（3）删除数据表**

```sql
DROP TABLE 数据表名;
```

**（4）删除表中的全部数据（但不删除表结构）**

```sql
TRUNCATE TABLE 数据表名;
```
或
```sql
DELETE FROM 数据表名;
```

**（5）创建临时表**

临时表只在当前连接可见，当关闭连接时，MySQL会自动删除表并释放所有空间。

```sql
CREATE TEMPORARY TABLE 数据表名（...）;
```
**（6）查看数据表信息**
- 查看数据表结构
```sql
DESC 数据表名;
或
SHOW COLUMNS FROM 数据表名;
```

- 查看数据表详细信息：表名、存储引擎、版本号、数据长度、创建时间等。
```sql
SHOW TABLE STATUS LIKE '数据表名';
```
**（7）复制数据表**

完整地复制旧数据表到新数据表，包括表的结构，索引，默认值等，步骤如下：
- 执行`SHOW CREATE TABLE 旧表名;`语句来获取旧数据表的创建语句。
- 复制结果语句，并将其中的旧表名改为新表名，再执行修改后的语句，将完全的复制数据表结构到新表。
- 执行`INSERT INTO 新表名（字段）SELECT 字段 FROM 旧表名;`语句来实现旧表中数据的复制。

**（8）ALTER修改命令**

用来修改数据表名或者修改数据表字段。 

①**修改表名、类型**：

```sql
ALTER TABLE 旧表名 RENAME TO 新表名;
ALTER TABLE 表名 ENGINE = MYISAM;
```

**②删除，添加或修改表字段**：

```sql
/* 1.删除和修改字段 */
/* 删除字段1 */
ALTER TABLE 表名 DROP 字段1; 
/* 添加字段2，并设置数据类型。默认添加到结尾，若需指定，则在语句结尾加上：关键字FIRST(设定位第一列)或者 AFTER 字段名（设定位于某个字段之后） */
ALTER TABLE 表名 ADD 字段2 INT; 

/* 2.修改字段类型及名称 */
/* modify只能修改字段类型，不能修改字段名称 */
ALTER TABLE 表名 MODIFY 字段3 CHAR(10);
/* change可以同时修改字段类型与字段名称 */
ALTER TABLE 表名 CHANGE 字段2 新字段名 BIGINT;

/* 3.指定、修改和删除字段默认值 */
/* 指定字段是否为空，若不为空则还可以设置其默认值 */
ALTER TABLE 表名 MODIFY 字段5 BIGINT NOT NULL DEFAULT 100;
/* 修改字段默认值 */
ALTER TABLE 表名 ALTER 字段4 SET DEFAULT 1000;
/* 删除字段默认值 */
ALTER TABLE 表名 ALTER 字段4 DROP DEFAULT;	
```

## 4、数据操作语言（Data Manipulation Language，DML）

DML主要是对数据表中的数据进行插入、修改或删除，关键字如下：
- INSERT：将数据插入到表中；
- UPDATE：修改表中数据；
- DELETE：删除表中数据。

### 4.1 INSERT插入数据
MySQL表中使用 INSERT INTO 语句来插入属性值数据，如果属性值是字符型，则需要使用单引号或者双引号，例如“value”。通用的 INSERT INTO SQL语法如下：
```sql
INSERT INTO 数据表名 (字段1, 字段2,...字段N) VALUES (字段1的值, 字段2的值,...字段N的值);
```

**插入数据示例**：

```sql
INSERT INTO 数据表名 (title, author, date) VALUES ("学习 PHP", "菜鸟教程", NOW());  
INSERT INTO 数据表名 (title, author, date) VALUES ("JAVA 教程", "RUNOOB.COM", '2016-05-06'); 
```
在以上实例中，我们并没有提供 id 的属性数据，因为我们在创建表的时候，已经将该字段的属性值设为 `AUTO_INCREMENT`(自动增加) ，所以该字段会自动递增而不需要我们去设置。此外，实例中 `NOW()` 是一个 MySQL 函数，该函数返回日期和时间。 

**Python批量插入数据**

批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据：
```python
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)" 
val = [ 
	('Google', 'https://www.google.com'), 
	('Github', 'https://www.github.com'), 
	('Taobao','https://www.taobao.com'), 
	('stackoverflow', 'https://www.stackoverflow.com/') ]
try:
	mycursor.executemany(sql, val)
	mydb.commit()
except:
	mydb.rollback()
```
如果插入某行数据后，想要获得该数据记录的id，可以使用mycursor.lastrowid得到。

### 4.2 UPDATE修改数据

UPDATE 命令修改 MySQL 数据表数据，也就是修改字段对应的属性值，where条件可以控制修改哪条记录或其他条件。

```sql
UPDATE 数据表名 SET 字段1=新属性值1, 字段2=新属性值2 [WHERE Clause]
```
**修改数据举例**
```sql
UPDATE employee SET salay=8000 WHERE name='jack';
UPDATE employee SET salay=5000, job='AAAA' WHERE name='jack';
```

### 4.3 DELETE删除数据

DELETE FROM 命令来删除数据表中的记录，其中where条件可以控制哪条记录，或者符合哪些条件的记录，若无where条件则删除所有记录。
```sql
DELETE FROM 数据表名 [WHERE Clause]
```
**删除数据举例**
```sql
/* 删除表中所有记录 */
DELETE FROM employee;
/* 删除姓名为rose的所有记录 */
DELETE FROM employee WHERE name='rose';
```

## 5、数据查询语言（Data Query Language，DQL）

- SELECT：查询数据表中的数据，其语法如下：

```sql
SELECT 字段1,字段2 FROM 数据表名1, 数据表名2 [WHERE Clause] [LIMIT N] [OFFSET M]
```
- 查询语句中可以查询一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。
- SELECT 命令可以读取一条或者多条记录。
- 可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有属性的数据。
- 可以使用 LIMIT 属性来设定返回的记录数。
- 你可以通过OFFSET指定SELECT语句开始查询的数据偏移量，默认情况下偏移量为0。 
- LIMIT基本语法：
```
SELECT * FROM table LIMIT [offset,] rows | rows OFFSET offset;
```
如果只给定一个参数，表示记录数。
```
// 检索前5条记录(1-5)
SELECT * FROM orange LIMIT 5;
```     
相当于
```
// 两个参数，第一个参数表示offset, 第二个参数为记录数。
SELECT * from orange LIMIT 0,5;
```

```
// 检索记录11-25
SELECT * FROM orange LIMIT 10,15;  
```
再如，另一种用法：
```
// 查询4-5两条记录
SELECT * FROM orange LIMIT 2 OFFSET 3;
```
等价于
```
SELECT * FROM orange  LIMIT 3,2;
```
**限制行**
```sql
/*  LIMIT 2表示查询结果只显示前两行  */
SELECT 字段 FROM 表名 LIMIT 2;
```
**去重**
```sql
/* DISTINCT用于对该字段对应的属性值去重 */
SELECT DISTINCT 字段 FROM 表名;
```

### 5.1 WHERE过滤函数
如需有条件地从表中选取数据，可将 WHERE 子句添加到 SELECT 语句中，多个WHERE条件需要用AND或OR连接。WHERE 子句类似于程序语言中的 if 条件，根据 MySQL 表中的字段属性值来读取指定的数据。

```sql
SELECT 字段1, 字段2,...字段N FROM 表名1, 表名2...
[WHERE 条件1 [AND [OR]] 条件2 [AND]/[OR] 条件3...]
```

**（1）where的操作符**
- =、!=
- <、>
- between…and…(指定两个值之间，可以是数值、文本或日期）
```sql
--- 示例
SELECT * FROM user WHERE uid BETWEEN 2 AND 5
```

**（2）逻辑操作符**
- and、or
- (not) in
- (not) null
- (not) like

**注**：MySQL 的 WHERE 子句的字符串比较是不区分大小写的。如果条件中有区分大小写的要求，可以使用 `BINARY` 关键字来设定 WHERE 子句的字符串使其可以区分大小写。

### 5.2 LIKE函数与通配符
LIKE与WHERE连用，一般用于模糊查询，LIKE或NOT LIKE支持两个通配符。
- % 表示0-多个字符
- _ 表示一个字符

```sql
--- 语法
SELECT 字段1, 字段2,...字段N FROM 表名 WHERE 字段1 LIKE 条件1 [AND [OR]] 字段2 = 'somevalue'
```

```sql
--- 示例
SELECT * FROM emp WHERE ename LIKE '_A%'
SELECT * FROM emp WHERE ename LIKE '%E_' 
```

## 6、数据表之间的关联

### 6.1 JOIN
当需要从多个数据表中读取数据时，可使用 JOIN 
在两个或多个表中查询数据。 JOIN按功能分为三类：
- **INNER JOIN**：**内连接，求交集**，交集条件是“`ON 条件`”，**查询两数据表中匹配该条件的各个记录（行），然后连接到一起作为一个数据表**。前面的表1的字段放在左边，后面的表2的字段放在右边，如果表2的记录数少于表1的则进行补齐。
```sql
--- 语法
SELECT 表名1.字段2，表名2.字段4 FROM 表名1 INNER JOIN 表名2 ON 表名1.字段1 = 表名2.字段1
```

```sql
--- 示例
SELECT article.aid,article.title,user.username FROM article INNER JOIN user ON article.aid = user.uid;   
等价于
SELECT article.aid,article.title,user.username FROM article, user WHERE article.aid = user.uid;   
```
- **LEFT/RIGHT JOIN**：左/右连接，同样是以“`ON 条件`”查询，但是会**取某个表作为主表，主表的所有记录都会显示（不仅是符合条件的），副表则仅显示符合条件的，副表没有匹配主表的则为NULL。 `LEFT JOIN`时，关键字前面的是主表，后面的是副表。 `RIGHT JOIN`时，关键字前面的是副表，后面的是主表**。
```sql
--- 示例：主表是article，副表是user
SELECT article.aid,article.title,user.username FROM article LEFT JOIN user ON article.aid = user.uid
--- 示例：主表是user，副表是article
SELECT article.aid,article.title,user.username FROM article RIGHT JOIN user ON article.aid = user.uid
```

### 6.2 UNION
UNION/UNION ALL：联合，即合并多个具有相同字段的数据集，若表头字段相同则字段属性值记录叠加，其余字段则直接连接。**由于联合查询时两个表的字段应该是顺序对应的，所以在查询时不能任意更改两表的每个字段的顺序对应位置**。
- UNION：对联合查询结果去重
- UNION ALL：不对联合查询结果去重
```sql
--- 语法
SELECT expression1, expression2, ... expression_n FROM tables
[WHERE conditions]
UNION [ALL]
SELECT expression1, expression2, ... expression_n FROM tables
[WHERE conditions];
```

```sql
--- 示例：将两个表中country合并、name与app_name合并，且查询结果的字段显示为country与name两列
SELECT country, name FROM Websites
WHERE country='CN'
UNION ALL
SELECT country, app_name FROM apps
WHERE country='CN'
ORDER BY country;
```

## 7、排序order by与分组group by

### 7.1 ORDER BY
ORDER BY：对SELECT读取的数据按照某字段结果进行排序，默认升序（ASC），若要降序则在字段后面接DESC。

```sql
--- 语法
SELECT 字段1, 字段2,...字段N FROM 表名1, 表名2...
ORDER BY 字段1 [ASC [DESC][默认 ASC]], [字段2...] [ASC [DESC][默认 ASC]]
```
可以使用任何字段来作为排序的条件，从而返回排序后的查询结果。**可以设定多个字段来排序**，也可以在之前添加 WHERE…LIKE 子句来设置条件。

### 7.2 GROUP BY
GROUP BY：根据一个或多个字段对应的列数据，对SELECT查询结果集进行分组。在分组的列上还可以使用 COUNT，SUM，AVG等函数。
```sql
--- 语法
SELECT 字段1, function(字段1)
FROM 表名
WHERE 条件
GROUP BY 字段1;
```

```sql
--- 示例
SELECT name, COUNT(*) FROM employee GROUP BY name;
```
**（1）WITH ROLLUP的使用**

实现**在分组统计基础上再进行相同的统计（SUM,AVG,COUNT…）**。例如我们将以上的数据表按名字进行分组，每个人统计了登录次数，在此基础上**又统计了所有人登录的次数**。

```sql
--- 示例
SELECT name, SUM(singin) as singin_count FROM employee GROUP BY name WITH ROLLUP;
```

<img src="https://img-blog.csdnimg.cn/20190828104303269.png"> 

这样得出了登录次数之和SUM(singin) ，但是未对结果命名。这就引出了coalesce的使用。

**（2）COALESCE的使用**
可以使用 `COALESCE` 来设置一个可以取代 NUll 的名称
```sql
--- 语法
SELECT COALESCE(a,b,c) ... 
```
参数说明
- 如果a == null，则选择b；
- 如果b ==null，则选择c；
- 如果a!=null,则选择a；
- 如果a b c 都为null ，则返回为null（无意义）。
```sql
--- 示例
SELECT COALESCE(name, '总数'), SUM(singin) as singin_count FROM employee GROUP BY name WITH ROLLUP;
```
<img src="https://img-blog.csdnimg.cn/20190828104522826.png">

## 8、处理重复数据
### 8.1 防止表中出现重复数据
**保证数据唯一性**：设置指定字段为**主键**（PRIMARY KEY）或**唯一索引**（UNIQUE）来保证数据的唯一性。

如果你想设置表中first_name字段和last_name字段的数据不能重复，你可以： 

**（1）设置双主键**：那么对应的字段的默认值不能为空，因此需要设置为`NOT NULL`。
```sql
--- 示例
CREATE TABLE person_tbl(
	first_name CHAR(20) NOT NULL,
	last_name CHAR(20) NOT NULL,
	sex CHAR(10),
	PRIMARY KEY (last_name, first_name)
)
```

**（2）插入数据不重复**：使用`INSERT IGNORE INTO`忽略那些在数据库中已存在的数据，从而达到不重复插入的目的。 

**（3）设置唯一索引UNIQUE**：如果我们设置了`唯一索引UNIQUE`，那么在插入重复数据时，SQL语句将无法执行成功，并抛出异常。
```sql
--- 示例
CREATE TABLE person_tbl ( 
	first_name CHAR(20) NOT NULL, 
	last_name CHAR(20) NOT NULL,
	sex CHAR(10), 
	UNIQUE (last_name, first_name)
)
```

### 8.2 统计重复数据

若要统计表person_tbl中字段first_name和字段last_name中的重复数据，可以使用以下SQL语句实现。
```sql
SELECT last_name, first_name，COUNT(*) as repetitions
FROM person_tbl
GROUP BY last_name, first_name
HAVING repetitions > 1;
```

**操作解析：字段first_name和字段last_name的属性列包含的值可能会重复。使用COUNT(*)进行统计重复数，作为新的字段repetitions。用GROUP BY子句进行分组。HAVING子句用于在聚合函数count之后的筛选（where只能在之前选），筛选后分组后只留下重复数大于1那些记录。**

### 8.3 过滤重复数据
**（1）DISTINCT**：如果需要读取不重复的数据可以在 SELECT 语句中使用 `DISTINCT` 关键字来过滤重复数据。
```sql
SELECT DISTINCT 字段1, 字段2 FROM 表名;
```

**（2）GROUP BY**：也可以使用 `GROUP BY` 来读取数据表中不重复的数据：

```sql
SELECT 字段1, 字段2 FROM 表名 GROUP BY (字段1, 字段2);
```

### 8.4 删除重复数据
**（1）GROUP BY** ：如果想删除数据表中的重复数据，可以使用以下的SQL语句：
```sql
CREATE TABLE 临时表名 SELECT 字段1, 字段2  FROM 旧表名  GROUP BY (字段1, 字段2);
DROP TABLE 旧表名;
ALTER TABLE 临时表名 RENAME TO 旧表名;
```

**（2）索引和主键**：也可以在数据表中添加 INDEX（索引）和 PRIMAY KEY（主键）方法如下：

```sql
ALTER IGNORE TABLE 表名 ADD PRIMARY KEY (last_name, first_name);
```

## 9、事务控制语言（Transaction Control Language，TCL）
**事务的4个特性（ACID）**：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）

**注意**：**在 MySQL 命令行的默认设置下，事务都是自动提交的**，即执行 SQL 语句后就会马上执行 COMMIT 操作。因此要显式地开启一个事务时必须使用命令 `BEGIN` 或 `START TRANSACTION`，或者执行命令 `SET AUTOCOMMIT=0`，用来禁止使用当前会话的自动提交。

 **MYSQL 事务处理主要有两种方面**： 
 
 **（1）用 BEGIN, ROLLBACK, COMMIT来实现** ：`BEGIN` 开始一个事务；`ROLLBACK` 事务回滚；`COMMIT` 事务确认。
 
 **（2）直接用 SET 来改变 MySQL 的自动提交模式:** `SET AUTOCOMMIT=0` 禁止自动提交；`SET AUTOCOMMIT=1` 开启自动提交。

```sql
mysql> use 数据库名;
Database changed
mysql> CREATE TABLE runoob_transaction_test( id int(5)) engine=innodb;  # 创建数据表，只有innodb引擎才能使用事务。
mysql> select * from runoob_transaction_test;
mysql> begin;  # 开始事务
mysql> insert into runoob_transaction_test value(5);
mysql> insert into runoob_transaction_test value(6);
mysql> commit; # 提交事务，永久修改了
mysql> select * from runoob_transaction_test;
+------+
| id   |
+------+
| 5    |
| 6    |
+------+
mysql> begin;    # 开始事务
mysql> insert into runoob_transaction_test values(7);
mysql> rollback;   # 回滚，撤销所有正在进行但未提交的修改
mysql> select * from runoob_transaction_test;   # 因为回滚所以数据没有插入
+------+
| id   |
+------+
| 5    |
| 6    |
+------+
```

## 10、索引

**索引的作用**：提高MySQL的检索速度

**索引的分类**：
- 单列索引，即一个索引只包含单个列，一个表可以有多个单列索引，但这不是组合索引。
- 组合索引，即一个索引包含多个列。 

**注意**：创建索引时，你需要确保该索引是应用在 SQL 查询语句的条件(一般作为 WHERE 子句的条件)。更新表时，MySQL不仅要保存数据，还要保存一下索引文件。实际上，索引也是一张表，该表保存了主键与索引字段，并指向实体表的记录。 

**显示索引信息**：

```sql
SHOW INDEX FROM 表名;
```

### 10.1 创建/删除索引

**创建索引的方式**：

（1）设置某字段为索引，并设置索引名：

```sql
CREATE INDEX 索引名 ON 表名(字段); 
```

（2）修改表结构(添加某字段为索引)：

```sql
ALTER TABLE 表名 ADD INDEX 索引名(字段);
```

（3）创建表的时候直接指定：

```sql
CREATE TABLE 表名(
	字段1 INT NOT NULL, 
	字段2 VARCHAR(16) NOT NULL,
	INDEX 索引名 (字段2)
);  
```

**删除索引的方式**：

```sql
DROP INDEX 索引名 ON 表名; 
```

### 10.2 唯一索引UNIQUE
唯一索引UNIQUE与前面的普通索引相比，**唯一索引的列的值必须唯一，但允许有空值**。**如果是组合索引，则列值的组合必须唯一**。
```sql
--- 唯一索引的几种创建方式
CREATE UNIQUE INDEX 索引名 ON 表名(字段); 
ALTER TABLE 表名 ADD UNIQUE 索引名(字段);
CREATE TABLE 表名(
	字段1 INT NOT NULL,
	字段2 VARCHAR(16) NOT NULL,
	UNIQUE 索引名 (字段2)
);  
```

### 10.3 使用ALTER命令添加和删除索引/主键

```sql
--- 为表添加一个主键，其字段的索引值必须是唯一的，且不能为NULL
ALTER TABLE 表名 ADD PRIMARY KEY (字段);
--- 为表创建唯一索引，字段值必须是唯一的（除了NULL外，NULL可能会出现多次）
ALTER TABLE 表名 ADD UNIQUE 索引名 (字段);
--- 为表添加普通索引，索引值可出现多次
ALTER TABLE 表名 ADD INDEX 索引名 (字段);
--- 为表创建FULLTEXT索引，用于全文索引
ALTER TABLE 表名 ADD FULLTEXT 索引名 (字段);
--- 删除testalter_tbl表的主键
ALTER TABLE testalter_tbl DROP PRIMARY KEY;
```

## 11、导出/导入数据

### 11.1 导出数据
**（1）将查询结果导出到某文件路径下**
```sql
--- 语法
SELECT ... INTO OUTFILE 文件路径
```
```sql
--- 举例
SELECT * FROM runoob_tbl INTO OUTFILE '/tmp/runoob.txt';
```

**（2）导出表作为原始数据**

mysqldump 产生一个 SQL 脚本，其中包含从头重新创建数据库所必需的命令 。使用 mysqldump 导出数据需要使用 --tab 选项来指定导出文件指定的目录，该目标必须是可写的。
```sql
--- 将数据表 runoob_tbl 导出到 /tmp 目录中：
$ mysqldump -u root -p --no-create-info --tab=/tmp RUNOOB runoob_tbl
```

**（3）导出SQL格式的数据**
```sql
--- 导出各种操作和格式信息
$ mysqldump -u root -p RUNOOB runoob_tbl > dump.txt
```

**（4）导出整个数据库的数据**
```sql
$ mysqldump -u root -p RUNOOB > database_dump.txt
```

**（5）备份所有数据库**：

```sql
$ mysqldump -u root -p --all-databases > database_dump.txt
```

### 11.2 导入数据

**（1）mysql 命令导入** 

```sql
--- 语法
mysql -u用户名 -p密码 < 数据库名.sql
```
```sql
--- 举例
mysql -uroot -p123456 < runoob.sql
```

**（2）source 命令导入**

source命令导入数据库需要先登录到数库终端
```sql
--- 创建数据库
mysql> create database abc;     
--- 使用已创建的数据库 
mysql> use abc;               
--- 设置编码   
mysql> set names utf8;        
--- 导入备份数据库
mysql> source /home/abc/abc.sql  
```

**（3）使用 LOAD DATA 导入数据**

从当前目录中读取文件 dump.txt ，将该文件中的数据插入到当前数据库的数据表中。

```sql
mysql> LOAD DATA LOCAL INFILE 'dump.txt' INTO TABLE mytbl;
```
LOAD DATA 默认情况下是按照数据文件中列的顺序插入数据的，如果数据文件中的列与插入表中的列不一致，则需要指定列的顺序。如，在数据文件中的列顺序是 a,b,c，但在插入表的列顺序为b,c,a，则数据导入语法如下：

```sql
mysql> LOAD DATA LOCAL INFILE 'dump.txt' INTO TABLE mytbl (b, c, a);
```

## 12、函数、运算符、正则表达式

**函数**：各种聚合函数，日期函数，高级函数，字符串函数。 
```sql
--- 聚合函数
MAX()：统计列表或者表达式的最大值。
MIN()：统计列表或者表达式的最小值。
AVG()：统计列表或者表达式的平均值。
SUM()：统计列表或者表达式的和。
COUNT()：用来统计表中数据的记录条数。
```
**运算符**：算术运算符，比较运算符，逻辑运算符，位运算符。 

**模糊匹配**：MySQL可以通过 `LIKE …%` 来进行模糊匹配。

**正则表达式**：MySQL中使用 `REGEXP` 操作符来进行正则表达式匹配。

```sql
--- 举例：查找name字段中以'st'为开头的所有数据
SELECT name FROM person_tbl WHERE name REGEXP '^st';
```

## 13、总结
```sql
/* 数据定义语言DDL */
--- SHOW
show databases
show tables
show columns from 表名
show index from 表名


--- 删除数据库
drop database 库名
--- 删除表结构
drop table 表名
--- 删除表数据
truncate table 表名
delete form 表名


--- 授权
grant select, insert, update, delete, create, drop on 表名 to 用户


--- 创建表字段后设置主键
create table 表名(
	id INT NOT NULL,
	title VARCHAR(100) NOT NULL,
	author VARCHAR(40) NOT NULL,
	submission_date DATE,
	PRIMARY KEY (id)
)

--- 创建表字段过程中指定主键
create table 表名(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	url VARCHAR(255) 
)

--- 创建表之后，在单独设置主键
alter table 表名 add id INT AUTO_INCREMENT PRIMARY KEY
alter table 表名 add PRIMARY KEY (last_name, first_name)

--- 设置双主键来防止表中出现重复数据
create table 表名(
	first_name CHAR(20) NOT NULL,
	last_name CHAR(20) NOT NULL,
	sex CHAR(10),
	PRIMARY KEY (last_name, first_name)
)

--- 设置唯一索引UNIQUE，在插入重复数据时，SQL无法执行成功，并抛出异常
create table 表名(
	first_name CHAR(20) NOT NULL,
	last_name CHAR(20) NOT NULL,
	sex CHAR(10),
	UNIQUE (last_name, first_name)
)

--- 建表语句中创建索引
create table 表名(
	字段1 INT NOT NULL, 
	字段2 VARCHAR(16) NOT NULL,
	INDEX 索引名 (字段2)
)

--- 建表之后单独创建索引
create index 索引名 on 表名(字段名)
create unique index 索引名 on 表名(字段名)


--- 复制数据表
--- （1）获取就数据表的创建语句
show create table 旧表名
--- （2）赋值创建语句，将其中的旧表名改为新表名，执行建表操作
--- （3）数据复制到新表中
insert into 新表名(字段) select 字段 form 旧表名


--- ALTER
alter table 旧表名 rename to 新表名
alter table 表名 engine = MYISAM
alter table 表名 drop 字段名
alter table 表名 add 新字段名 字段类型
alter table 表名 add primary key(字段名)
alter table 表名 add index 索引名(字段名)
alter table 表名 add unique 索引名(字段名)
alter table 表名 modify 字段名 新的类型
alter table 表名 modify 字段名 新的类型 新的限制条件（比如非空且默认值为100 NOT NULL DEFAULT 100）
alter table 表名 change 旧字段名 新字段名 新的类型
alter table 表名 alter 字段名 set DEFAULT 100
alter table 表名 alter 字段名 drop DEFAULT



/* 数据操作语言DML */
--- INSERT
insert into 表名 (字段名...) values (字段值...)
--- INSERT IGNORE INTO：忽略那些在数据库中已存在的数据，从而达到不重复插入的目的。
insert ignore into 表名 (字段名...) values (字段值...)

--- UPDATE
update 表名 set 字段名 = 新的字段值 where ...
update employee set salay=8000 where name='jack'

--- DELETE
delete from 表名 where ...
delete from employee where name='rose'



/* 数据查询语言DQL */

/* 其中SELECT后面可加 *或部分列名/函数/运算式/字符串常量，DISTINCT为指定去掉结果表中的重复行，如果没有指定DISTINCT，默认为ALL */
/* 当聚集函数遇到空值时，除COUNT(*)外，都跳过空值而只处理非空值；聚集函数只能用于SELECT子句和GROUP BY中的HAVING子句。 */
/*
GROUP BY子句
（1）作用在于将查询结果按某一列或多列的值分组，值相等的为一组。
（2）分组后聚集函数将作用于每一个组，即每一组都有一个函数值。
（3）HAVING可对分的组进行筛选，即作用对象为分的这些组，这里要区别于WHERE作用于整个表。
（4）SELECT后跟的列除非使用了聚集函数，否则列名必须包含在GROUP BY短语中。
*/
--- SELECT查询格式
SELECT [ALL|DISTINCT] <目标列表达式> [,<目标列表达式>]...
FROM <表名或视图名> [,<表名或视图名>...] | (<SELECT语句>) [AS] <别名>
[WHERE 条件1 [AND [OR]] 条件2 [AND]/[OR] 条件3...]
[GROUP BY <列名1> [HAVING <条件表达式>]]
[ORDER BY <列名2> [ASC|DESC]];
[LIMIT M, N]

--- （1）LIMIT
--- 查询记录11-25
select 字段名 from 表名 limit 10, 15

--- 查询前两行
select 字段名 from 表名 limit 2


--- （2）数据去重
--- 使用DISTINCT对查询结果去重
select distinct 字段名1, 字段名2 from 表名
--- 使用GROUP BY对查询结果去重
select 字段名1, 字段名2 from 表名 group by 字段1, 字段2


--- （3）统计重复数据
select last_name, first_name, COUNT(*) as repetitions
from person_tbl
group by last_name, first_name
having repetitions > 1


--- （4）LIKE/NOT LIKE函数与通配符
select 字段名... from 表名 where 字段名 like 通配符

--- % 表示0-多个字符，_ 表示一个字符
select * from emp where ename like '_A%'
select * from emp where ename not like '_A%'

--- （5）数据表之间的连接查询
--- ①CROSS JOIN：交叉连接，求两个表的笛卡尔积
--- 下面三种方式可以直接连接两个表，查询结果相同
select * form 表名1 join 表名2
select * form 表名1 cross join 表名2
select * form 表名1 inner join 表名2

--- ②JOIN/INNER JOIN：内连接，求交集，交集条件是“ON 条件”，查询两数据表中匹配该条件的各个记录（行），然后连接到一起作为一个数据表。
select 表名1.字段2, 表名2.字段4 from 表名1 inner join 表名2 on 表名1.字段1 = 表名2.字段1

--- ③LEFT/RIGHT JOIN：左/右外连接，同样是以“ON 条件”查询，但是会取某个表作为主表，主表的所有记录都会显示（不仅是符合条件的），副表则仅显示符合条件的，副表没有匹配主表的则为NULL。 LEFT JOIN时，关键字前面的是主表，后面的是副表。 RIGHT JOIN时，关键字前面的是副表，后面的是主表。
select 表名1.字段2, 表名2.字段4 from 表名1 left join 表名2 on 表名1.字段1 = 表名2.字段1
select 表名1.字段2, 表名2.字段4 from 表名1 right join 表名2 on 表名1.字段1 = 表名2.字段1


--- （6）数据表之间的联合查询
--- UNION/UNION ALL：联合，即合并多个具有相同字段的数据集，若表头字段相同则字段属性值记录叠加，其余字段则直接连接。由于联合查询时两个表的字段应该是顺序对应的，所以在查询时不能任意更改两表的每个字段的顺序对应位置。
--- UNION：对联合查询结果去重；UNION ALL：不对联合查询结果去重
/*
union查询就是把2条或者多条sql语句的查询结果，合并成一个结果集。
如：sql1: N行，sql2: M行，sql1 union sql2 ---> N+M行

1、能否从2张表查询再union呢?
可以,union 合并的是"结果集",不区分在自于哪一张表.

2、取自于2张表,通过"别名"让2个结果集的列一致。那么,如果取出的结果集,列名字不一样,还能否union.
可以,而且取出的最终列名,以第1条sql为准

3、union满足什么条件就可以用了?
只要结果集中的列数一致就可以.（如都是2列或者N列）

4、union后结果集,可否再排序呢?
可以的。Sql1 union sql2 order by 字段
注意: order by 是针对合并后的结果集排的序.

5、如果Union后的结果有重复(即某2行,或N行,所有的列,值都一样),怎么办?
这种情况是比较常见的,默认会去重.

6、如果不想去重怎么办?
union all
*/
--- 语法（两表的字段数量必须相同）
SELECT 字段1, 字段2, ... 字段n FROM 表名1
[WHERE conditions]
UNION [ALL]
SELECT 字段1, 字段2, ... 字段n FROM 表名2
[WHERE conditions];

--- 将两个表中country合并，Websites中的name与apps中的app_name合并，且查询结果的字段显示为country与name两列
select country, name from Websites
where country='CN'
union all
select country, app_name from apps
where country='EN'
order by country

--- SQL必知必会第47题：表OrderItems包含订单产品信息，字段prod_id代表产品id、quantity代表产品数量。 将两个 SELECT 语句结合起来，以便从 OrderItems表中检索产品 id（prod_id）和 quantity。其中，一个 SELECT 语句过滤数量为 100 的行，另一个 SELECT 语句过滤 id 以 BNBG 开头的产品，最后按产品 id 对结果进行升序排序。
select prod_id,quantity
from OrderItems
where quantity=100
union 
select prod_id,quantity
from OrderItems
where prod_id like 'BNBG%'
order by prod_id;
等价于
select prod_id,quantity 
from OrderItems
where quantity = 100 or prod_id like 'BNBG%'
order by prod_id


--- （7）ORDER BY：对SELECT读取的数据按照某字段结果进行排序，默认升序（ASC），若要降序则在字段后面接DESC。
--- 注：可以设定多个字段来排序
SELECT 字段1, 字段2,...字段N FROM 表名1, 表名2...
ORDER BY 字段1 [ASC [DESC][默认 ASC]], [字段2...] [ASC [DESC][默认 ASC]]


--- （8）GROUP BY：根据一个或多个字段对应的列数据，对SELECT查询结果集进行分组。在分组的列上还可以使用 COUNT，SUM，AVG等函数。
SELECT 字段1, function(字段1)
FROM 表名
WHERE 条件
GROUP BY 字段1;

--- 查询每个人的数据条目数量
select name, count(*) from employee group by name

--- 查询平均成绩大于等于90分的学生学号和平均成绩
select Sno,AVG(Grade) 
from SC 
group by Sno
having AVG(Grade)>=90;

--- WITH ROLLUP：实现在分组统计基础上再进行相同的统计（SUM,AVG,COUNT…）。
--- 按名字进行分组，每个人统计了登录次数，在此基础上又统计了所有人登录的次数
select name, SUM(singin) as singin_count 
from employee
group by name
with rollup

--- COALESCE：使用 COALESCE 来设置一个可以取代 NUll 的名称
--- 语法如下，如果a == null，则选择b；如果b ==null，则选择c；如果a!=null,则选择a；如果a b c 都为null ，则返回为null（无意义）。
select coalesce(a,b,c) ...
--- 按名字进行分组，每个人统计了登录次数，在此基础上又统计了所有人登录的次数，并对登陆次数总数命名为“总数”
select coalesce(name, '总数'), SUM(singin) as singin_count
from employee
group by name
with rollup


--- （9）聚合函数
MAX()：统计列表或者表达式的最大值。
MIN()：统计列表或者表达式的最小值。
AVG()：统计列表或者表达式的平均值。
SUM()：统计列表或者表达式的和。
COUNT()：用来统计表中数据的记录条数。
substring(字符串，起始位置，截取字符数）：字符串的截取
concat(字符串1，字符串2，字符串3,...)：字符串的拼接
upper(字符串）：字母大写
lower(字符串)：字母小写
date_format(日期,'%Y%m%d')：返回日期的一部分

--- SQL必知必会第22题：编写 SQL 语句，返回顾客 ID（cust_id）、顾客名称（cust_name）和登录名（user_login），其中登录名全部为大写字母，并由顾客联系人的前两个字符（cust_contact）和其所在城市的前三个字符（cust_city）组成。
select cust_id,cust_name,
upper(concat(substring(cust_name,1,2),substring(cust_city,1,3))) as user_login
from Customers

--- SQL必知必会第23题：编写 SQL 语句，返回 2020 年 1 月的所有订单的订单号（order_num）和订单日期（order_date），并按订单日期升序排序
select * from Orders 
where date_format(order_date, '%Y-%m') = '2020-01' 
order by order_date

--- SQL必知必会第27题：编写 SQL 语句，返回每个订单号（order_num）各有多少行数（order_lines），并按 order_lines对结果进行升序排序。（GROUP BY的应用）
select order_num, count(order_num) as order_lines 
from OrderItems
group by order_num
order by order_lines

--- SQL必知必会第28题：编写 SQL 语句，返回名为 cheapest_item 的字段，该字段包含每个供应商成本最低的产品（使用 Products 表中的 prod_price），然后从最低成本到最高成本对结果进行升序排序。
select vend_id, min(prod_price) as cheapest_item
from Products
group by vend_id
order by cheapest_item

--- SQL必知必会第28题：OrderItems代表订单商品表，包括：订单号order_num和订单数量quantity。请编写 SQL 语句，返回订单数量总和不小于100的所有订单号，最后结果按照订单号升序排序。
select order_num from OrderItems
group by order_num
having sum(quantity) >= 100
order by order_num

--- SQL必知必会第30题：OrderItems表代表订单信息，包括字段：订单号order_num和item_price商品售出价格、quantity商品数量。编写 SQL 语句，根据订单号聚合，返回订单总价不小于1000 的所有订单号，最后的结果按订单号进行升序排序。（总价 = item_price 乘以 quantity。）
select order_num, sum(item_price * quantity) as total_price
from OrderItems
group by order_num
having total_price >= 1000
order by order_num

--- SQL必知必会第32题：OrderItems表示订单商品表，含有字段订单号：order_num、订单价格：item_price；Orders表代表订单信息表，含有顾客id：cust_id和订单号：order_num。使用子查询，返回购买价格为 10 美元或以上产品的顾客列表，结果无需排序。注意：你需要使用 OrderItems 表查找匹配的订单号（order_num），然后使用Order 表检索这些匹配订单的顾客 ID（cust_id）。
SELECT DISTINCT cust_id
FROM Orders
WHERE order_num IN (
    SELECT order_num
    FROM OrderItems
    WHERE item_price >= 10
)

--- SQL必知必会第34题：你想知道订购 BR01 产品的日期，有表OrderItems代表订单商品信息表，prod_id为产品id；Orders表代表订单表有cust_id代表顾客id和订单日期order_date；Customers表含有cust_email 顾客邮件和cust_id顾客id。【问题】返回购买 prod_id 为BR01 的产品的所有顾客的电子邮件（Customers 表中的 cust_email），结果无需排序。
select cust_email 
from OrderItems inner join Orders 
inner join Customers
on OrderItems.order_num = Orders.order_num 
and Orders.cust_id = Customers.cust_id
and OrderItems.prod_id='BR01'
或
select cust_email from OrderItems, Orders, Customers
where OrderItems.order_num = Orders.order_num and Orders.cust_id = Customers. cust_id
and OrderItems.prod_id='BR01'
或
SELECT cust_email
FROM Customers
WHERE cust_id IN 
    (SELECT cust_id FROM Orders WHERE order_num IN 
    	(SELECT order_num FROM OrderItems WHERE prod_id = 'BR01')
    );

--- SQL必知必会第35题：我们需要一个顾客 ID 列表，其中包含他们已订购的总金额。OrderItems表代表订单信息，OrderItems表有订单号：order_num和商品售出价格：item_price、商品数量：quantity。Orders表订单号：order_num、顾客id：cust_id。【问题】编写 SQL语句，返回顾客 ID（Orders 表中的 cust_id），并使用子查询返回total_ordered 以便返回每个顾客的订单总数，将结果按金额从大到小排序。提示：你之前已经使用 SUM()计算订单总数。
select cust_id, sum(item_price*quantity) as total_order
from OrderItems, Orders
where OrderItems.order_num = Orders.order_num
group by cust_id
order by total_order desc

--- SQL必知必会第36题：Products 表中检索所有的产品名称：prod_name、产品id：prod_id。OrderItems代表订单商品表，订单产品：prod_id、售出数量：quantity。【问题】编写 SQL 语句，从 Products 表中检索所有的产品名称（prod_name），以及名为 quant_sold 的计算列，其中包含所售产品的总数（在 OrderItems 表上使用子查询和 SUM(quantity)检索）。
select prod_name as prod_name, sum(quantity) as quant_sold
from Products, OrderItems
where Products.prod_id = OrderItems.prod_id
group by prod_name
或
select prod_name as prod_name, sum(quantity) as quant_sold
from Products join OrderItems
on Products.prod_id = OrderItems.prod_id
group by prod_name

--- SQL必知必会第39题：表OrderItems代表订单商品信息表，prod_id为产品id；Orders表代表订单表有cust_id代表顾客id和订单日期order_date。【问题】编写 SQL 语句，使用子查询来确定哪些订单（在 OrderItems 中）购买了 prod_id 为 "BR01" 的产品，然后从 Orders 表中返回每个产品对应的顾客 ID（cust_id）和订单日期（order_date），按订购日期对结果进行升序排序。
--- on是连接条件，where是筛选条件
select cust_id, order_date
from Orders join OrderItems
on Orders.order_num = OrderItems.order_num
where prod_id = 'BR01'
order by order_date
或
select cust_id, order_date
from Orders join OrderItems
on Orders.order_num = OrderItems.order_num
and prod_id = 'BR01'
order by order_date

--- SQL必知必会第40题：返回购买 prod_id 为BR01 的产品的所有顾客的电子邮件（Customers 表中的 cust_email），结果无需排序。
select cust_email
from Customers join Orders join OrderItems
on OrderItems.order_num = Orders.order_num 
and Orders.cust_id = Customers.cust_id
where prod_id='BR01'

--- SQL必知必会第41题：编写 SQL 语句，返回订单总价不小于1000 的客户名称和总额（OrderItems 表中的order_num）。提示：需要计算总和（item_price 乘以 quantity）。按总额对结果进行排序，请使用INNER JOIN 语法。
select cust_name, sum(item_price*quantity) as total_price
from OrderItems join Orders join Customers
on OrderItems.order_num = Orders.order_num
and Orders.cust_id = Customers.cust_id
group by cust_name
having total_price >= 1000

--- SQL必知必会第43题：检索每个顾客的名称（Customers表中的 cust_name）和所有的订单号（Orders 表中的 order_num），列出所有的顾客，即使他们没有下过订单。最后根据顾客姓名cust_name升序返回。
select cust_name, order_num
from Customers left join Orders
on Customers.cust_id = Orders.cust_id
order by cust_name

--- SQL必知必会第45题：使用 OUTER JOIN 联结 Products 表和 OrderItems 表，返回产品名称（prod_name）和每一项产品的总订单数（不是订单号），并按产品名称升序排序。
--- 两表中重复的字段，需要指定表名，即以表名.字段名的方式表示
select prod_name,count(OrderItems.prod_id) as orders
from Products left join OrderItems
on Products.prod_id = OrderItems.prod_id
group by prod_name
order by prod_name

--- SQL必知必会第47题：表OrderItems包含订单产品信息，字段prod_id代表产品id、quantity代表产品数量。 将两个 SELECT 语句结合起来，以便从 OrderItems表中检索产品 id（prod_id）和 quantity。其中，一个 SELECT 语句过滤数量为 100 的行，另一个 SELECT 语句过滤 id 以 BNBG 开头的产品，最后按产品 id 对结果进行升序排序。
select prod_id,quantity
from OrderItems
where quantity=100
union 
select prod_id,quantity
from OrderItems
where prod_id like 'BNBG%'
order by prod_id;
等价于
select prod_id,quantity 
from OrderItems
where quantity = 100 or prod_id like 'BNBG%'
order by prod_id
```


## 14、mysql数据库实例与提升
### 14.1 经典的50个SQL语句（以学生、教师为背景）
跳转网址：https://www.cnblogs.com/luo813/p/8993727.html

#### 1、以下功能以学生-课程数据库为例：
- 学生表：Student(Sno,Sname,Ssex,Sage,Sdept)
- 课程表：Course(Cno,Cname,Cpno,Ccredit)
- 学生选课表：SC(Sno,Cno,Grade)
##### （1）求各个课程号及相应的选课人数。
```sql
--- 该语句对查询结果按课程号Cno的值进行分组，所有具有相同课程号Cno值的元组为一组，然后对每一组作用聚集函数COUNT进行计算，以求得该组的学生人数。
SELECT Cno,COUNT(Sno)
FROM SC
GROUP BY Cno;
```

##### （2）查询平均成绩大于等于90分的学生学号和平均成绩。
下面的语句是不对的：
```sql
SELECT Sno,AVG(Grade)
FROM SC
WHERE AVG(Grade)>=90
GROUP BY Sno;
```
因为WHERE子句中是不能用聚集函数作为条件表达式的，正确的查询语句是：
```sql
SELECT Sno,AVG(Grade)
FROM SC
GROUP BY Sno
HAVING AVG(Grade)>=90;
```
