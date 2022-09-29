## 一、为什么要使用数据库

程序有些数据需要持久化。

文件存储有一定的问题，比如不适合查询。

所以说数据库的优点：

1.实现数据持久化；

2.使用完整的管理系统统一管理数据，方便查询。

<br/>

## 二、数据库相关概念

DB(DataBase)：存储数据的仓库，保存了一系列**有组织**的数据。(如果没有组织，那其实和回收站一样了)

DBMS(DataBase Manager System)：数据库管理系统，数据库是通过DBMS创建和操作的容器。

DBMS分为两大类：

```
第一类是基于共享文件系统的DBMS，例如微软的access

第二类是基于C/S架构的DBMS，例如MySQL、Oracle、SqlServer。（安装数据库是安装数据库的服务端）
```

**切记：我们平时说的安装数据库，是不对的。是安装数据库管理系统。数据库管理系统创建和操作数据库。**

常见的DBMS：MySql（Oracle）、Oracle、DB2（IBM推出的、适合处理海量数据）、SqlServer（微软、只能安装在win上）

<br/>

SQL(Structure Query Language)：专门用来和数据库通讯的语言。CRUD。

基本所有的DBMS都支持SQL

## 三、数据库存储的特点

<br/>

<br/>

## 四、初始MySQL

### 启动和停止数据库的命令

```
进入安装好的DBMS 
mysql -h localhost -P 3306 -u root -p
退出
exit;/\q/
启动MySQL服务
sudo /usr/local/mysql/support-files/mysql.server start
停止MySQL服务
sudo /usr/local/mysql/support-files/mysql.server stop
重启MySQL服务
sudo /usr/local/mysql/support-files/mysql.server restart
```

<br/>

### MySQL常见命令

1.查看DBMS里有哪些数据库

```mysql
show databases;
create database test;---创建一个名为test的数据库
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
```

**information_schema**  用于存储数据库元数据(数据库的数据)，例如数据库名、表名、列的数据类型、访问权限等；information_schema 中的表实际上是视图，而不是基本表，因此，文件系统上没有与之相关的文件。

**mysql** 是mysql的核心数据库，类似于sql server中的master表，主要负责存储数据库的用户、权限设置、关键字等mysql自己需要使用的控制和管理信息。不可以删除。

**performance_schema **为系统新增用以收集数据库服务器性能参数，其下的所有表的存储引擎均为performance_schema 。

**sys **sys内的table大多承载了performance_schema的内容，它通过视图把information_schema和performance_schema结合起来 

2.打开制定的数据库

```
use 数据库名;---进入了一个库，
use sys;
```

3.查看当前库的所有表

```
show tables;---查看当前库有什么表
select database(); ---查看当前在哪个库
show tables from performance_schema; 
```

4.查看其它库的所有表

```
show tables from performance_schema; 
```

5.创建表

```
mysql> create table stuinfo(
    -> id int,
    -> name varchar(20)
    -> );
```

**6.查看表结构**

```
desc 表名;
mysql> desc stuinfo;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
```

7.查看当前mysql版本

```
mysql> select version();
+-----------+
| version() |
+-----------+
| 8.0.28    |
+-----------+
shell 下可以使用
mysql --version
```

<br/>

### mysql语法规范

1.mysql不区分大小写，**但是建议关键字大写，表名和列名小写**。
2.每条命令用分号结尾；
3.每条命令可以根据需要进行缩进和换行；
4.注释，有两种，单行注释以#开头；或者--空格加内容；多行注释 /\*。。。\*/

<br/>

## 五、DQL（Data Query Language）语言

这里使用课件里一个myemployees库，导入该库的语句是

```mysql
sql>source 文件路径/myemployees.sql;
```

表结构如下：

```
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| employee_id    | int          | NO   | PRI | NULL    | auto_increment | 员工ID
| first_name     | varchar(20)  | YES  |     | NULL    |                | 名字
| last_name      | varchar(25)  | YES  |     | NULL    |                | 姓
| email          | varchar(25)  | YES  |     | NULL    |                | 电子邮件
| phone_number   | varchar(20)  | YES  |     | NULL    |                | 电话号
| job_id         | varchar(10)  | YES  | MUL | NULL    |                | 工种id
| salary         | double(10,2) | YES  |     | NULL    |                | 工资
| commission_pct | double(4,2)  | YES  |     | NULL    |                | 奖金率（年总工资*奖金率=奖金）
| manager_id     | int          | YES  |     | NULL    |                | 部门经理的员工id
| department_id  | int          | YES  | MUL | NULL    |                | 部门id
| hiredate       | datetime     | YES  |     | NULL    |                | 入职日期
+----------------+--------------+------+-----+---------+----------------+

+-----------------+------------+------+-----+---------+----------------+
| Field           | Type       | Null | Key | Default | Extra          |
+-----------------+------------+------+-----+---------+----------------+
| department_id   | int        | NO   | PRI | NULL    | auto_increment | 部门id
| department_name | varchar(3) | YES  |     | NULL    |                | 部门名称
| manager_id      | int        | YES  |     | NULL    |                | 部门经理的员工id
| location_id     | int        | YES  | MUL | NULL    |                | 部门地址id
+-----------------+------------+------+-----+---------+----------------+

+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| job_id     | varchar(10) | NO   | PRI | NULL    |       | 工种id
| job_title  | varchar(35) | YES  |     | NULL    |       | 工种名字
| min_salary | int         | YES  |     | NULL    |       | 最低工资
| max_salary | int         | YES  |     | NULL    |       | 最高工资
+------------+-------------+------+-----+---------+-------+

+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| location_id    | int         | NO   | PRI | NULL    | auto_increment | 部门的地址id
| street_address | varchar(40) | YES  |     | NULL    |                | 街道名
| postal_code    | varchar(12) | YES  |     | NULL    |                | 邮政编码
| city           | varchar(30) | YES  |     | NULL    |                | 城市
| state_province | varchar(25) | YES  |     | NULL    |                | 省/州
| country_id     | varchar(2)  | YES  |     | NULL    |                | 国家id
+----------------+-------------+------+-----+---------+----------------+
```

### 基础查询

```mysql
/*
 * 基本语法
 * select 查询列表
 * from 表名;
 *  
 * 注意：
 *  1.查询列表可以是表中的字段，常量值、表达式、函数
 *  2.查询到的结果是一个虚拟的表格，不是真实存在的。
 */
 
use myemployees; -- 建议每次查询之前都加上这一句


#1.查询表中单个字段
mysql> select last_name from employees;
#2.查询表中多个字段
mysql> select last_name,salary,email from employees;
#3.查询表中所有字段
mysql> select * from employees;
mysql> select 
  `employee_id`,
  `first_name`,
  `last_name`,
  `email`,
  `phone_number`,
  `job_id`,
  `salary`,
  `commission_pct`,
  `manager_id`,
  `department_id`,
  `hiredate`
  from employees;
  -- 注意这里的字段上的``这个是键盘上1旁边的反引号，平时可以不加，但是某个字段如果和关键字重合，可以加上。

#4.查询常量值
mysql> select 100;
+-----+
| 100 |
+-----+
| 100 |
+-----+
mysql> select 'join'; -- MySQL不区分字符和字符串，所以单引号和双引号都可以。
+------+
| join |
+------+
| join |
+------+

#5.查询表达式
mysql> select 100%98;
+--------+
| 100%98 |
+--------+
|      2 |
+--------+

#6.查询函数
sql> select version();
+-----------+
| version() |
+-----------+
| 8.0.28    |
+-----------+

#7.起别名
# 好处1.便于理解
# 好处2.在连接查询的时候，如果要查询的字段有重名的情况，使用别名可以区分开来
mysql> select 100%98 as 结果;
+--------+
| 结果   |
+--------+
|      2 |
+--------+
mysql> select last_name as 姓,first_name as 名 from employees; -- 也可以不用as实现
mysql> select last_name 姓,first_name 名 from employees; -- 要有空格
+-------------+-------------+
| 姓          | 名          |
+-------------+-------------+
| K_ing       | Steven      |
| Kochhar     | Neena       |
| De Haan     | Lex         |
.....
| Gietz       | William     |
+-------------+-------------+
#案例
mysql> select salary as out put from employees; -- 这样不对因为out put这个别名中间有空格这个特殊字符，#也是特殊字符
mysql> select salary as "out put" from employees; -- 官方建议是加上双引号，其实单引号也可以

#8.去重复
#案例 查询员工表中涉及到的所有部门编号
mysql> select distinct department_id from employees;
+---------------+
| department_id |
+---------------+
|          NULL |
|            10 |
|            20 |
|            30 |
|            40 |
|            50 |
|            60 |
|            70 |
|            80 |
|            90 |
|           100 |
|           110 |
+---------------+


#9.+的作用：mysql种的加号只能当运算符
#案例：查询员工名和员工的姓连成一个字段，显示为姓名
mysql> select last_name+first_name as 姓名 from employees; -- 这样不对，这个字段结果都是0

mysql> select 1+2;# 如果两个操作数都是数值型，那就正常运算；
# 如果任意一个操作数不是数值型，就把其尝试转化为数值型再做运算；
#如果转换失败，就转换成0
mysql> select 'join'+9;
mysql> select null+10; # 如果任意一个操作数是null，那结果肯定是null
#这里使用函数concat(str1,str2...)，如果有数值型数据，会转为字符型
mysql> select concat(last_name,' ',first_name) as 姓名 from employees;
+-------------------+
| 姓名              |
+-------------------+
| K_ing Steven      |
| Kochhar Neena     |
| De Haan Lex       |
...
| Gietz William     |
+-------------------+


#练习 拼接出来employees表中的一些字段值，这些字段中可能为null
select concat(first_name,',',last_name,',',job_id,',',commission_pct) as output from employees;
+-------------------------------+
| output                        |
+-------------------------------+
| NULL                          |
| NULL                          |
| NULL                          |
| John,Russell,SA_MAN,0.40      |
| Karen,Partners,SA_MAN,0.30    |
| Alberto,Errazuriz,SA_MAN,0.30 |
| Gerald,Cambrault,SA_MAN,0.30  |
| Eleni,Zlotkey,SA_MAN,0.20     |
| NULL                          |
| NULL                          |
| NULL                          |
+-------------------------------+
# 结果有一部分为NULL，因为concat函数中，一旦有一个字段为null，结果就会是0
# 所以这里使用一个函数ifnull(expr1,expr2) ifnull(commission_pct,0)如果字段expr1是null，就返回expr2
mysql> select concat(first_name,',',last_name,',',job_id,',',ifnull(commission_pct,0)) as output from employees;
```

### 条件查询

```mysql
/*
 * 语法
 * select 查询列表
 * from 表名
 * where 筛选条件;
 *  注意：字符型数据和日期类型数据必须用引号印起来，数值型不需要
 * 分类：
 *  1.按照条件表达式筛选
 *     条件运算符：>,<,>=,<=,=,不等有两个(!=和<>)
 *  2.按照逻辑运算筛选
 *     逻辑运算符：&&，||,!,推荐使用：and or not 
 *  3.模糊查询
 *     like，between and ，in ，is null 
 *     like一般和通配符搭配使用，通配符有%（任意多个字符，包含0个），_任意单个字符
 *     between and 是一个闭区间，但是不可以颠倒顺序
 *     in是判断某一条数据是否符合in条件中 的一项，如果符合就返回，使用in比or好；in列表的值类型必须统一或兼容
 *     注意，in列表里面不能使用通配符，因为in的本质是使用=号，不是like，所以不支持通配符
 *     =和<>不能用于判断null值
 */
 
  #1.按条件表达式筛选
  #案例：查询工资大于12000的员工信息
  mysql> select * from employees where salary >=12000;
  #案例：查询部门编号不等于90号的员工名和部门编号
  mysql> select concat(last_name," ",first_name)as name,department_id from employees where department_id<>90;
 
  #2.按逻辑运算符筛选
  #案例：查询工资在10000-20000的员工名，工资、以及奖金
  mysql> select concat(first_name,",",last_name) as name,salary,salary*12*ifnull(commission_pct,0) as bonus 
  from employees 
  where salary>=10000 and salary<=20000;
  #案例：查询部门编号不再90-110之间的，或者工资高于15000的员工信息
  mysql> select * from employees where department_id<90 or department_id>110 or salary>15000;
  mysql> select * from employees where not (department_id>=90 and department_id<=110) or salary>15000;
  
  #3.模糊查询
  #案例：查询员工名中包含字符a的员工信息
  mysql> select * from employees where last_name like '%a%';
  #案例：查询员工名中第3个字符位a，第5个字符位为e的员工信息
  mysql> select * from employees where last_name like '__a_e%';
  #案例：查询员工名中第2个字符是_的员工信息
  mysql> select * from employees where last_name like '_\_%';-- 使用反斜杠转义
  mysql> select * from employees where last_name like '_$_%' escape '$'; -- 自定义转义符，推荐使用
  #查询员工编号在100-120的员工信息
  mysql> select * from employees where employee_id between 100 and 120;
  #查询员工的工种编号是IT_PROG，AD_VP，AD_PRES的员工信息
  mysql> select * from employees where job_id in ('AD_PRES','IT_PROG','AD_VP'); -- 使用or也可以
  #案例：查询没有奖金的员工名和奖金率
  mysql> select last_name,commission_pct from employees where commission_pct is null;
  #案例：查询有奖金的员工名和奖金率
  mysql> select last_name,commission_pct from employees where commission_pct is not null;
  
  
  #安全等于<=> 可以参与数值=和is null
  #案例：查询没有奖金的员工名和奖金率
  mysql> select last_name,commission_pct from employees where commission_pct <=> null;
  #案例：查询工资12000的员工信息
  mysql> select * from employees where salary <=>12000;
  
  #案例：查询员工号为176的员工姓名、部门号和年薪
  mysql> select last_name,department_id,salary*12*(1+ifnull(commission_pct,0))as 年薪 from employees 
  where employee_id =176;
```

经典面试题

```mysql
select * from employees;
select * from employees where commission_pct like '%%' and last_name like '%%';
#这两句一样吗？
#答案是不一样，因为commission_pct是存在null值的，执行第二句只会返回commission_pct非null情况的数据
select * from employees where commission_pct like '%%' or last_name like '%%';
#把and改为or其实就一样了。
```

补充

```mysql
#isnull(expr)函数
mysql> select isnull(commission_pct),commission_pct from employees;
#函数对数据判断，如果数据为空返回1，否则返回0
```

### 排序查询

```mysql
/*
 * 排序查询
 * 语法：
 *    select 查询列表
 *    from 表
 *   【where 筛选条件】
 *    order by 排序列表 【asc｜desc】
 *
 *    asc代表升序、desc代表降序。
 *    如果不写，默认是升序
 *    order by可以支持多个字段，可以放函数，表达式、别名
 *    order by子句一般放在最后（limit子句除外）
 */
 
#案例：查询员工信息，按工资从高到低排序
mysql> select * from employees order by salary desc;
#案例：查询员工信息，按工资从低到高排序
mysql> select * from employees order by salary asc; -- 
#案例：查询部门编号大于等于90的员工信息，按照入职的时间进行排序
mysql> select * from employees where department_id>=90 order by hiredate asc;
#案例：按照表达式排序---按照员工年薪的高低显示员工的信息和年薪
mysql> select *,salary*12*(1+ifnull(commission_pct,0)) as 年薪 from employees 
order by salary*12*(1+ifnull(commission_pct,0)) desc;
#案例：按照别名排序---按照员工年薪的高低显示员工的信息和年薪
mysql> select *,salary*12*(1+ifnull(commission_pct,0)) as 年薪 from employees order by 年薪 desc;
#案例：按照函数排序---按姓名的字节长度来显示员工的姓名和工资 
#这里会用到一个函数length(expr)
mysql> select last_name,salary from employees order by length(last_name) desc;
#案例：按照多个字段排序---查询员工信息，先按照工资升序排序、再按照员工编号降序排序
mysql> select * from employees order by salary asc,employee_id desc;
#这样排序，salary是一样的，相同salary的情况下，根据employee_id降序
```

### 常见函数

#### 单行函数

```mysql
/*
 * 语法：
 *  select 函数名(实参列表)
 *    [from   表名];
 *
 * 分类：
 *  1.单行函数
 *      concat(expr1,expr2,...),ifnull(expr1,expr2),isnull(expr),length(expr)等
 *  2.分组函数（做统计使用的，也称为聚集函数）
 *      
 */
 
 /*
  * 单行函数
  * 分类：
  *   字符函数 length,concat,upper/lower,substr,instr,trim,lpad,rpad,replace
  *   数学函数 round,ceil,floor,truncate,mod
  *   日期函数 now,curdate,curtime,year,month,monthname,day,hour,minute,second,str_to_date,data_format
  *   其他函数 version,databse
  *   流程控制函数 if,case
  */
  
  
  
#字符函数
# 1.length(expr) 获取expr的字节个数
mysql>  select length('john');-- 返回4
mysql>  select length('杨云钊'); -- 返回9，因为汉字在utf8占3个字节，一个英文字母占1个字节
  
#查看数据库使用的字符集编码
mysql> show variables like "%char%";
+--------------------------+--------------------------------------------------------+
| Variable_name            | Value                                                  |
+--------------------------+--------------------------------------------------------+
| character_set_client     | utf8mb3    主要看这一项                                |
| character_set_connection | utf8mb3                                                |
| character_set_database   | gb2312                                                 |
| character_set_filesystem | binary                                                 |
| character_set_results    | utf8mb3                                                |
| character_set_server     | utf8mb3                                                |
| character_set_system     | utf8mb3                                                |
| character_sets_dir       | /usr/local/mysql-8.0.28-macos11-x86_64/share/charsets/ |
+--------------------------+--------------------------------------------------------+
  
#2.concat(str1,str2,...)拼接字符串
mysql> select concat(last_name,'_',first_name) from employees;
  
#3.upper(str),lower(str) 大小写转换
mysql> select upper('john');
#案例：将员工的姓变大写，名字变小写拼接
mysql> select concat(upper(last_name),'_',lower(first_name)) from employees;
  
#4.substr/substring. 截取字符串，注意，索引从1开始,注意这里都是字符长度，不是字节
#   substr(str,pos) 截取str从pos字符之后的字符，包含pos字符
mysql> select substr('杨云钊',2);
+-----------------------+
| substr('杨云钊',2)    |
+-----------------------+
| 云钊                  |
+-----------------------+
#   substr(str,pos,len) 截取pos字符之后len个字符
mysql> select substr('杨云钊',2,1);
+-------------------------+
| substr('杨云钊',2,1)    |
+-------------------------+
| 云                      |
+-------------------------+
#案例：员工信息表中，返回员工lastname首字母大写，其他字符小写
mysql> select concat(upper(substr(last_name,1,1)),lower(substr(last_name,2))) from employees;

#5.instr(str,substr) 用于返回substr在str中的第一次出现的起始索引，从1开始，如果没有找到返回0
mysql> select instr('杨云钊','云钊');
+-----------------------------+
| instr('杨云钊','云钊')      |
+-----------------------------+
|                           2 |
+-----------------------------+

#6.trim(str) 去除前后的空格
mysql> select trim('    杨云钊     ') ;
+----------------------------+
| trim('    杨云钊     ')    |
+----------------------------+
| 杨云钊                     |
+----------------------------+
#trim还可以去除指定的字符,还是去掉前后
mysql> select trim(a from 'aaaaaaa杨aa云aa钊aaaaaaa');
+----------------------------------------------+
| trim('a' from 'aaaaaaa杨aa云aa钊aaaaaaa')    |
+----------------------------------------------+
| 杨aa云aa钊                                   |
+----------------------------------------------+

#7.lpad(str,len,c)用指定字符c左填充str，使得其长度达到了len,如果len小于str长度，那就截取
mysql> select lpad(1,10,0);
+--------------+
| lpad(1,10,0) |
+--------------+
| 0000000001   |
+--------------+

#8.rpad(str,len,c)用指定字符c右填充str，使得其长度达到了len,如果len小于str长度，那就截取
mysql> select rpad('yyz',10,'!~');
+---------------------+
| rpad('yyz',10,'!~') |
+---------------------+
| yyz!~!~!~!          |
+---------------------+

#9.replace(str,from_str,to_str)使用to_str替换str中的from_str 切记是全部替换
mysql> select replace('张无忌爱上了周芷若','周芷若','赵敏');
+-------------------------------------------------------------+
| replace('张无忌爱上了周芷若','周芷若','赵敏')               |
+-------------------------------------------------------------+
| 张无忌爱上了赵敏                                            |
+-------------------------------------------------------------+





#数学函数
#1.round(num) 四舍五入
mysql> select round(-1.65); -- 负号不影响，绝对值取整，然后加符号
+-------------+
| round(1.65) |
+-------------+
|           -2|
+-------------+
mysql> select round(1.567,2); -- 第二个参数是小数点后保留2位
+----------------+
| round(1.567,2) |
+----------------+
|           1.57 |
+----------------+

#2.ceil(num)向上取整
mysql> select ceil(1.002);
+-------------+
| ceil(1.002) |
+-------------+
|           2 |
+-------------+
#注意，这里永远向数轴右边最近的整数靠拢
mysql> select ceil(-0.2);
+------------+
| ceil(-0.2) |
+------------+
|          0 |
+------------+

#3.floor(num)向下取整
mysql> select floor(0.8);
+------------+
| floor(0.8) |
+------------+
|          0 |
+------------+
#注意，这里永远向数轴左边边最近的整数靠拢
mysql> select floor(-0.8);
+-------------+
| floor(-0.8) |
+-------------+
|          -1 |
+-------------+

#4.truncate(num,numOfbit) 截断,即数字num小数点后保留numOfBit位
mysql> select truncate(1.699999,1);
+----------------------+
| truncate(1.699999,1) |
+----------------------+
|                  1.6 |
+----------------------+

#5.mod(num1,num2) 取余 和num1%num2一样. 底层实现是 num1-num1/num2*num2
mysql> select mod(10,3); -- 10-(10/3*3)=1
+-----------+
| mod(10,3) |
+-----------+
|         1 |
+-----------+
mysql> select mod(-10,3); -- -10-(-10/3*3)=-1
+------------+
| mod(-10,3) |
+------------+
|         -1 |
+------------+
mysql> select mod(10,-3);  -- 10-(10/(-3)*-3)=1
+------------+
| mod(10,-3) |
+------------+
|          1 |
+------------+
mysql> select mod(-10,-3); -- -10-((-10)/(-3)*(-3))=-1
+-------------+
| mod(-10,-3) |
+-------------+
|          -1 |
+-------------+






#日期函数
#1. now() 返回当前系统日期+时间
mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2022-01-29 21:46:21 |
+---------------------+
#2. curdate() 返回当前系统日期，但是不包含时间
mysql> select curdate();
+------------+
| curdate()  |
+------------+
| 2022-01-29 |
+------------+
#3. curtime() 返回当前时间，不包含日期
mysql> select curtime();
+-----------+
| curtime() |
+-----------+
| 21:48:39  |
+-----------+
#4. 可以获取指定的部分：年year、月month、日day、小时hour、分钟minute、秒second
mysql> select year(now());
+-------------+
| year(now()) |
+-------------+
|        2022 |
+-------------+
mysql> select year('1994-09-19'); -- 19940919、940919、都可以，但是94不行
mysql> select year(hiredate) from employees;
#月、月名
mysql> select month(now());
+--------------+
| month(now()) |
+--------------+
|            1 |
+--------------+
mysql> select monthname(now());
+------------------+
| monthname(now()) |
+------------------+
| January          |
+------------------+


#5. str_to_date 将日期格式的字符串转换成指定格式的日期
mysql> select str_to_date('9-19-1994','%m-%d-%Y'); -- 按照参数中的格式要求解析这个日期
+-------------------------------------+
| str_to_date('9-19-1994','%m-%d-%Y') |
+-------------------------------------+
| 1994-09-19                          |
+-------------------------------------+
mysql> select str_to_date('94-9-19','%y-%c-%d');
+-----------------------------------+
| str_to_date('94-9-19','%y-%c-%d') |
+-----------------------------------+
| 1994-09-19                        |
+-----------------------------------+
#案例：查询入职日期为1992--4-3的员工信息
mysql> select * from employees where hiredate ='1992-4-3'; -- 这样可以查出来
mysql> select * from employees where hiredate =str_to_date('4-3-1992','%c-%d-%Y');

#6. data_format(data,format) 传入一个日期，将一个日期转换为指定格式的字符
mysql> select date_format('1994/09/19','%Y年%m月%d日');
+---------------------------------------------+
| date_format('1994/09/19','%Y年%m月%d日')    |
+---------------------------------------------+
| 1994年09月19日                              |
+---------------------------------------------+
mysql> select date_format(now(),'%y年%c月%d日');
+--------------------------------------+
| date_format(now(),'%y年%c月%d日')    |
+--------------------------------------+
| 22年1月29日                          |
+--------------------------------------+
#案例：查询有奖金员工的姓名和入职日期(xx月/xx日 xx年)
mysql> select last_name,date_format(hiredate ,'%c月%d日 %Y年') from employees where commission_pct is not null;
+------------+-------------------------------------------+
| last_name  | date_format(hiredate ,'%c月%d日 %Y年')    |
+------------+-------------------------------------------+
| Russell    | 12月23日 2002年                           |
| Partners   | 12月23日 2002年                           |
...
+------------+-------------------------------------------+
```

|序号|格式符号|功能|
|--|--|--|
|1|%Y|4位数的年份|
|2|%y|2位数的年份|
|3|%m|月份(01,02,...09,10,11,12)|
|4|%c|月份(1,2,...9,10,11,12)|
|5|%d|日(01,02,...30,31)|
|6|%H|小时(24小时制)|
|7|%h|小时(12小时制)|
|8|%i|分钟(00,01,02,...58,59)|
|9|%s|秒(00,01,02,...59)|

```mysql
#其他函数

#1. 查看数据库版本
mysql> select version();
+-----------+
| version() |
+-----------+
| 8.0.28    |
+-----------+
#2.查看当前的数据库
mysql> select database();
+-------------+
| database()  |
+-------------+
| myemployees |
+-------------+
#3.查看当前的用户
mysql> select user();
+----------------+
| user()         |
+----------------+
| root@localhost |
+----------------+
#4.password(字符) 返回该字符的密码形式，相当于加密
mysql> select password('yyz'); -- 执行不成功
mysql> select md5('yyz');-- md5可以
+----------------------------------+
| md5('yyz')                       |
+----------------------------------+
| 37612607323c2c91f9c38619a76b4176 |
+----------------------------------+


#流程控制函数
#1.if(expr1,expr2,expr3)函数，可以实现if else的效果
#条件表达式expr1是否成立，如果成立就返回expr2，否则返回expr3
mysql> select if(10>5,'大','小');
+----------------------+
| if(10>5,'大','小')   |
+----------------------+
| 大                   |
+----------------------+
mysql> select last_name,commission_pct,if(commission_pct is null,'没奖金','有奖金') from employees;

#2.case函数
# case函数的使用1:
#  语法：
#     case 要判断的字段或表达式
#     when 常量1 then 要显示的值或语句（值不用加分号，语句要加）
#     ...
#     else 要现实的值或语句（默认情况）
#     end

#案例：查询员工的工资：如果部门号为30，显示工资的1.1倍；为40显示1.2倍，50为1.3倍，其余的1倍
select last_name,department_id,salary,
(
  case department_id
  when 30 then 1.1*salary
  when 40 then 1.2*salary
  when 50 then 1.3*salary
  else salary
  end
) as wages
from employees;

# case函数的使用2：类似多重if
#   语法：
#     case
#       when 条件1 then 值/语句;
#       when 条件2 then 值/语句;
#       else 值/语句;
#     end

#案例：查询员工工资，大于等于20000，显示A级别，大于等于15000显示B级别，大于等于10000显示C级别，否则显示D级别
select last_name,
(
  case
  when salary>=20000 then 'A'
  when salary>=15000 then 'B'
  when salary>=10000 then 'C'
  else 'D'
  end
) as class 
from employees;
```

阶段作业

```mysql
#显示系统时间（日期+时间）
mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2022-01-30 17:33:00 |
+---------------------+
#查询员工号，姓名和工资，以及工资提高20%后的结果(new salary)
mysql> select last_name,salary,salary*1.2 as 'new salary' from employees;
#将员工姓名按照首字母排序，并写出姓名的长度
mysql> select last_name,length(last_name) from employees order by substr(last_name,1,1) asc;
#做一个查询，显示下面的结果：
#<last_name> earns <salary> monthlys but wants <salary*3> dream salary
mysql> select concat(last_name,' earns ',salary,' monthly, but wants ',salary*3) as 'dream salary' 
from employees;
#要求使用case when then 实现下面的条件
#job greade （AD_PRES,A）(ST_MAN,B) (IT_PROG,C)
mysql> select 
  case job_id 
  when 'AD_PRES' then 'A' 
  when 'ST_MAN' then 'B' 
  when 'IT_PROG' then 'C' 
  else 'D' 
  end as grade,
  job_id as job 
  from employees;
```

<br/>

#### 分组函数

```mysql
/*
 * 功能：用作统计使用，又称为聚合函数，或统计函数、组函数
 * 分类：
 *    sum求和、avg求平均值，max最大，min最小，count计算个数
 * 特点：
 *    1.sum和avg只支持数值型
 *    2.max、min、count支持任意类型
 *    3.分组函数都忽略了null值进行运算
 *    4.可以和distinct搭配实现去重复
 *    5.count函数详细介绍
 *    6.和分组函数一同查询的字段，一般都是group by的字段，其他都不行
 */
 
#1.简单使用：sum求和，avg求平均值，max，min，count计算条数，非空的值有几个
mysql> select sum(salary),round(avg(salary),2),max(salary),min(salary),count(salary)from employees;
+-------------+----------------------+-------------+-------------+---------------+
| sum(salary) | round(avg(salary),2) | max(salary) | min(salary) | count(salary) |
+-------------+----------------------+-------------+-------------+---------------+
|   691400.00 |              6461.68 |    24000.00 |     2100.00 |           107 |
+-------------+----------------------+-------------+-------------+---------------+
+---------------+
mysql> select count(commission_pct) from employees;
+-----------------------+
| count(commission_pct) |
+-----------------------+
|                    35 |
+-----------------------+

#2.组函数支持哪些参数类型
#sum和avg不支持字符型，日期类型，因为没有意义。
mysql> select sum(last_name),avg(last_name) from employees;
+----------------+----------------+
| sum(last_name) | avg(last_name) |
+----------------+----------------+
|              0 |              0 |
+----------------+----------------+
mysql> select sum(hiredate ),avg(hiredate ) from employees; -- 这样虽然有结果但是没有意义
+------------------+---------------------+
| sum(hiredate )   | avg(hiredate )      |
+------------------+---------------------+
| 2148552443000000 | 20079929373831.7757 |
+------------------+---------------------+
#max和min支持字符型和日期类型
mysql> select max(last_name),min(last_name) from employees;
+----------------+----------------+
| max(last_name) | min(last_name) |
+----------------+----------------+
| Zlotkey        | Abel           |
+----------------+----------------+
mysql> select max(hiredate ),min(hiredate ) from employees;
+---------------------+---------------------+
| max(hiredate )      | min(hiredate )      |
+---------------------+---------------------+
| 2016-03-03 00:00:00 | 1992-04-03 00:00:00 |
+---------------------+---------------------+
#count记非空个数

#3.是否忽略null --- 所有的分组函数都忽略null值
# sum和avg忽略null进行运算
mysql> select sum(commission_pct),avg(commission_pct) from employees;
+---------------------+---------------------+
| sum(commission_pct) | avg(commission_pct) |
+---------------------+---------------------+
|                7.80 |            0.222857 |
+---------------------+---------------------+
#验证
mysql> select sum(commission_pct)/count(commission_pct) from employees where commission_pct is not null;
+-------------------------------------------+
| sum(commission_pct)/count(commission_pct) |
+-------------------------------------------+
|                                  0.222857 |
+-------------------------------------------+
# max和min忽略null进行运算

#4.可以和distinct搭配实现去重复
mysql> select sum(distinct salary),sum(salary) from employees;
+----------------------+-------------+
| sum(distinct salary) | sum(salary) |
+----------------------+-------------+
|            397900.00 |   691400.00 |
+----------------------+-------------+
mysql> select count(distinct salary) ,count(salary)from employees;
+------------------------+---------------+
| count(distinct salary) | count(salary) |
+------------------------+---------------+
|                     57 |           107 |
+------------------------+---------------+

#5.count函数的详细介绍
mysql> select count(salary) from employees;
#统计表中所有的非空列
mysql> select count(*) from employees;
+----------+
| count(*) |
+----------+
|      107 |
+----------+
#count(1/2/3...'a')  这样好比新加了一列全是1，统计1的个数，1的个数就是行数
mysql> select count(1) from employees;
#效率比较
# 在MYISAM存储引擎下，count(*)效率最高，因为该引擎下，有个内部计数器，直接就返回了行数
# 在INNODB存储引擎下，count(*)和count(1)效率差不多，但要高于count(字段)

#6.和分组函数一起查询的字段有限制，必须是group by的字段
select avg(salary),employee_id from employees; -- 这样employee_id没有意义,而且报错

```

作业

```mysql
#查询员工表中的最大入职时间和最小入职时间相差的天数
#这里用到一个函数datediff(expr1,expr2) 前面大后面小
mysql> select datediff('2022-1-30','2022-1-29');
+-----------------------------------+
| datediff('2022-1-30','2022-1-29') |
+-----------------------------------+
|                                 1 |
+-----------------------------------+
mysql> select datediff(now(),'2016-7-29');
+-----------------------------+
| datediff(now(),'2016-7-29') |
+-----------------------------+
|                        2011 |
+-----------------------------+
mysql> select datediff(max(hiredate ),min(hiredate )) as difference from employees;
+------------+
| difference |
+------------+
|       8735 |
+------------+

#查询部门编号为90的员工个数
mysql> select count(*) from employees where department_id=90;
+----------+
| count(*) |
+----------+
|        3 |
+----------+
```

<br/>

<br/>

### 分组查询

```mysql
#引入：查询每个部分的平均工资
mysql> select department_id,avg(salary) as avg_salary,count(*) as people from employees group by department_id;
+---------------+--------------+--------+
| department_id | avg_salary   | people |
+---------------+--------------+--------+
|          NULL |  7000.000000 |      1 |
|            10 |  4400.000000 |      1 |
|            20 |  9500.000000 |      2 |
|            30 |  4150.000000 |      6 |
|            40 |  6500.000000 |      1 |
|            50 |  3475.555556 |     45 |
|            60 |  5760.000000 |      5 |
|            70 | 10000.000000 |      1 |
|            80 |  8955.882353 |     34 |
|            90 | 19333.333333 |      3 |
|           100 |  8600.000000 |      6 |
|           110 | 10150.000000 |      2 |
+---------------+--------------+--------+

/*
 * 语法：
 *    select 列，分组函数
 *      from 表
 *      【where 筛选条件】
 *        group by 分组的列表
 *      【order by 排序的列】;
 *
 * 注意：
 *    1.查询列表必须是groupby 的字段和分组函数
 * 特点：
 *    1.分组查询的筛选条件分为两类，一类是分组前筛选，一种是分组后筛选。
 *                    数据源            位置                  使用关键字
 *      分组前筛选    原始表            group by子句的前面    where
 *      分组后筛选    分组后的结果集    group by子句的后面    having
 *    2.分组函数做条件，一定是放在having子句
 *    3.能用分组前筛选的就优先用where，性能问题。
 *    4.groupby 支持单字段、多字段分组，支持表达式、函数。
 *    5.可以添加排序子句，放在最后
 */
 
#简单的分组查询
#案例：查询每个工种的最高工资
mysql> select job_id,max(salary) from employees group by job_id;
#案例：查询每个location的部门个数
mysql> select location_id,count(department_id) from departments group by location_id; -- count(*)也行

#添加筛选条件的分组查询
#案例：查询邮箱中包含字符a的，每个部门的平均工资
mysql> select department_id,avg(salary) from employees where email like '%a%' group by department_id;
#案例：查询有奖金的，每个领导手下的最高工资
mysql> select manager_id ,max(salary) from employees where commission_pct is not null group by manager_id;
+------------+-------------+
| manager_id | max(salary) |
+------------+-------------+
|        100 |    14000.00 |
|        145 |    10000.00 |
|        146 |    10000.00 |
|        147 |    10500.00 |
|        148 |    11500.00 |
|        149 |    11000.00 |
+------------+-------------+

#添加分组后的筛选条件
#查询哪个部门的员工数目大于2 这使用到了having子句。
#为什么不用where条件，因为where是针对from的表取查的，表中没有people字段，所以要使用having去筛选
#切记，筛选条件在表里用where，不在表里用having
mysql> select department_id ,count(*) as people  from employees group by department_id having (people)>2;
+---------------+--------+
| department_id | people |
+---------------+--------+
|            30 |      6 |
|            50 |     45 |
|            60 |      5 |
|            80 |     34 |
|            90 |      3 |
|           100 |      6 |
+---------------+--------+
#查询每个工种有奖金的员工的最高工资》12000的工种id和最高工资
mysql> select job_id,max(salary) as maxsalary  from employees where commission_pct is not null group by job_id having maxsalary>12000;
+--------+-----------+
| job_id | maxsalary |
+--------+-----------+
| SA_MAN |  14000.00 |
+--------+-----------+
#查询领导编号》102的每个领导手下的最低工资》5000的领导编号是哪个？
mysql> select manager_id from employees where manager_id >102 group by manager_id having min(salary)>5000;
+------------+
| manager_id |
+------------+
|        108 |
|        145 |
|        146 |
|        147 |
|        148 |
|        149 |
|        201 |
|        205 |
+------------+


#按照表达式或者函数分组
#按照员工姓名长度进行分组，查询每一组的员工个数，筛选员工个数》5的有几个
mysql> select length(last_name) as len,count(*)from employees group by len having count(*)>5;
+------+----------+
| len  | count(*) |
+------+----------+
|    5 |       29 |
|    7 |       15 |
|    6 |       28 |
|    9 |        8 |
|    4 |       11 |
|    8 |        7 |
+------+----------+


#按多个字段分组 多个字段都放在group by后面
#案例：查询每个部门、每个工种的员工的平均工资
mysql> select department_id,job_id ,avg(salary) from employees group by department_id,job_id;


#添加排序
#案例：查询每个部门、每个工种的员工的平均工资，从高到低展示
mysql> select department_id,job_id ,avg(salary) from employees group by department_id,job_id 
order by avg(salary) desc;
```

作业

```mysql
#1.查询job_id的员工工资的最大值和最小值，平均值，总和，按照job_id升序
mysql> select job_id,max(salary),min(salary) ,avg(salary) ,sum(salary)from employees 
group by job_id 
order by job_id asc;
+------------+-------------+-------------+--------------+-------------+
| job_id     | max(salary) | min(salary) | avg(salary)  | sum(salary) |
+------------+-------------+-------------+--------------+-------------+
| AC_ACCOUNT |     8300.00 |     8300.00 |  8300.000000 |     8300.00 |
| AC_MGR     |    12000.00 |    12000.00 | 12000.000000 |    12000.00 |
| AD_ASST    |     4400.00 |     4400.00 |  4400.000000 |     4400.00 |
| AD_PRES    |    24000.00 |    24000.00 | 24000.000000 |    24000.00 |
| AD_VP      |    17000.00 |    17000.00 | 17000.000000 |    34000.00 |
| FI_ACCOUNT |     9000.00 |     6900.00 |  7920.000000 |    39600.00 |
| FI_MGR     |    12000.00 |    12000.00 | 12000.000000 |    12000.00 |
| HR_REP     |     6500.00 |     6500.00 |  6500.000000 |     6500.00 |
| IT_PROG    |     9000.00 |     4200.00 |  5760.000000 |    28800.00 |
| MK_MAN     |    13000.00 |    13000.00 | 13000.000000 |    13000.00 |
| MK_REP     |     6000.00 |     6000.00 |  6000.000000 |     6000.00 |
| PR_REP     |    10000.00 |    10000.00 | 10000.000000 |    10000.00 |
| PU_CLERK   |     3100.00 |     2500.00 |  2780.000000 |    13900.00 |
| PU_MAN     |    11000.00 |    11000.00 | 11000.000000 |    11000.00 |
| SA_MAN     |    14000.00 |    10500.00 | 12200.000000 |    61000.00 |
| SA_REP     |    11500.00 |     6100.00 |  8350.000000 |   250500.00 |
| SH_CLERK   |     4200.00 |     2500.00 |  3215.000000 |    64300.00 |
| ST_CLERK   |     3600.00 |     2100.00 |  2785.000000 |    55700.00 |
| ST_MAN     |     8200.00 |     5800.00 |  7280.000000 |    36400.00 |
+------------+-------------+-------------+--------------+-------------+
#2.查询各个管理者手下员工的最低工资，其中最低工资不能低于6000，没有管理者的员工不计算
mysql> select manager_id,min(salary) from employees where manager_id is not null group by manager_id having min(salary)>=6000;
+------------+-------------+
| manager_id | min(salary) |
+------------+-------------+
|        102 |     9000.00 |
|        108 |     6900.00 |
|        145 |     7000.00 |
|        146 |     7000.00 |
|        147 |     6200.00 |
|        148 |     6100.00 |
|        149 |     6200.00 |
|        201 |     6000.00 |
|        205 |     8300.00 |
+------------+-------------+
#3.查询每个部门的编号，员工数量和工资平均值，并按照平均工资降序排列
mysql> select department_id ,count(*) as people ,avg(salary)as avg from employees group by department_id order by avg desc;
+---------------+--------+--------------+
| department_id | people | avg          |
+---------------+--------+--------------+
|            90 |      3 | 19333.333333 |
|           110 |      2 | 10150.000000 |
|            70 |      1 | 10000.000000 |
|            20 |      2 |  9500.000000 |
|            80 |     34 |  8955.882353 |
|           100 |      6 |  8600.000000 |
|          NULL |      1 |  7000.000000 |
|            40 |      1 |  6500.000000 |
|            60 |      5 |  5760.000000 |
|            10 |      1 |  4400.000000 |
|            30 |      6 |  4150.000000 |
|            50 |     45 |  3475.555556 |
+---------------+--------+--------------+
```

<br/>

<br/>

### 连接查询

```mysql
/*
 * 连接查询又称为多表查询,当查询的字段来自于多个表的时候，就会用到连接查询
 * 笛卡尔乘积现象：表1有m行，表2有n行，最后有m*n行查询数据
 *    发生原因：没有有效的连接条件，要添加有效的连接条件
 *    
 * 分类：
 *    按照年代分类：
 *        sql92标准：只支持内连接
 *        sql99标准(推荐)  ：支持内连接、外连接（左外+右外），交叉连接
 *    按功能分类：
 *        内连接
 *            等值连接
 *            非等值连接
 *            自连接
 *        外连接
 *            左外连接
 *            右外连接
 *            全外连接
 *        交叉连接
 */
 
#这里使用到一个新的数据库girls.sql;
mysql> desc beauty;
+--------------+-------------+------+-----+---------------------+----------------+
| Field        | Type        | Null | Key | Default             | Extra          |
+--------------+-------------+------+-----+---------------------+----------------+
| id           | int         | NO   | PRI | NULL                | auto_increment |
| name         | varchar(50) | NO   |     | NULL                |                |
| sex          | char(1)     | YES  |     | 女                  |                |
| borndate     | datetime    | YES  |     | 1987-01-01 00:00:00 |                |
| phone        | varchar(11) | NO   |     | NULL                |                |
| photo        | blob        | YES  |     | NULL                |                |
| boyfriend_id | int         | YES  |     | NULL                |                |
+--------------+-------------+------+-----+---------------------+----------------+
mysql> desc boys;
+---------+-------------+------+-----+---------+----------------+
| Field   | Type        | Null | Key | Default | Extra          |
+---------+-------------+------+-----+---------+----------------+
| id      | int         | NO   | PRI | NULL    | auto_increment |
| boyName | varchar(20) | YES  |     | NULL    |                |
| userCP  | int         | YES  |     | NULL    |                |
+---------+-------------+------+-----+---------+----------------+

#现在要查询每个beauty表中女生对应的男朋友
mysql> select name,boyName from beauty,boys; -- 这样写不对，因为每个女生都会匹配boys表中的男生，也就是笛卡尔积
#加上有效的连接条件
mysql> select boyName,name from boys,beauty where boys.id=beauty.boyfriend_id;
+-----------+------------+
| boyName   | name       |
+-----------+------------+
| 黄晓明    | Angelababy |
| 鹿晗      | 热巴       |
| 张无忌    | 周芷若     |
| 张无忌    | 小昭       |
| 段誉      | 王语嫣     |
| 张无忌    | 赵敏       |
+-----------+------------+
```

#### sql92标准

```mysql
#支持所有的内连接
#等值连接
/*
 * 总结：
 *    1.多表等值连接的结果是多表的交集部分
 *    2.n表连接至少需要n-1个连接条件
 *    3.多表的顺序没有要求
 *    4.一般需要为表起别名
 *    5.可以搭配排序，分组、筛选使用
 */
#1.实现原理：用表1中的id字段和表2中的boyfriend_id字段去匹配，相同的话，就组装成一条数据
#案例：查询所有的女生和对应的男友名字
mysql> select boyName,name from boys,beauty where boys.id=beauty.boyfriend_id;
#案例：查询员工名对于的部门名字
mysql> select last_name,department_name from employees,departments 
where employees.department_id=departments.department_id;

#2.为表起别名，写起来更方便,区分重名字段。
#注意，如果为表起了别名，相当于生成了对应表的一个视图，去查生成的视图，所以不能再用表名取限定字段！！！
#案例：查询员工号，工种号和工种名,注意这里的job_id两个表都有，有二义性，所以加表名
mysql> select last_name,jobs.job_id,job_title from jobs,employees where employees.job_id=jobs.job_id;
mysql> select e.last_name,e.job_id,j.job_title 
from employees as e,jobs as j 
where e.job_id=j.job_id;

#3.两个表的顺序是否可以调换：可以

#4.内连接时候，可以加筛选条件
#案例：查询有奖金的员工名和部门名字
mysql> select e.last_name,d.department_name from employees as e,departments as d 
where e.department_id=d.department_id 
and e.commission_pct is not null;
#案例：查询城市名中第二个字符为o的部门名字和城市名
mysql> select d.department_name,l.city from departments as d,locations as l where d.location_id=l.location_id and l.city like '_o%';
+-----------------+---------------------+
| department_name | city                |
+-----------------+---------------------+
| IT              | Southlake           |
| Shi             | South San Francisco |
| Mar             | Toronto             |
| Hum             | London              |
+-----------------+---------------------+

#5.可以加分组
#案例：查询每个城市的部门个数
mysql> select l.city ,count(*) from locations as l,departments as d 
where l.location_id=d.location_id group by l.city;
+---------------------+----------+
| city                | count(*) |
+---------------------+----------+
| Southlake           |        1 |
| South San Francisco |        1 |
| Seattle             |       21 |
| Toronto             |        1 |
| London              |        1 |
| Oxford              |        1 |
| Munich              |        1 |
+---------------------+----------+
#案例：查询有奖金的每个部门的部门名、部门领导编号和该部门的最低工资
mysql> select d.department_name,d.manager_id,min(e.salary) 
from departments as d,employees as e 
where d.department_id=e.department_id and e.commission_pct is not null  
group by d.department_id;
+-----------------+------------+---------------+
| department_name | manager_id | min(e.salary) |
+-----------------+------------+---------------+
| Sal             |        145 |       6100.00 |
+-----------------+------------+---------------+

#6.可以加排序
#案例：查询每个工种的工种名和员工个数，并且按照员工个数降序
mysql> select j.job_title,count(*) 
from jobs as j,employees as e 
where j.job_id=e.job_id 
group by j.job_title order by count(*) desc;
+---------------------------------+----------+
| job_title                       | count(*) |
+---------------------------------+----------+
| Sales Representative            |       30 |
| Shipping Clerk                  |       20 |
| Stock Clerk                     |       20 |
| Accountant                      |        5 |
| Programmer                      |        5 |
| Purchasing Clerk                |        5 |
| Sales Manager                   |        5 |
| Stock Manager                   |        5 |
| Administration Vice President   |        2 |
| Public Accountant               |        1 |
| Accounting Manager              |        1 |
| Administration Assistant        |        1 |
| President                       |        1 |
| Finance Manager                 |        1 |
| Human Resources Representative  |        1 |
| Marketing Manager               |        1 |
| Marketing Representative        |        1 |
| Public Relations Representative |        1 |
| Purchasing Manager              |        1 |
+---------------------------------+----------+

#7.实现3表连接
#案例：查询员工名，部门名和所在的城市
mysql> select e.last_name,d.department_name,l.city 
from employees as e,departments as d,locations as l 
where e.department_id=d.department_id and d.location_id=l.location_id;

#----------------------------------------------------------------------------------------------
#非等值连接（反正不是等号）
#案例：查询员工的工资和工资级别
#这里需要引入一张表
create table job_grades
(grade_level varchar(3),
lowest_sal int,
highest_sal int);
insert into job_grades values('A',1000,2999);
insert into job_grades values('B',3000,5999);
insert into job_grades values('C',6000,9999);
insert into job_grades values('D',10000,14999);
insert into job_grades values('E',15000,24999);
insert into job_grades values('F',25000,40000);
#开始查询
mysql> select e.employee_id,e.salary,jg.grade_level 
from employees as e,job_grades as jg 
where e.salary between jg.lowest_sal and jg.highest_sal;
+-------------+----------+-------------+
| employee_id | salary   | grade_level |
+-------------+----------+-------------+
|         100 | 24000.00 | E           |
|         101 | 17000.00 | E           |
...


#----------------------------------------------------------------------------------------------
#自连接：相当于等值连接，但是自己连接自己
#案例：查询员工名字和他上级的名字,注意这里要连接同一张表
mysql> select e.last_name,m.last_name from employees as e,employees as m where e.manager_id=m.employee_id;

```

作业

```mysql
#1.显示所有员工的姓名、部门号和部门名称
mysql> select e.last_name,d.department_id,d.department_name 
from employees as e,departments as d 
where e.department_id=d.department_id;
#2.查询部门号是90的员工的job_id和90号部门的location_id
mysql> select e.job_id,d.location_id  
from employees as e,departments as d  
where e.department_id=d.department_id and d.department_id=90;
+---------+-------------+
| job_id  | location_id |
+---------+-------------+
| AD_PRES |        1700 |
| AD_VP   |        1700 |
| AD_VP   |        1700 |
+---------+-------------+
#3.查询所有有奖金员工的last_name,department_name,location_id,city
mysql> select e.last_name,d.department_name,d.location_id,l.city 
from employees as e,departments as d,locations as l 
where e.department_id=d.department_id and d.location_id=l.location_id and e.commission_pct is not null;
#4.查询在城市Toronto工作的员工的last_name,job_id,department_id,department_name
mysql> select e.last_name,e.job_id,e.department_id,d.department_name 
from employees as e ,departments as d,locations as l   
where e.department_id=d.department_id and d.location_id=l.location_id and l.city='Toronto';
#5.查询每个工种，每个部门的部门名字，工种名字和最低工资
mysql> select d.department_name,j.job_title,min(e.salary) 
from departments as d,jobs as j, employees as e 
where d.department_id=e.department_id and j.job_id=e.job_id group by department_name,j.job_title;
+-----------------+---------------------------------+---------------+
| department_name | job_title                       | min(e.salary) |
+-----------------+---------------------------------+---------------+
| Acc             | Public Accountant               |       8300.00 |
| Acc             | Accounting Manager              |      12000.00 |
| Adm             | Administration Assistant        |       4400.00 |
| Exe             | President                       |      24000.00 |
| Exe             | Administration Vice President   |      17000.00 |
| Fin             | Accountant                      |       6900.00 |
| Fin             | Finance Manager                 |      12000.00 |
| Hum             | Human Resources Representative  |       6500.00 |
| IT              | Programmer                      |       4200.00 |
| Mar             | Marketing Manager               |      13000.00 |
| Mar             | Marketing Representative        |       6000.00 |
| Pub             | Public Relations Representative |      10000.00 |
| Pur             | Purchasing Clerk                |       2500.00 |
| Pur             | Purchasing Manager              |      11000.00 |
| Sal             | Sales Manager                   |      10500.00 |
| Sal             | Sales Representative            |       6100.00 |
| Shi             | Shipping Clerk                  |       2500.00 |
| Shi             | Stock Clerk                     |       2100.00 |
| Shi             | Stock Manager                   |       5800.00 |
+-----------------+---------------------------------+---------------+
#6.查询每个国家下的部门个数大于2的国家编号
mysql> select l.country_id,count(*) 
from locations as l,departments as d  
where l.location_id=d.location_id  
group by l.country_id 
having count(*)>2;
+------------+----------+
| country_id | count(*) |
+------------+----------+
| US         |       23 |
+------------+----------+
#7.选择制定员工姓名，员工号，以及他的管理者姓名和员工号
mysql> select e.last_name ,e.employee_id ,m.last_name ,m.employee_id 
from employees as e ,employees as m 
where e.manager_id=m.employee_id;
```

<br/>

#### sql99标准

```mysql
/*
 *  语法：
 *    select 查询列表
 *    from 表1 as 别名
 *    【连接类型】join 表2 on 连接条件
 *    【where 筛选条件】
 *    【group by 分组】
 *    【having 筛选条件】
 *    【order by 排序列表】;
 *
 *
 *  内连接（重点）inner
 *  外连接
 *    左外连接（重点）:left [outer]
 *    右外连接（重点）:right [outer]
 *    全外连接:full [outer]
 *  交叉连接 cross
 *
 *  特点：
 *    1.添加排序、分组、筛选
 *    2.inner可以省略
 *    3.筛选条件放在where后面，连接条件放在on后面，提高了分离性，便于阅读
 *    4.inner join 和sql92中的等值连接实现效果相同，都是查询多张表的交集部分
 
 *
 *
 */
 
#---------------------------------------------------------------------------------------------- 
#内连接：包含等值连接、非等值连接，自连接
 
#案例：查询员工名，部门名 和92语法底层原理一样
mysql> select e.last_name,d.department_name  
  -> from employees as e inner join departments as d
  -> on e.department_id=d.department_id;
#案例：查询名字中包含e的员工名和工种名字
mysql> select e.last_name ,j.job_title
    -> from employees as e
    -> inner join jobs as j on e.job_id=j.job_id
    -> where e.last_name like '%e%' ;
#案例：查询部门个数大于3的城市名和部门个数
mysql> select l.city,count(*)
    -> from locations as l
    -> inner join departments as d on d.location_id=l.location_id
    -> group by l.city
    -> having count(*)>3;
+---------+----------+
| city    | count(*) |
+---------+----------+
| Seattle |       21 |
+---------+----------+
#案例：查询哪个部门的部门员工个数》3的部门名和员工数，并按照人数降序排列
mysql> select d.department_name,count(*)
    -> from departments as d
    -> inner join employees as e on d.department_id=e.department_id
    -> group by department_name
    -> having count(*)>3
    -> order by count(*) desc;
+-----------------+----------+
| department_name | count(*) |
+-----------------+----------+
| Shi             |       45 |
| Sal             |       34 |
| Pur             |        6 |
| Fin             |        6 |
| IT              |        5 |
+-----------------+----------+
#案例：查询员工名，部门名字，工种名字，按照部门名字降序
mysql> select e.last_name,d.department_name,j.job_title
    -> from employees as e
    -> inner join departments as d on e.department_id=d.department_id
    -> inner join jobs as j on j.job_id=e.job_id
    -> order by department_name desc;
    
#非等值连接
#案例：查询员工的工资级别
mysql> select e.last_name,e.salary,jg.grade_level
    -> from employees as e
    -> inner join job_grades as jg on e.salary between jg.lowest_sal and jg.highest_sal;
#案例：查询每个工资级别的人数大于2，并按照工资级别降序排列
mysql> select jg.grade_level ,count(*) as num
    -> from employees as e
    -> inner join job_grades as jg on e.salary between jg.lowest_sal and jg.highest_sal
    -> group by jg.grade_level
    -> having num>2
    -> order by jg.grade_level desc;

#自连接
#案例：查询员工的名字和他上司的名字
mysql> select e.last_name,m.last_name
    -> from employees as e
    -> inner join employees as m on e.manager_id=m.employee_id;
    
    
  
#----------------------------------------------------------------------------------------------
#外连接
/*
 *  应用场景：用户查询一个表中有，另外一个表中没有对应数据的情况
 *  特点：
 *    1.外连接的查询结果是‘主表’中的所有记录，
 *      如果‘从表’中有和它匹配的，就显示匹配的值
 *      如果‘从表’中没有和它匹配的，就显示null
 *    总之，外连接查询结果：内连接查询结果+主表中有而从表中没有的记录
 *    2.左外连接：left outer join 左边的是主表
 *      右外连接：right outer join 右边的是主表
 *    3.左外连接和右外连接交换表的顺序可以实现一样的效果
 *    4.全外连接（不支持）：内连接结果+表1中有的但表2中没有的+表1中没有的但是表2中有的
 */
#引入：查询男朋友不在男神表的女生名字
mysql> select b.name 
from beauty as b 
left join boys as bo on b.boyfriend_id=bo.id 
where bo.id is null; -- 这里的筛选条件必须选一个非空的字段，否则筛选会有问题
+-----------+
| name      |
+-----------+
| 柳岩      |
| 苍老师    |
| 周冬雨    |
| 岳灵珊    |
| 双儿      |
| 夏雪      |
+-----------+
#这道题使用右外连接也可以
mysql> select be.name 
from boys as bo  
right join beauty as be  on bo.id=be.boyfriend_id 
where bo.id is null;

#案例：查询哪个部门没有员工（这里的主表是departments，拿着id取匹配emp表，如果没有匹配到就是这个部门没有人）
mysql> select d.department_id,d.department_name,e.department_id 
from departments as d 
left join employees as e on d.department_id=e.department_id 
where e.employee_id is null;
+---------------+-----------------+---------------+
| department_id | department_name | department_id |
+---------------+-----------------+---------------+
|           120 | Tre             |          NULL |
|           130 | Cor             |          NULL |
|           140 | Con             |          NULL |
|           150 | Sha             |          NULL |
|           160 | Ben             |          NULL |
|           170 | Man             |          NULL |
|           180 | Con             |          NULL |
|           190 | Con             |          NULL |
|           200 | Ope             |          NULL |
|           210 | IT              |          NULL |
|           220 | NOC             |          NULL |
|           230 | IT              |          NULL |
|           240 | Gov             |          NULL |
|           250 | Ret             |          NULL |
|           260 | Rec             |          NULL |
|           270 | Pay             |          NULL |
+---------------+-----------------+---------------+
#这里使用右外做
mysql> select d.department_id,d.department_name from employees as e
    -> right outer join departments as d on e.department_id=d.department_id
    -> where e.employee_id is null;
    
#----------------------------------------------------------------------------------------------
#交叉连接，相当于两张表取笛卡尔乘积,使用99语法的标准实现笛卡尔乘积
mysql> select be.*,bo.* from beauty as be
    -> cross join boys as bo

```

#### sql92和sql99的对比

功能：sql99支持的比较多

可读性：sql99实现了连接条件和筛选条件的分离

作业

```mysql
#1.查询编号大于3的女神的男朋友信息，如果有就详细列出，如果没有就用null表示
mysql> select be.id,be.name ,bo.* 
from beauty as be 
left join boys as bo on be.boyfriend_id=bo.id 
where be.id>3;
+----+-----------+------+-----------+--------+
| id | name      | id   | boyName   | userCP |
+----+-----------+------+-----------+--------+
|  4 | 热巴      |    2 | 鹿晗      |    800 |
|  5 | 周冬雨    | NULL | NULL      |   NULL |
|  6 | 周芷若    |    1 | 张无忌    |    100 |
|  7 | 岳灵珊    | NULL | NULL      |   NULL |
|  8 | 小昭      |    1 | 张无忌    |    100 |
|  9 | 双儿      | NULL | NULL      |   NULL |
| 10 | 王语嫣    |    4 | 段誉      |    300 |
| 11 | 夏雪      | NULL | NULL      |   NULL |
| 12 | 赵敏      |    1 | 张无忌    |    100 |
+----+-----------+------+-----------+--------+
#2.查询哪个城市没有部门
mysql> select l.city,d.department_id 
from locations as l 
left join departments as d on l.location_id=d.location_id 
where department_id is null;
+-----------------+---------------+
| city            | department_id |
+-----------------+---------------+
| Roma            |          NULL |
| Venice          |          NULL |
| Tokyo           |          NULL |
| Hiroshima       |          NULL |
| South Brunswick |          NULL |
| Whitehorse      |          NULL |
| Beijing         |          NULL |
| Bombay          |          NULL |
| Sydney          |          NULL |
| Singapore       |          NULL |
| Stretford       |          NULL |
| Sao Paulo       |          NULL |
| Geneva          |          NULL |
| Bern            |          NULL |
| Utrecht         |          NULL |
| Mexico City     |          NULL |
+-----------------+---------------+
#3.查询部门名字为SAL或者IT的员工信息,注意，部门可能没有员工，所以使用内连接不太合适
mysql> select e.* 
from departments as d 
left join employees as e on d.department_id=e.department_id 
where d.department_name in('Sal','IT');
```

<br/>

<br/>

### 子查询（有难度）

含义：出现在**其他**语句中的select语句，称为子查询或内查询。外部的查询语句称为主查询或者外查询。

分类：

	按照子查询出现的位置分类：

		1.放在select后面

				只支持标量子查询

		2.放在from后面

				支持表子查询

**		3.放在where和having后面**

**				支持标量子查询（单行）**

**				支持列子查询（多行）**子查询去重复一下提高效率

				支持行子查询

		4.放在exists后面（相关子查询）

				支持表子查询

	按照结果集的行列数不同分类：

		1.标量子查询（结果集只有一行一列）

		2.列子查询（结果集有一列多行）

		3.行子查询（结果集有一行多列）

		4.表子查询（结果集，行列无所谓）

```mysql
#----------------------------------------------------------------------------------------------
#放在where和having后面的
/*
 *  特点：
 *    1.子查询放在括号内
 *    2.子查询一般放在条件的右侧
 *    3.标量子查询一般配合单行操作符使用：>,< =
 *    4.列子查询一般配合多行操作符使用：IN，ANY/SOME（可用max/min代替,大于最小的，小于最大的），
 *    ALL（可用max/min代替,大于最大的，小于最小的）
 *    5.子查询的执行要优先于主查询的执行
 *
 */
 
#1.标量子查询（单行子查询）

#案例：谁的工资比Abel高
#解析：首先查到Abel的工资是多少，然后把它作为条件
mysql> select salary from employees where last_name='Abel';-- 这个结果是一行一列，所以是标量子查询
+----------+
| salary   |
+----------+
| 11000.00 |
+----------+
mysql> select last_name 
from employees 
where salary>(select salary from employees where last_name='Abel');

#案例：返回job_id和141号员工相同，且salary比143号员工多的员工姓名和，job_id和工资
#解析：首先找到141号员工的job_id 和 143号员工的salary
mysql> select last_name,job_id,salary 
from employees 
where job_id=(select job_id from employees where employee_id=141) 
and salary>(select salary from employees where employee_id=143);

#案例：返回公司工资最少的员工的名字，job_id和salary
#解析：先查到最小工资，拿着工资值取找员工的姓名和job_id
mysql> select last_name,job_id,salary 
from employees where salary=(select min(salary) from employees);


#案例：查询最低工资大于50号部门最低工资的部门id和最低工资
#解析：先根据部门id和最低工资分组，然后查询50号部门的最低工资用来筛选
mysql> select department_id,min(salary)as minsal 
from employees 
group by department_id 
having minsal>(select min(salary) from employees where department_id=50);


#非法使用标量子查询
mysql> select department_id,min(salary)as minsal 
from employees 
group by department_id 
having minsal>(select salary from employees where department_id=50); -- 子查询结果是多行
#
mysql> select department_id,min(salary)as minsal 
from employees 
group by department_id 
having minsal>(select salary from employees where department_id=5555550); -- 子查询结果为空

#2.列子查询（多行子查询：一列多行）小技巧，子查询去重复一下提高效率

#案例：返回location_id是1400或者1700的部门中的所有员工姓名
#解析：先找到location_id是1400和1700的department_id，然后去查员工姓名
mysql> select last_name 
from employees 
where department_id in
(select distinct department_id from locations where location_id in (1400,1700)); -- 子查询最好去重，效率
#可以使用any进行替换
mysql> select last_name 
from employees 
where department_id =any
(select distinct department_id from locations where location_id in (1400,1700));
#如果原来是not in 可以使用<>all替换

#案例：返回其他工种中比job_id为‘IT_PROG’部门任一工资低的员工号，姓名，job_id,以及salary
mysql> select employee_id,last_name,job_id,salary 
from employees 
where salary<any(select distinct salary from employees where job_id='IT_PROG') 
and job_id <>'IT_PROG';
#使用max函数替代，大于最小，小于最大
mysql> select employee_id,last_name,job_id,salary 
from employees 
where salary<(select max(salary) from employees where job_id='IT_PROG') 
and job_id <>'IT_PROG';

#案例：返回其他工种中比job_id为‘IT_PROG’部门所有工资低的员工号，姓名，job_id,以及salary
mysql> select employee_id,last_name,job_id,salary from employees 
where salary<all(select distinct salary from employees where job_id='IT_PROG') 
and job_id !='IT_PROG';
#使用min函数替换，大于最大的，小于最小的
mysql> select employee_id,last_name,job_id,salary from employees 
where salary<(select min(salary) from employees where job_id='IT_PROG') 
and job_id !='IT_PROG';


#3.行子查询（单行多列）

#引入：查出员工编号最小，工资最高的员工信息（别管存不存在）
#解析：先找出员工编号最小的，再找出工资最高的，因为这里是两个字段所以是多列,最后进行筛选
#献给出来普通的做法
mysql> select * from employees
where employee_id=(select min(employee_id) from employees) 
and salary=(select max(salary) from employees);
#行子查询：因为上面两个筛选条件都是使用的相同的运算符，所以可以合并起来作为行子查询
ysql> select * from employees 
where (employee_id,salary)=(select min(employee_id),max(salary) from employees);




#----------------------------------------------------------------------------------------------
#放在select后面的子查询
/*
 *  只支持标量子查询，子查询返回只能是一行一列
 *
 *
 */
#引入：查询每个部门的员工个数，有的部门可能没有员工
#解析：这里要得到部门的信息+部门多少人，注意筛选条件都在子查询语句里面
mysql> select d.*,(select count(*) from employees as e where e.department_id=d.department_id) 
from departments as d;

#案例：查询员工好102的员工所在的部门名字
select 
(
select d.department_name 
from employees as e 
left join departments as d on e.department_id = d.department_id 
where employee_id=102;
); -- 鸡肋



#----------------------------------------------------------------------------------------------
#放在from后面的子查询
/*
 *  将子查询的结果集充当了一个表,要求必须起别名
 *
 */
 
 #案例：查询每个部门的平均工资的工资等级
 #解析：首先根据部门分组，算平均工资，这个作为结果集。和等级表非等值连接查询
 mysql> select avg_dep.department_id,avg_dep.avgsal,jg.grade_level 
 from job_grades as jg,
 (select department_id,avg(salary) as avgsal from employees group by department_id) as avg_dep 
 where avg_dep.avgsal between jg.lowest_sal and jg.highest_sal; -- 最后一定要加上连接条件
 #99语法来一遍
 mysql> select avg_dep.*,jg.grade_level  
 from (select department_id,avg(salary) as avgsal from employees group by department_id) as avg_dep 
 inner join job_grades as jg on avg_dep.avgsal between jg.lowest_sal and jg.highest_sal;
 
 
#----------------------------------------------------------------------------------------------
#放在exists后面的子查询(相关子查询)
/*
 *  exists(完整查询语句)表示是否存在，函数只关心有没有值，有的话返回1，没有的话返回0
 *  含exists的子查询和其他的不一样，先执行外查询，再执行子查询，用条件去过滤
 *  相关的含义就是，子查询涉及到了主查询的字段
 
 *
 */
#案例：查询有员工的部门名
mysql> select d.department_name  from departments as d
    -> where exists(select * from employees as e where d.department_id=e.department_id);
+-----------------+
| department_name |
+-----------------+
| Adm             |
| Mar             |
| Pur             |
| Hum             |
| Shi             |
| IT              |
| Pub             |
| Sal             |
| Exe             |
| Fin             |
| Acc             |
+-----------------+
#使用in来代替
mysql> select department_name from departments 
where department_id in(select distinct department_id from employees);

#案例：查询没有女朋友的男神信息
mysql> select bo.* 
from boys as bo 
where not exists(select * from beauty as be where bo.id=be.boyfriend_id);
#使用in来实现
mysql> select bo.* from boys as bo
    -> where bo.id not in(select boyfriend_id from beauty);
```

作业

```mysql
#1.查询和Zlotkey相同部门的员工姓名和工资
mysql> select e.last_name,e.salary 
from employees as e  
where e.department_id=(select department_id from employees where last_name='Zlotkey');

#2.查询工资比公司平均工资高的员工的员工号，姓名和工资
mysql> select e.employee_id,e.last_name,e.salary 
from employees as e 
where e.salary>(select avg(salary) from employees);

#3.查询各部门中工资比本部门平均工资高的员工的工号，姓名和工资
#先查询本部门的平均工资
select department_id,avg(salary) as avgsal from employees group by department_id;
#再根据部门号对员工的工资进行分组
#这里需要连接两张表，所以把第一个的结果作为表比较合适
select e.employee_id,e.department_id,e.last_name,e.salary from employees as e,
(select department_id,avg(salary) as avgsal from employees group by department_id) as avg_dep 
where avg_dep.department_id=e.department_id and e.salary>avg_dep.avgsal ;

#4.查询和姓名中包含字母u的员工在相同部门员工号和姓名
mysql> select e.employee_id,e.last_name 
from employees as e 
where e.department_id in
  (select distinct department_id from employees where last_name like '%u%');
  
#5.查询在部门location_id为1700的部门工作的员工的员工号
mysql> select e.employee_id 
from employees as e 
where e.department_id in
 (select distinct department_id from departments where location_id=1700); -- 这里可以使用any
 
mysql> select e.employee_id 
from employees as e 
where e.department_id =
 any(select distinct department_id from departments where location_id=1700); 
 
#6.查询员工姓名是K_ing的员工姓名和工资(这里有重名，K_ing有两个人)
mysql> select last_name,salary 
from employees 
where manager_id=any(select distinct employee_id from employees where last_name='K_ing');

#7.查询工资最高的员工姓名，要求first_name和last_name显示在一列，列名为姓名
mysql> select concat(first_name," ",last_name ) as 姓名  
from employees where salary=(select max(salary) from employees );
```

<br/>

### 分页查询

应用场景：当要显示的数据一页显示不全，就要分页提交sql请求

```mysql
/*
 *  语法：
 *    select 查询列表
 *    from 表
 *    【join type join 表2  on 连接条件】
 *    where 筛选条件
 *    group by 分组字段
 *    havig 分组后的筛选
 *    order by 排序字段
 *    limit [offset，]size；
 *
 *  注意这里，offset要从0开始，和mysql其他的不太一样
 *  特点：
 *    1.limit语句放在查询语句的最后，执行顺序也在最后
 *    2.公式：要现实的页数是page，每页的条目数字是size ：limit (page-1)*size，size 
 *
 */
 
#案例：查询前5条员工信息
mysql> select * from employees limit 5;-- 相当于limit 0，5
#案例：要查询第11条到第25条员工信息(11-25条一共有15条，起始索引是10)
mysql> select * from employees limit 10,15;
#有奖金的员工信息，且工资较高的前10名显示出来
mysql> select * from employees where commission_pct is not null order by salary desc limit 0,10;
```

作业

```mysql
/*
 *  已知表stuinfo
 *  id学号，name姓名，email邮箱（join@126.com），gradeId年级编号，sex性别（男，女），age年龄
 *  已知表grade
 *  id年级编号，gardeName年级名称
 */
#1.查询所有学员邮箱的用户名
select substr(email,1,instr(email,'@')-1) from stuinfo;
#2.查询男女个数
select sex,count(*) from stuinfo group by sex;
#3.查询所有年龄大于18的学生姓名和年级名
select s.name,g.gradeName from stuinfo as s
inner join grade as g on g.id=s.gradeId
where s.age>18;
#4.查询哪个年级的学生最小年龄大于20岁
select s.gradeId,g.gradeName s.min(age) from stuinfo as s
inner join grade as g on g.id=s.gradeId
group by s.gradeId s.having min(age)>20;

#5.说出查询语句中涉及到的所有关键字和执行的先后顺序
/*    select 查询列表                              执行第六步
 *    from 表                                      执行第一步
 *    【join type join 表2  on 连接条件】          执行第二步
 *    where 筛选条件                               执行第三步
 *    group by 分组字段                            执行第四步
 *    havig 分组后的筛选                           执行第五步
 *    order by 排序字段                            执行第七步
 *    limit [offset，] size                        执行第八步
 */
```

<br/>

#### 子查询经典案例

```mysql
#1.查询工资最低的员工信息：last_name,salary
mysql> select last_name,salary 
from employees 
where salary=(select min(salary) from employees);

#2.查询平均工资最低的部门信息
#先查到每个部门的最低工资，找出最低平均工资的部门
mysql> select department_id,avg(salary) from employees group by department_id order by avg(salary) limit 1;
#再根据这个部门的id查部门表
mysql> select * from departments 
where department_id=
(select department_id from employees group by department_id order by avg(salary) limit 1);

#3.查询平均工资最低的部门信息和该部门的平均工资
#先查询部门的平均工资最低的部门号和工资
mysql> select department_id,avg(salary) as avg_salary 
from employees 
group by department_id 
order by avg_salary limit 1;
#再把上一步的内容当作表去连接部门表
mysql> select d.*,avg_dep.avg_salary 
from departments as d
inner join 
(select department_id,avg(salary) as avg_salary from employees group by department_id order by avg_salary limit 1) as avg_dep 
on d.department_id=avg_dep.department_id;

#4.查询平均工资最高的job信息
#先根据job_id进行分组，得到平均工资最高的job_id，使用这个分组表去连接jobs表
mysql> select job_id,max(salary) as max_salary 
from employees 
group by job_id 
order by max_salary desc limit 1;

mysql> select * from jobs 
inner join 
(select job_id,avg(salary) as avg_salary from employees group by job_id order by avg_salary desc limit 1) as avg_dep 
on avg_dep.job_id=jobs.job_id;

#5.查询平均工资高于工资平均工资的部门
mysql> select department_id,avg(salary) 
from employees 
group by department_id 
having avg(salary)>(select avg(salary) from employees);

#6.查询出公司中所有manager的详细信息,这里manager_id有个null，
mysql> select * from employees 
where employee_id =any(select distinct manager_id from employees);

#7.各部门中最高工资最低的那个部门，最低工资多少？
#首先查找到最高工资中最低的那个部门编号
select department_id -- ,max(salary) 
from employees 
group by department_id
order by max(salary) asc limit 1;

select department_id,min(salary) 
from employees 
where department_id=
(select department_id from employees  group by department_id order by max(salary) asc limit 1) 
group by department_id;

#8.查询平均工资最高的部门的manager的详细信息:last_name,departmemt_id,email,salary
#首先找到平均工资最高的部门id
select department_id -- ,max(salary) 
from employees 
group by department_id
order by avg(salary) desc limit 1
#再使用这个department_id去找manager_id
select manager_id from departments where department_id=
(
select department_id -- ,max(salary) 
from employees 
group by department_id
order by max(salary) asc limit 1
);
#最后查manager的详细信息
select last_name,department_id,email,salary from employees  where employee_id=
(
select manager_id from departments where department_id=
(
select department_id -- ,max(salary) 
from employees 
group by department_id
order by avg(salary) desc limit 1
)
);

```

作业(先创建如下数据库)

```mysql
create database student;
use student;

CREATE TABLE student(
    studentno VARCHAR(10) NOT NULL PRIMARY KEY,
    studentname VARCHAR(20) NOT NULL,
    loginpwd VARCHAR(8) NOT NULL,
    sex CHAR(1) ,
    majorid INT NOT NULL REFERENCES grade(majorid),
    phone VARCHAR(11),
    email VARCHAR(20) ,
    borndate DATETIME
);
 
CREATE TABLE major(
    majorid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    majorname VARCHAR(20) NOT  NULL
 
);
CREATE TABLE result(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    studentno VARCHAR(10) NOT NULL REFERENCES student(studentno),
    score DOUBLE
);
 
 
INSERT INTO major VALUES(NULL,'javaee');
INSERT INTO major VALUES(NULL,'html5');
INSERT INTO major VALUES(NULL,'android');
 
 
INSERT INTO student VALUES('S001','张三封','8888','男',1,'13288886666','zhangsanfeng@126.com','1966-9-1');
INSERT INTO student VALUES('S002','殷天正','8888','男',1,'13888881234','yintianzheng@qq.com','1976-9-2');
INSERT INTO student VALUES('S003','周伯通','8888','男',2,'13288886666','zhoubotong@126.com','1986-9-3');
INSERT INTO student VALUES('S004','张翠山','8888','男',1,'13288886666',NULL,'1995-9-4');
INSERT INTO student VALUES('S005','小小张','8888','女',3,'13288885678','xiaozhang@126.com','1990-9-5');
 
INSERT INTO student VALUES('S006','张无忌','8888','男',2,'13288886666','zhangwuji@126.com','1998-8-9');
INSERT INTO student VALUES('S007','赵敏','0000','女',1,'13288880987','zhaomin@126.com','1998-6-9');
INSERT INTO student VALUES('S008','周芷若','6666','女',1,'13288883456','zhouzhiruo@126.com','1996-7-9');
INSERT INTO student VALUES('S009','殷素素','8888','女',1,'13288886666','yinsusu@163.com','1986-1-9');
INSERT INTO student VALUES('S010','宋远桥','6666','男',3,'1328888890','songyuanqiao@qq.com','1996-2-9');
 
 
INSERT INTO student VALUES('S011','杨不悔','6666','女',2,'13288882345',NULL,'1995-9-9');
INSERT INTO student VALUES('S012','杨逍','9999','男',1,'13288885432',NULL,'1976-9-9');
INSERT INTO student VALUES('S013','纪晓芙','9999','女',3,'13288888765',NULL,'1976-9-9');
INSERT INTO student VALUES('S014','谢逊','9999','男',1,'13288882211',NULL,'1946-9-9');
INSERT INTO student VALUES('S015','宋青书','9999','男',3,'13288889900',NULL,'1976-6-8');
 
 
 
INSERT INTO result VALUES(NULL,'s001',100);
INSERT INTO result VALUES(NULL,'s002',90);
INSERT INTO result VALUES(NULL,'s003',80);
 
INSERT INTO result VALUES(NULL,'s004',70);
INSERT INTO result VALUES(NULL,'s005',60);
INSERT INTO result VALUES(NULL,'s006',50);
INSERT INTO result VALUES(NULL,'s006',40);
INSERT INTO result VALUES(NULL,'s005',95);
INSERT INTO result VALUES(NULL,'s006',88);



#1.查询每个专业的学生人数
mysql> select majorid,count(*) from student group by majorid;
#2.查询参加考试的学生中，每个学生的平均分和最高分
mysql> select studentno,avg(score),max(score),count(*) from result group by studentno;
#3.查询姓张的每个学生的最低分大于60分的学号和姓名
#首先查到每个学生的最低分大于60的学号，然后连接student表，找姓张的
select studentno,min(score) from result group by studentno having min(score)>60;
mysql> select s.studentno,s.studentname from student s
    -> inner join (select studentno,min(score) from result group by studentno having min(score)>60) as min_dep on min_dep.studentno=s.studentno
    -> where s.studentname like '张%';
#方法2:
#两个表连接起来再分组筛选
mysql> select s.*,r.* from student as s inner join result as r on r.studentno=s.studentno;
#分组结果
+-----------+-------------+----------+------+---------+-------------+----------------------+---------------------+----+-----------+-------+
| studentno | studentname | loginpwd | sex  | majorid | phone       | email                | borndate            | id | studentno | score |
+-----------+-------------+----------+------+---------+-------------+----------------------+---------------------+----+-----------+-------+
| S001      | 张三封      | 8888     | 男   |       1 | 13288886666 | zhangsanfeng@126.com | 1966-09-01 00:00:00 |  1 | s001      |   100 |
| S002      | 殷天正      | 8888     | 男   |       1 | 13888881234 | yintianzheng@qq.com  | 1976-09-02 00:00:00 |  2 | s002      |    90 |
| S003      | 周伯通      | 8888     | 男   |       2 | 13288886666 | zhoubotong@126.com   | 1986-09-03 00:00:00 |  3 | s003      |    80 |
| S004      | 张翠山      | 8888     | 男   |       1 | 13288886666 | NULL                 | 1995-09-04 00:00:00 |  4 | s004      |    70 |
| S005      | 小小张      | 8888     | 女   |       3 | 13288885678 | xiaozhang@126.com    | 1990-09-05 00:00:00 |  5 | s005      |    60 |
| S006      | 张无忌      | 8888     | 男   |       2 | 13288886666 | zhangwuji@126.com    | 1998-08-09 00:00:00 |  6 | s006      |    50 |
| S006      | 张无忌      | 8888     | 男   |       2 | 13288886666 | zhangwuji@126.com    | 1998-08-09 00:00:00 |  7 | s006      |    40 |
| S005      | 小小张      | 8888     | 女   |       3 | 13288885678 | xiaozhang@126.com    | 1990-09-05 00:00:00 |  8 | s005      |    95 |
| S006      | 张无忌      | 8888     | 男   |       2 | 13288886666 | zhangwuji@126.com    | 1998-08-09 00:00:00 |  9 | s006      |    88 |
+-----------+-------------+----------+------+---------+-------------+----------------------+---------------------+----+-----------+-------+
mysql> select s.studentname,s.studentno 
from student s 
inner join result as r on r.studentno=s.studentno 
where s.studentname like '张%' 
group by s.studentno having min(r.score)>60;

#4.查询生日在‘1988-1-1’后的学生姓名、专业名称
mysql> select s.studentname,m.majorname from student as s
    -> inner join major m on m.majorid=s.majorid
    -> where datediff(borndate,'1988-1-1')>0;
    
#5.查询每个专业男生人数和女生人数分别是多少？
mysql> select majorid,sex,count(*) from student group by majorid ,sex;
+---------+------+----------+
| majorid | sex  | count(*) |
+---------+------+----------+
|       1 | 男   |        5 |
|       2 | 男   |        2 |
|       3 | 女   |        2 |
|       1 | 女   |        3 |
|       3 | 男   |        2 |
|       2 | 女   |        1 |
+---------+------+----------+
#方法2:
mysql> select s.majorid, 
(select count(*) from student where sex='男' and majorid=s.majorid) as 男, 
(select count(*) from student where sex='女' and majorid=s.majorid) as 女 
from student as s group by s.majorid;
+---------+------+------+
| majorid | 男   | 女   |
+---------+------+------+
|       1 |    5 |    3 |
|       2 |    2 |    1 |
|       3 |    2 |    2 |
+---------+------+------+

#6.查询专业和张翠山一样的学生的最低分
#首先查到张翠山的majorid
select majorid from student where studentname='张翠山';
#然后去找一样课的studentno
select studentno from student 
where majorid=(select majorid from student where studentname='张翠山') 
and studentname<>'张翠山';
#最后查最低分
select min(score) from result where studentno in
(
select studentno from student 
where majorid=(select majorid from student where studentname='张翠山') 
and studentname<>'张翠山'
);


#7.查询大于60分的学生的姓名、密码、和专业
mysql> select s.studentname,s.loginpwd,m.majorname 
from student as s 
inner join major as m on m.majorid=s.majorid 
where s.studentno in(select distinct studentno from result where
 score>60);
 
 #8.按照邮箱的位数分组，查询每组学生的个数
 mysql> select length(email),count(*) from student group by length(email) ;
 
 #9.查询学生名，专业名、分数 (注意有的没有分数，要用左连接)
 mysql> select s.studentname,m.majorname,r.score from student s 
 inner join major m on m.majorid=s.majorid 
 left join result r on r.studentno=s.studentno;
 
 #10.查询哪个专业没有学生，分别用左连接和右连接实现
 mysql> select m.*from major m  
 left join student s on m.majorid=s.majorid 
 where s.studentno is null;
 mysql> select m.* from student s 
 right join major m on s.majorid=m.majorid 
 where s.studentno is null;
 
 #11.查询没有成绩的学生人数
 mysql> select count(*) 
 from student s  
 left join result r on r.studentno=s.studentno 
 where r.score is null;

```

### 联合查询

union联合：把多条查询语句的结果合并为一个结果,查出来的结果取并集

注意 union all 不去重

```mysql
#引入案例：查询部门编号大于90或邮箱包含a的员工信息
mysql> select * from employees where department_id>90 or email like '%a%';
#使用联合查询
mysql> select * from employees where department_id>90
    -> union
    -> select * from employees where email like '%a%';
    
/*
 *  语法：
 *    查询语句1
 *    union 【all】
 *    查询语句2
 *    union 【all】
 *    ... 
 *  应用场景：
 *    当要查询的结果来自于多个表，且多个表没有直接的连接关系，但是查询信息一致时，使用联合查询
 *    特点：
 *      1.要求多条查询语句的查询列数一致
 *      2.要求多条查询语句的每一列的类型和顺序最好一致（不一致也不报错，但是没有意义）
 *      3.union关键字默认去重复，使用union all可以包含重复项
 */
 
#举例，需要使用一个test库

```

<br/>

## 六、DML(Data Manage Language)语言

数据操作语言包括：

		数据的插入 insert

		数据的修改 update

		数据的删除 delete

<br/>

### 插入语句

```mysql
/*
 *  方式一：经典插入方式
 *  语法：
 *    insert into 表名(列名。。。) 
 *    values(值1，。。。)
 *
 */
 
#1.插入的值的类型要与列的类型一致或兼容
mysql> insert into beauty(id,name,sex,borndate,phone,photo,boyfriend_id) 
values(13,'唐艺昕','女','1990-4-23',18988888888,null,2);
Query OK, 1 row affected (0.01 sec)

#2.不可以为null的列必须插入值，可以为null的列是如何插入值的？
#方式一：写null
mysql> insert into beauty(id,name,sex,borndate,phone,photo,boyfriend_id) 
values(13,'唐艺昕','女','1990-4-23',18988888888,null,2); -- 写null
#方式二：列名不写，null也不写，相当于忽略这一列
mysql> insert into beauty(id,name,sex,borndate,phone,boyfriend_id) 
values(14,'金星','女','1990-4-23',13988888888,9);
mysql> insert into beauty(id,name,sex,phone) 
values(15,'娜扎','女',13888888888); -- 生日字段没有值会有一个默认值插入


#3.列的顺序是否可以颠倒，可以，只要对应的上
mysql> insert into beauty(name,id,sex,phone) values('蒋欣',16,'女',110);

#4.列数和值的数量必须一一对应
mysql> insert into beauty(name,id,sex,phone，boyfrined_id) values('关晓彤',17,'女',110); -- 报错

#5.可以省略列名，但是默认是所有列，而且列的顺序和表的列顺序是一致的
mysql> insert into beauty 
values(18,'张飞','男',null,119,null,null);


/*
 *  方式二：
 *  语法：
 *    insert into 表名
 *    set 列名=值,列名=值,...;
 */
#案例
mysql>  insert into beauty set id=19,name='刘涛',phone=999;


/*
 *  两种方式pk
 *    1.方式1支持插入多行，方式2不支持
 *    2.方式1支持子查询，方式2不支持
 *
 */
 
#案例：可以一条语句插入多行
mysql> insert into beauty 
values(18,'张飞','男',null,119,null,null),(13,'唐艺昕','女','1990-4-23',18988888888,null,2),(...);
#案例：方式1支持子查询
mysql> insert into beauty(id,name,phone) select 26,'宋茜',1111112;
```

<br/>

### 修改语句

```mysql
/*
 *  1.修改单表的记录
 *    语法：
 *      update 表名
 *      set 列名=值,...
 *      where 筛选条件;
 *
 *
 *  2.修改多表的记录：级联更新
 *    语法(sql92):
 *      update 表1 别名1，表2别名2
 *      set 列=值,...
 *      where 连接条件 and筛选条件;
 *
 *    语法(sql99):
 *      update 表1 别名
 *      【inner｜left｜right】 join 表2 别名 on 连接条件
 *      set 列=值
 *      where 筛选条件;
 *
 */
 
 #修改单表的记录
 #案例1:修改beauty表中姓唐的女生电话为13899999999
 mysql> update beauty set phone=13899999999 where name like '唐%';
 #案例2:修改boys表中id为2的名称为张飞，魅力值为10
 mysql> update boys set boyName='张飞', userCP=10 where id=2; -- 注意set中间不能用and
 
 
 #修改多表的记录
 #案例1:修改张无忌女朋友的手机号为114
 #先找到张无忌的女朋友们
 mysql> select be.* from beauty be left join boys bo on be.boyfriend_id=bo.id where bo.boyName='张无忌';
 #再在select语句的基础上改
 mysql> update beauty be left join boys bo on be.boyfriend_id=bo.id set phone=114  where bo.boyName='张无忌';
 #案例2:修改没有男朋友的女神的男朋友都为2号
 #首先查出来没有男朋友的女神
 mysql> select be.* from beauty be left join boys bo on be.boyfriend_id=bo.id where boyfriend_id is null;
 #然后再修改
 mysql> update beauty be left join boys bo on be.boyfriend_id=bo.id 
 set boyfriend_id =2 where boyfriend_id is null;
```

<br/>

### 删除语句

```mysql
/*
 *  方式1:
 *    1.单表删除：
 *      delete from 表名 where 筛选条件 【limit 条目数】;
 *    2.多表删除：
 *      sql92语法：
 *        delete 别名（要删除表记录的别名，如果多个表都删，都加上） 
 *        from 表1 别名，表2 别名
 *        where 连接条件 and 筛选条件;
 *
 *      sql99语法：
 *        delete 别名（要删除表记录的别名，如果多个表都删，都加上） 
 *        from 表1 别名
 *        inner/left/right join 表2 别名 on 连接条件
 *        where 筛选条件;
 *
 *  方式2: 删除整个表的数据
 *    语法：truncate table 表名;
 *
 *  两种方式的区别（重点面试题）：
 *    1.delete可以加where条件，truncate不可以
 *    2.truncate效率高于delete
 *    3.加入要删除的表中有一列自增长列
 *      如果使用delete删除，再插入数据，自增长列的数值从断点开始
 *      如果使用truncate删除，再插入数据，自增长列的数值从1开始
 *    4.truncate删除没有返回值（不返回删了几行），但是delete删除有返回值（返回删了几行）
 *    5.truncate删除不能回滚，delete删除可以回滚
 */
 
#方式1
#单表删除
#案例：删除手机号以9结尾的女神信息
delete from beauty where phone like '%9';
#多表删除
#案例：删除张无忌女朋友信息
#先找到张无忌的女朋友们
mysql> select be.* from beauty be left join boys bo on be.boyfriend_id=bo.id where bo.boyName='张无忌';
#再删除
delete be from beauty be left join boys bo on be.boyfriend_id=bo.id where bo.boyName='张无忌';
#案例：删除黄晓明信息和他女朋友信息
delete bo,be from boys bo 
inner join beauty be on be.boyfriend_id=bo.id
where bo.boyName='黄晓明';

#方式2
truncate table boys; -- 不能加筛选条件，效率高于delete
```

<br/>

作业

```mysql
#1.运行以下脚本创建表my_employees
use myemployees;

create table my_employees(
Id int(10),
First_name varchar(10),
Last_name varchar(10),
User_id varchar(10),
Salary double(10,2)
);

create table users(
id int,
userid varchar(10),
department_id int
);

#2.查看表结构
desc my_employees;
desc users;

#3.插入数据
#方式1:
insert into my_employees(Id,First_name,Last_name,User_id,Salary)
values(1,'patel','Ralph','Rpatel',895),
(2,'Dancs','Betty','Bdancs',860),
(3,'Biri','Ben','Bbiri',1100),
(4,'Newman','Chad','Cnewman',750),
(5,'Ropeburn','Audrey','Aropebur',1550);
#方式2
insert into my_employees(Id,First_name,Last_name,User_id,Salary)
select 1,'patel','Ralph','Rpatel',895 union
select 2,'Dancs','Betty','Bdancs',860 union
select 3,'Biri','Ben','Bbiri',1100 union
select 4,'Newman','Chad','Cnewman',750 union
select 5,'Ropeburn','Audrey','Aropebur',1550;

#4.插入数据
insert into users(id,userid,department_id)
values(1,'Rpatel',10),
(2,'Bdancs',10),
(3,'Bbiri',20),
(4,'Cnewman',30),
(5,'Aropebur',40);

#5.修改3号员工的last_name为'derelexer'
update my_employees set Last_name ='derelexer' where Id=3;

#6.把所有工资小于900的员工的工资都改为1000
update my_employees set Salary=1000 where Salary<900;

#7.将userid为Bbiri的users表和my_employees 表中的记录都删除
delete u,m
from users u
inner join my_employees m on m.User_id=u.userid
where u.userid='Bbiri';

#8.删除所有的数据
delete from my_employees;
delete from users;

#9.清空表my_employees 
truncate table my_employees;
```

<br/>

## 七、DDL(Data Define Language)语言

数据定义语言，主要涉及库和表的操作。

库的管理：创建create、修改alter、删除drop

表的管理：创建create、修改alter、删除drop，复制

**注意：if not exists 和if exists 只针对库和表的创建和删除，列不行。**

### 库的管理

```mysql
/*
 *  1.库的创建
 *    语法：
 *    create database [if not exists ]库名 【character set 字符集名】;
 *
 *
 */
 
#案例
create database books; -- 执行第二遍会报错
#改进版本，不报错且只有不存在的时候才创建
create database if not exists books;

/*
 *  2.库的修改
 *  
 *    一般不修改库，很容易影响存量数据
 *    5版本之前的MySQL支持库的重命名
 *    rename database 老名字 to 新名字
 *    现在不行了，如果要改，直接去找库的文件夹，停了服务再改。
 *
 *    更改库的字符集
 *    alter database 库名 character set gbk|utf8;
 *
 */
#案例
alter database books character set gbk;
#检查一下
use books;
show variables like '%character%'; -- character_set_database

/*
 *  3.库的删除
 *  
 *  语法：
 *    drop database [if exists] 库名;
 *
 *
 */
#案例
drop  database if exists books;
#检查一下
show databases;
```

<br/>

### 表的管理

```mysql
/*
 *  1.表的创建（重点）
 *    语法：
 *      create table 【if not exists】表名
 *      (
 *        列名 列的类型【(长度) 列的约束】,
 *        列名 列的类型【(长度) 列的约束】,  
 *        列名 列的类型【(长度) 列的约束】,
 *        ...
 *        列名 列的类型【(长度) 列的约束】
 *      );
 */
#案例：创建book表
mysql> create table if not exists book(
       id int,-- 图书编号
       bName varchar(20),-- 图书名
       price double, -- 图书价格
       authorId int, -- 作者表
       publishDate datetime -- 出版日期
       );
desc book;
#案例，创建author表
mysql> create table if not exists author(
       id int,
       au_name varchar(20),
       nation varchar(10)
       );




/*
 *  2.表的修改
 *    修改列名
 *      语法：alter table 表名 change 【column】旧列名 新列名 新列类型;
 *
 *    修改列的类型或约束条件
 *      语法：alter table 表名 modify column 列名 新类型 【新约束】;
 *
 *    添加列
 *        语法：alter table 表名 add column 列名 列类型 【first|after 字段名】; -- 添加到哪个位置
 *
 *    删除列
 *        语法：alter table 表名 drop column 列名;
 *
 *    修改表名
 *        语法：alter table 旧表名 rename to 新表名
 *
 *    总结：
 *      alter table 表名 add|drop|modify|change|(rename to) column 列名 【列类型 约束条件】
 *
 */
#修改列名publishDate为pubDate,注意这里要重置类型
alter table book change column publishDate pubDate datetime;
desc book;

#修改列pubDate的类型为timestamp
alter table book modify column pubDate timestamp;

#author表新增一列年薪annual
alter table author add column annual double;


##author表删除年薪annual列
alter table author drop column annual; -- 这里不能使用if exists 仅仅在库和表的创建删除的时候使用，列不行

#修改表名
alter table author rename to book_author;




/*
 *  3.表的删除
 *  
 *  语法：drop table 【if exists 】表名;
 * 
 *
 */
#案例：删除表book_author
drop table if exists book_author;
show tables;

/*
 *  4.表的复制
 *  
 *  只复制表的结构
 *    语法：create table 新表名 like 要复制的表;
 *
 *  复制表的结构和数据，可以只复制部分数据
 *  create table 新表名
 *  select * from 要复制的表名
 *
 */
#案例：复制表book_author
#先插入点数据看效果
mysql> insert into book_author 
values(1,'村上春树','日本'),
(2,'莫言','中国'),
(3,'冯唐','中国'),
(4,'金庸','中国');

#只复制表的结构
create table copy like book_author;
#复制表的结构和数据
create table copy2 select * from book_author;
#只复制部分数据
create table copy3 select id,au_name from book_author where nation ='中国';

#只复制表的结构中某些字段，没有数据
create table copy4 select id,au_name from book_author where 1=2; -- 设置一个恒不成立的条件 或者where 0
create table copy4 select id,au_name from book_author where 0;
```

通用的写法

```mysql
drop database if exists 旧库名;
create database 新库名;
drop table if exists 旧表名;
create table 新表名
```

作业

```mysql
use test;
#1.创建dept1表
create table dept1(id int(7),name varchar(25));

#2.将myemployees库中的departments表中的数据插入dept2表中
create table dept2 
select department_id,department_name from myemployees.departments;

#3.创建表emp5
create table emp5
(
id int(7),
First_name varchar(25),
Last_name varchar(25),
Dept_id int(7)
);

#4.要求将emp5表的Last_name字段的长度增加到50
alter table emp5 modify column Last_name varchar(50);

#5.根据表employees表创建employees2表
create table employees2 select * from myemployees.employees;
create table employees2 like myemployees.employees;

#6.删除表emp5
drop table if exists emp5;

#7.重命名employees2表为emp5
alter table employees2 rename to emp5;

#8.在dept和emp5中添加列test_column
alter table dept1 add column test_column int;
alter table emp5 add column test_column int;

#9.删除emp5表中的department_id字段
alter table emp5 drop column department_id;
```

<br/>

#### 常见的数据类型

选择数据类型的原则：**所选类型越简单越好，能保存数值的类型越小越好。**

<br/>

```mysql
/*
 *  分类：
 *    数值型：
 *      整型
 *      小数：
 *        定点数 float(M,D) double (M,D)
 *        浮点数 dec(M,D)或者decimal(M,D)
 *
 *    字符型
 *      较短的文本：char,varchar
 *      较长的文本：text，blob（二进制数据）
 *
 *    日期型
 */
```

##### 整型

|整数类型|字节|范围|
|--|--|--|
|tinyint|1|有符号：-128～127<br/>无符号：0～255|
|smallint|2|有符号：-32768～32767 <br/>无符号：0～65535|
|mediumint|3|有符号：-8388608～ 8388607<br/>无符号：0～1677215|
|int,integer|4|有符号：-2147483648～ 2147483647 <br/>无符号：0～4294967295|
|bigint|8|有符号：-9223372036854775808～ 9223372036854775807 <br/>无符号：0～9223372036854775807*2+1|

<br/>

```mysql
/*
 *  特点：
 *    1.如果不设置，默认是有符号；如果想设置无符号，那就加unsigned关键字
 *    2.如果超出了整型范围，会报out of range异常，并插入临界值
 *    3.如果不设置长度，会有默认长度。长度代表显示结果的一个位数宽度，如果不够这个位数宽度，会用0来填充
 *      但必须搭配zerofill
 *
 */

#案例：如何设置无符号和有符号
create table tab_int (t1 int); -- 这样其实是设置有符号
insert into tab_int value(-123456); -- 结果是-123456

create table tab_int (t1 int,t2 int unsigned); -- t2是无符号
insert into tab_int value(-123456,-123456); -- 会有警告,会把负数转化为0
mysql> select * from tab_int;
+---------+------+
| t1      | t2   |
+---------+------+
| -123456 |    0 |
+---------+------+


#案例：超出整型范围
insert into tab_int value(2147483648,4294967296); -- 超出上界就记录下来上界
mysql> select * from tab_int;
+------------+------------+
| t1         | t2         |
+------------+------------+
|    -123456 |          0 |
| 2147483647 | 4294967295 |
+------------+------------+


#案例：
insert into tab_int value(123,123); -- 并没有用0填充，因为没有用关键字zerofill
#zerofill关键字默认搭配的是无符号数
create table tab_int 
(
t1 int(7) zerofill,
t2 int(7) zerofill
);
insert into tab_int value(123,123);
mysql> select * from tab_int;
+---------+---------+
| t1      | t2      |
+---------+---------+
| 0000123 | 0000123 |
+---------+---------+
```

##### 小数

|浮点数类型|字节|范围|
|--|--|--|
|float|4||
|double|8||

|定点数类型|字节|类型|
|--|--|--|
|DEC(M,D) --简写<br/>DECIMAL(M,D)|M+2|最大取值范围和double相同，给定decimal的取值范围由M和D来决定|

<br/>

```mysql
/*
 *  特点：
 *    1.M代表是整数位+小数位数，D代表小数位。如果超出临界值，插入临界值
 *    2.M和D都可以省略，但是decimal类型，默认M是10，D是0，如果超过了会插入临界值
 *      如果是float和double，会根据插入数字的精度来决定精度
 *    3.定点型的精度较高，如果插入数值精度较高比如货币运算等考虑使用
 */
 
#1.M和D啥意思
create table tab_float 
(
f1 float(5,2),
f2 double(5,2),
f3 decimal(5,2)
);
insert into tab_float values(123.45,123.45,123.45);
insert into tab_float values(123.456,123.456,123.456);  -- 发现保留两位小数，四舍五入了
insert into tab_float values(123.4,123.4,123.4); -- 填充0
mysql> select * from tab_float;
+--------+--------+--------+
| f1     | f2     | f3     |
+--------+--------+--------+
| 123.45 | 123.45 | 123.45 |
| 123.46 | 123.46 | 123.46 |
| 123.40 | 123.40 | 123.40 |
+--------+--------+--------+
insert into tab_float values(1523.4,1523.4,1523.4); -- 三个警告
mysql> select * from tab_float;
+--------+--------+--------+
| f1     | f2     | f3     |
+--------+--------+--------+
| 123.45 | 123.45 | 123.45 |
| 123.46 | 123.46 | 123.46 |
| 123.40 | 123.40 | 123.40 |
| 999.99 | 999.99 | 999.99 |
+--------+--------+--------+
```

<br/>

##### 字符型

|字符串类型|最多字符数<br/>英文和汉字都是字符|描述及存储需求|
|--|--|--|
|char(M)|M|M 为0～255的整数|
|varchar(M)|M|M位0～65535的整数|
|binary||包含较短二进制|
|varbinary||包含较短二进制|
|enum||枚举类型，要求插入的值必须是列表中的值<br/>列表成员1-255 使用1B<br/>列表成员255-65535 使用2B<br/>最多65535|
|set||和enum类似，但是可以同时保存0～64个成员<br/>成员数1-8占用1B<br/>成员数9-16占用2B<br/>成员数17-24占用3B<br/>成员数25-32占用4B<br/>成员数33-64占用8B|
|text||较长文本|
|blob||二进制图片|

特点：

	1.M代表最大的字符数

	2.char代表固定长度的字符（开辟固定M个字符的空间），varchar代表可变长度的字符

	3.char比varchar消耗空间多

	4.char比varchar效率高

	5.char(M)的M可以省略，默认为1；varchar(M)不可以省略

```mysql
#测试枚举
create table tab_char
(
  c1 enum('a','b','c')
);
insert into tab_char values('a');
insert into tab_char values('b');
insert into tab_char values('c');
insert into tab_char values('m'); -- 插入了一个空
insert into tab_char values('A'); -- 插入了一个小a. 枚举不区分大小写
mysql> select * from tab_char;
+------+
| c1   |
+------+
| a    |
| b    |
| c    |
|      |
| a    |
+------+

#测试set，和枚举一样不区分大小写
create table tab_set
(
  s1 set('a','b','c','d')
);
insert into tab_set values('a');
insert into tab_set values('a,b');
insert into tab_set values('a,c,d');
mysql> select * from tab_set;
+-------+
| s1    |
+-------+
| a     |
| a,b   |
| a,c,d |
+-------+
```

<br/>

##### 日期型

|日期和时间类型|字节|最小值|最大值|
|--|--|--|--|
|date|4|1000-01-01|9999-12-31|
|**datetime**|8|1000-01-01 00:00:00|9999-12-31 23:59:59|
|**timestamp**|4|19700101080001|2038年的某个时刻|
|time|3|-838:59:59|838:59:59|
|year|1|1901|2155|

**datetime和timestamp的区别**

	1.timestamp支持的时间范围较小，datetime支持的时间范围较大

	2.timestamp和实际的时区有关，更能反应实际的日期；datetime则只能反应出插入时的当地时区

	3.timestamp的属性受MySQL和SQLMode的影响比较大

```mysql
#
create table tab_date
(
t1 datetime,
t2 timestamp
);
insert into tab_date values(now(),now());
mysql> select * from tab_date;
+---------------------+---------------------+
| t1                  | t2                  |
+---------------------+---------------------+
| 2022-02-09 20:42:24 | 2022-02-09 20:42:24 |
+---------------------+---------------------+

#看一下当前的时区
mysql> show variables like 'time_zone';
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| time_zone     | SYSTEM |
+---------------+--------+
#设置时区为东九区
mysql> set time_zone ='+9:00';
#此时在看表内的数据，timestamp跟着时区变化了，datatime不变化
mysql> select * from tab_date;
+---------------------+---------------------+
| t1                  | t2                  |
+---------------------+---------------------+
| 2022-02-09 20:42:24 | 2022-02-09 21:42:24 |
+---------------------+---------------------+
```

<br/>

#### 常见约束

含义：一种限制，用于限制表中的数据的，为了最终保证数据的准确和可靠性、一致性。

##### 六大约束

	1.not null 非空约束，用于保证该字段 的值不能为空

	2.default 默认约束，用于保证该字段有默认值

	3.primerary key 主键约束，用于保证该字段的值的唯一性且非空

	4.unique 唯一约束，用于保证该字段的值具有唯一性，但是可以为空 eg座位号

	5.check 检查约束（MySQL不支持但不报错），年龄、性别都可以用

	6.foreign key 外健约束，用于限制两个表的关系，用于保障该字段的值必须来自于主表关联列的值。

		在从表中添加外键约束，用于引用主表某一列的值

添加约束的时机：

	1.创建表的时候

	2.修改表的时候（添加数据之前）

<br/>

约束的添加分类

	列级约束

		六大约束都支持，但是外键约束写成列级约束没有效果

	表级约束（字段约束都写完了，最后写一个）

		除了非空约束、默认约束，其他的都支持

**注意：可以添加多个列级约束，使用空格隔开，不用逗号，没有顺序限制**

<br/>

##### 创建表的时候添加约束

```mysql
#一、创建表的时候添加约束
#1.添加列级约束
/*
 *  语法：直接在字段类型后面添加约束条件即可
 *        只支持主键、非空、默认、唯一
 *
 *
 */
create database students;
use students;

create table major
(
id int primary key,
majorName varchar(20)
);
create table stuinfo
(
id int primary key, #主键
stuName varchar(20) not null,#非空
gender char(10) check(gender in ('男','女')), -- 或者check(gender='男'or gender ='女')
seat int unique, #唯一约束
age int default 18， #默认18岁
majorId int references major(id) #外健，不过写成列级约束没有效果 这条会报错，删掉
);
mysql> desc stuinfo;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| id      | int         | NO   | PRI | NULL    |       |
| stuName | varchar(20) | NO   |     | NULL    |       |
| gender  | char(10)    | YES  |     | NULL    |       |
| seat    | int         | YES  | UNI | NULL    |       |
| age     | int         | YES  |     | 18      |       |
| majorId | int         | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+

#查看stuinfo表中所有的索引
mysql> show index from stuinfo;
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table   | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| stuinfo |          0 | PRIMARY  |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| stuinfo |          0 | seat     |            1 | seat        | A         |           0 |     NULL |   NULL | YES  | BTREE      |         |               | YES     | NULL       |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
#Non_unique不是唯一，0代表不是非唯一，也就是唯一
#注意：主键、外键、唯一键都是自动添加了索引



#二、添加表级约束
/*
 *  语法：在各个字段的最下面，名字可以不起
 *        【constraint 约束名字】 约束类型(表字段名字) 【references  外键涉及的主表(字段)】
 *
 *
 */
drop table if exists stuinfo; -- 先删了表重新建
create table stuinfo
(
id int , 
stuName varchar(20) ,
gender char(10) , 
seat int, 
age int ,
majorId int,
#添加表级约束
constraint pk primary key(id),
constraint uq unique(seat),
constraint ck check(gender='男'or gender ='女'),
constraint fk_stuinfo_major foreign key(majorId) references major(id) #外键
);

mysql> desc stuinfo;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| id      | int         | NO   | PRI | NULL    |       |
| stuName | varchar(20) | YES  |     | NULL    |       |
| gender  | char(10)    | YES  |     | NULL    |       |
| seat    | int         | YES  | UNI | NULL    |       |
| age     | int         | YES  |     | NULL    |       |
| majorId | int         | YES  | MUL | NULL    |       |
+---------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

mysql> show index from stuinfo; -- 主键名字不能改
+---------+------------+------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| Table   | Non_unique | Key_name         | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment | Visible | Expression |
+---------+------------+------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+
| stuinfo |          0 | PRIMARY          |            1 | id          | A         |           0 |     NULL |   NULL |      | BTREE      |         |               | YES     | NULL       |
| stuinfo |          0 | uq               |            1 | seat        | A         |           0 |     NULL |   NULL | YES  | BTREE      |         |               | YES     | NULL       |
| stuinfo |          1 | fk_stuinfo_major |            1 | majorId     | A         |           0 |     NULL |   NULL | YES  | BTREE      |         |               | YES     | NULL       |
+---------+------------+------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+---------+------------+




#通用写法
create table if not exists stuinfo
(
id int primary key,
stuName varchar(20) not null,
gender char(1),
age int default 18,
seat int unique,
majorId int,
constraint fk_stuinfo_major foreign key(majorId) references major(id)
);

#主键和唯一的大对比
insert into major values(1,'java'),(2,'h5');
insert into stuinfo value(1,'john','男',null,19,1);
insert into stuinfo value(2,'lily','男',null,19,2);
```

主键和唯一的大对比

||保证唯一性|是否允许为空|一个表中可以有多少个|是否允许组合|
|--|--|--|--|--|
|主键|可以|不可以|只能有一个|允许组合，但是不推荐|
|唯一|可以|可以|可以有多个|允许组合，但是不推荐|

```mysql
#主键和唯一的大对比

drop table if exists stuinfo; -- 先删了表重新建
create table stuinfo
(
id int , 
stuName varchar(20) ,
gender char(10) , 
seat int, 
age int ,
majorId int,
#添加表级约束
constraint pk primary key(id),
constraint uq unique(seat),
constraint ck check(gender='男'or gender ='女'),
constraint fk_stuinfo_major foreign key(majorId) references major(id) #外键
);

insert into major values(1,'java'),(2,'h5');

#可以unique列可以有多个null
insert into stuinfo value(1,'john','男',null,19,1);
insert into stuinfo value(2,'lily','男',null,19,2);

#主键可以组合，联合主键，还是一个主键
create table stuinfo
(
id int , 
stuName varchar(20) ,
gender char(10) , 
seat int, 
age int ,
majorId int,
#添加表级约束
drop table if exists stuinfo;
create table stuinfo
(
id int , 
stuName varchar(20) ,
gender char(10) , 
seat int, 
age int ,
majorId int,
#添加表级约束
constraint pk primary key(id,stuName),
constraint uq unique(seat),
constraint ck check(gender='男'or gender ='女'),
constraint fk_stuinfo_major foreign key(majorId) references major(id) #外键
);

show index from stuinfo;
```

外键：

	1.要求在从表中设置外键关系

	2.从表的外键列的类型要求和主表的关联列的类型要求一致或兼容，但是名称没有要求

	3.**主表中的关联列必须是一个key，一般是主键或者唯一键**

	4.插入数据时，先插入主表再插入从表；删除的时候，先删除从表，再删除主表

<br/>

**外键的级联删除和级联置空**

```mysql
#使用数据
use student;
#设置外键
mysql> alter table student add constraint fk_stu_major foreign key(majorid) references major(majorid);
#student表在创建的时候设置了外键majorid，那么major表删除数据就会受阻
delete from major where majorid=3; -- 会被外键阻止


#1.设置级联删除
#先删除之前的外键
alter table student drop foreign key  fk_stu_major;
mysql> alter table student 
add constraint fk_stu_major foreign key(majorid) references major(majorid) on delete cascade;
#再次删除就可以了
delete from major where majorid=3; -- 注意，student表中引用3号的也被删了

#2.设置级联置空
#先删除之前的外键
alter table student drop foreign key  fk_stu_major;
mysql> alter table student modify column majorid int ; -- 先设置student表中的majorid可以为空
alter table student modify column major id int;
mysql> alter table student 
add constraint fk_stu_major1 foreign key(majorid) references major(majorid) on delete set null;
#删除
mysql> delete from major where majorid=2;
#检查student表
mysql> select * from student; -- 结果里面有null值
+-----------+-------------+----------+------+---------+-------------+----------------------+---------------------+
| studentno | studentname | loginpwd | sex  | majorid | phone       | email                | borndate            |
+-----------+-------------+----------+------+---------+-------------+----------------------+---------------------+
| S001      | 张三封      | 8888     | 男   |       1 | 13288886666 | zhangsanfeng@126.com | 1966-09-01 00:00:00 |
| S002      | 殷天正      | 8888     | 男   |       1 | 13888881234 | yintianzheng@qq.com  | 1976-09-02 00:00:00 |
| S003      | 周伯通      | 8888     | 男   |    NULL | 13288886666 | zhoubotong@126.com   | 1986-09-03 00:00:00 |
| S004      | 张翠山      | 8888     | 男   |       1 | 13288886666 | NULL                 | 1995-09-04 00:00:00 |
| S006      | 张无忌      | 8888     | 男   |    NULL | 13288886666 | zhangwuji@126.com    | 1998-08-09 00:00:00 |
| S007      | 赵敏        | 0000     | 女   |       1 | 13288880987 | zhaomin@126.com      | 1998-06-09 00:00:00 |
| S008      | 周芷若      | 6666     | 女   |       1 | 13288883456 | zhouzhiruo@126.com   | 1996-07-09 00:00:00 |
| S009      | 殷素素      | 8888     | 女   |       1 | 13288886666 | yinsusu@163.com      | 1986-01-09 00:00:00 |
| S011      | 杨不悔      | 6666     | 女   |    NULL | 13288882345 | NULL                 | 1995-09-09 00:00:00 |
| S012      | 杨逍        | 9999     | 男   |       1 | 13288885432 | NULL                 | 1976-09-09 00:00:00 |
| S014      | 谢逊        | 9999     | 男   |       1 | 13288882211 | NULL                 | 1946-09-09 00:00:00 |
+-----------+-------------+----------+------+---------+-------------+----------------------+---------------------+
#恢复
insert into major values(2,'h5');
update student set majorid=2 where majorid is null;
```

<br/>

<br/>

```mysql
#主表中的关联列必须是一个key
drop tavle if exits stuinfo;
drop table if exists major; 
create table major
(
id int ,-- 没有主键约束
majorName varchar(20)
);
create table stuinfo
(
id int , 
stuName varchar(20) ,
gender char(10) , 
seat int, 
age int ,
majorId int,
#添加表级约束
constraint pk primary key(id,stuName),
constraint uq unique(seat),
constraint ck check(gender='男'or gender ='女'),
constraint fk_stuinfo_major foreign key(majorId) references major(id) #外键
); -- 此时会报错

#试试唯一键
create table major
(
id int unique,-- 没有主键约束
majorName varchar(20)
);
create table stuinfo
(
id int , 
stuName varchar(20) ,
gender char(10) , 
seat int, 
age int ,
majorId int,
#添加表级约束
constraint pk primary key(id,stuName),
constraint uq unique(seat),
constraint ck check(gender='男'or gender ='女'),
constraint fk_stuinfo_major foreign key(majorId) references major(id) #外键
); -- 此时可以
```

<br/>

##### 修改表时添加约束

```mysql
/*
 *  1.添加列级约束
 *    alter table 表名 modify column 字段名 字段类型 新约束
 *  2.添加表级约束
 *    alter table 表名 add 【constraint 约束名】 约束类型(字段名) 【references 表名(字段)】
 *
 *
 */


drop table if exists stuinfo;
create table if not exists stuinfo
(
id int ,
stuName varchar(20) ,
gender char(1),
age int ,
seat int ,
majorId int
);

#1.添加非空约束
alter table stuinfo modify column stuName varchar(20) not null; -- 想删的话，字段、类型后面加上 null 或者不写

#2.添加默认约束
alter table stuinfo modify column age int default 18;

#3.添加主键
alter table stuinfo modify column id int primary key;
#这种是表级约束的写法
alter table stuinfo add primary key(id); -- 这样写也可以

#4.添加唯一键
alter table stuinfo modify column seat int unique;
alter table stuinfo add unique(seat);

#5.添加外键
alter table stuinfo add foreign key (majorId) references major(id);
alter table stuinfo add constraint fk_stuinfo_major foreign key(majorId) references major(id);
```

<br/>

##### 修改表时删除约束

```mysql
#1.删除非空约束
alter table stuinfo modify column stuName varchar(20) null; -- null不写也可以

#2.#删除默认约束
alter table stuinfo modify column age int;

#3.删除主键
#列级约束删除
alter table stuinfo modify column id int;
#表级约束删除
alter table stuinfo drop primary key;-- 不用写字段，因为一个表只有一个主键

#4.删除唯一键
alter table stuinfo modify column seat int;
#这里要先查一下唯一键什么名字
show index from stuinfo;
alter table stuinfo drop index seat;

#5.删除外键约束
alter table stuinfo drop foreign key fk_stuinfo_major;
```

<br/>

列级约束和表级约束

||位置|支持的约束类型|是否可以起名字|
|--|--|--|--|
|列级约束|列的后面|语法都支持，检查和外键没效果|不可以|
|表级约束|所有列的下面|默认和非空、检查不支持|可以，但是主键没效果|

<br/>

<br/>

#### 标识列

又称为自增长列，可以不用手动的插入值，系统可以提供默认的序列值

特点:

	1.标识列不一定必须和主键搭配，但必须和一个key搭配（主键、唯一、外键）

	2.一个表中最多只能有一个自增长列

	3.标识列只能是数值类型，浮点型也可以

	4.标识列可以通过set auto_increment_increment=3；设置步长，可以通过手动插入值设置起始值

<br/>

##### 创建表的时候添加标识列

```mysql
#一、创建表时，设置标识列,在约束后面加
drop table if exists tab_identity;
create table tab_identity
(
id int primary key auto_increment,
name varchar(20)
);
#添加数据
insert into tab_identity values(null,'yyz'); -- id主键写空就行，自动插入系统默认值
insert into tab_identity(name) values('yyz'); -- 这么写也行
mysql> select * from tab_identity;
+----+------+
| id | name |
+----+------+
|  1 | yyz  |
|  2 | yyz  |
|  3 | yyz  |
|  4 | yyz  |
+----+------+


#可以使得默认值不从1开始
mysql> show variables like '%auto_increment%';
#mysql不支持设置起始值offset，只支持设置增长差值（步长）
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 1     |
| auto_increment_offset    | 1     |
+--------------------------+-------+
set auto_increment_increment=3；

truncate table tab_identity;
insert into tab_identity(name) values('yyz'); -- 执行多次
mysql> select * from tab_identity;
+----+------+
| id | name |
+----+------+
|  1 | yyz  |
|  4 | yyz  |
|  7 | yyz  |
| 10 | yyz  |
+----+------+

#就算不能更改起始值，也可以通过先插入一个值，来让数据从这个值开始递增
truncate table tab_identity;
insert into tab_identity(id,name) values(10,'yyz'); 
insert into tab_identity(name) values('yyz'); -- 执行多次
mysql> select * from tab_identity;
+----+------+
| id | name |
+----+------+
| 10 | yyz  |
| 13 | yyz  |
| 16 | yyz  |
| 19 | yyz  |
+----+------+
```

<br/>

##### 修改表的时候添加标识列

```mysql
drop table if exists tab_identity;
create table tab_identity
(
id int ,
name varchar(20)
);
alter table tab_identity modify column id int primary key auto_increment;
mysql> desc tab_identity;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int         | NO   | PRI | NULL    | auto_increment |
| name  | varchar(20) | YES  |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
```

<br/>

##### 修改表的时候删除标识列

注意，主键、外键、唯一键用drop删除

```mysql
alter table tab_identity modify column id int primary key; -- auto_increment去掉
```

<br/>

<br/>

## 八、TCL（transaction control language）语言

### 事务

	指的是一个或一组sql语句组成一个执行单元，这个执行单元要么全部执行，要么全部不执行。

<br/>

#### 存储引擎

	在MySQL中的数据采用不同的技术存储在文件或者内存中

	通过show engines;查看MySQL支持的存储引擎

	在MySQL中用的最多的存储引擎有：innodb，myisam，memory等。其中innodb支持事务，其他两个不支持

<br/>

#### 事务的ACID属性

	Atomicity 原子性

		指的是事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生

	consistency 一致性

		事务必须从数据库的一个一致性状态转移为另外一个一致性状态

	Isolation 隔离性

		一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用数据对并发的其他事务是隔离的，并发执行的各个事务之间不能相互干扰，**得看设置的是什么隔离级别**。

	Durability 持久性

		指的是一个事务一旦被提交了，它对数据库中的数据的改变是永久性的，其他操作及数据库故障不能对其有影响

<br/>

#### 事务的分类

	隐式事务：事务没有明显的开启和结束的标记。比如insert、update、delete语句 

	显示事物：事务必须有明显的开启和结束的标记

		前提：设置自动提交功能禁用，**注意只针对当前的会话有效，不是永久关闭的**。

```mysql
#查看是否隐式提交
mysql> show variables like '%autocommit%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| autocommit    | ON    |
+---------------+-------+
set autocommit =0; -- off也可以

```

<br/>

#### 事务的创建

```mysql
set autocommit =0;
#步骤1:开始事务
start transaction; -- 可选的
#步骤2；编写事务中的sql语句（可以有多条），一般是select insert update delete
#步骤3:结束事务（两种方式）
commit； -- 提交事务
rollback; -- 回滚事务



#案例
use test;
drop table if exists account;
create table account
(
id int primary key auto_increment,
username varchar(20),
balance double
);

insert into account(username,balance) values('张无忌',1000),('赵敏',1000);
mysql> select * from account;
+----+-----------+---------+
| id | username  | balance |
+----+-----------+---------+
|  1 | 张无忌    |    1000 |
|  4 | 赵敏      |    1000 |
+----+-----------+---------+


#开始转账(演示commit)
set autocommit =0;
start transaction;
update account set balance=500 where username='张无忌';
update account set balance=1500 where username='赵敏';
commit;

#演示回滚,没有变化
set autocommit =0;
start transaction;
update account set balance=1000 where username='张无忌';
update account set balance=1000 where username='赵敏';
rollback;
```

<br/>

#### delete和truncate在事务中的区别

```mysql
#delete演示
set autocommit=0;
start transaction;
delete from account;
rollback;
#这样实际上没有删除了数据，所以delete可以回滚

#truncate演示
set autocommit=0;
start transaction;
truncate table account;
rollback;
#数据都删除了，所以truncate不支持回滚
```

#### 事务的隔离级别

对于同时运行的多个事务，当这些事务访问**数据库中相同的数据**，如果没有采取必要的隔离机制，就会引起各种并发问题。

	**脏读**：对于两个事务T1和T2，T1读取了已经被T2更新但是还没有提交的字段，之后如果T2回滚，T1读取的字段无效。

	**不可重复读**：对于两个事务T1和T2，T1读取了一个字段，然后T2更新了该字段，之后T1再次读取同一个字段，值不同了。

	**幻读**：对于两个事务T1和T2，T1从一个表中读取了一个字段，然后T2在该表中插入了一些新的行，之后如果T1再读表，会多出几行数据

<br/>

数据库提供四种事务的隔离级别

|隔离级别|描述|
|--|--|
|read uncommitted<br/>(读未提交数据)|允许事务读取未被提交的变更，脏读，不可重复读，幻读都会出现|
|read committed <br/>(读已提交数据)|只允许事务读取已经被其他事务提交的变更，可以避免脏读，但是不可重复读和幻读问题都可能出现|
|Repeatable read<br/>（可重复读）|确保事务可以多次从一个字段读取相同的值，在这个事务持续期间，**禁止其他事务对这个字段进行更新**，可以避免脏读和不可重复读，但避免不了幻读|
|serializable<br/>（串行化）|确保事务可以从一个表中读取相同的行，在这个事务持续期间，**禁止其他事物对该表进行插入、更新和删除操作**，所有的并发问题都可以避免，但是效率十分低下。|

<br/>

Oracle支持两种事务隔离，read commited (读已提交数据)和serializable（串行化），默认是read commited 

MySQL支持四种事务隔离，默认的事务隔离是Repeatable read（可重复读）

**设置当前连接的隔离级别**

set session transaction isolation level XXX ; -- 但是需要重启数据库

**设置数据库系统的全局隔离级别**

set global transaction isolation level XXX; -- 但是需要重启数据库

##### 设置读未提交隔离级别

```mysql
#会话1，查看当前数据库的隔离级别
mysql> show variables like '%isolation%';
+-----------------------+-----------------+
| Variable_name         | Value           |
+-----------------------+-----------------+
| transaction_isolation | REPEATABLE-READ |
+-----------------------+-----------------+

#会话1，修改为最低的隔离级别
set session transaction isolation level read uncommitted;
mysql> show variables like '%isolation%';
+-----------------------+------------------+
| Variable_name         | Value            |
+-----------------------+------------------+
| transaction_isolation | READ-UNCOMMITTED |
+-----------------------+------------------+
#会话1，开始验证，使用test库
mysql> use test;
Database changed
mysql> select *from account;
+----+-----------+---------+
| id | username  | balance |
+----+-----------+---------+
|  1 | 张无忌    |     500 |
|  4 | 赵敏      |    1500 |
+----+-----------+---------+

#会话1，开启事务
set autocommit=0;
start transaction;
update account set username='john' where id=1;

#会话2，此时事务没有结束，再开启另外一个链接,记得还是要修改隔离级别为read uncommitted
set session transaction isolation level read uncommitted;
set autocommit=0;
mysql> select * from account; -- 看到名字变了，但是前面的事务还没有提交，复现了脏读
+----+----------+---------+
| id | username | balance |
+----+----------+---------+
|  1 | john     |     500 |
|  4 | 赵敏     |    1500 |
+----+----------+---------+

#会话1，事务1回滚
rollback;
#会话2，事务2再查，变回去了
mysql> select * from account;
+----+-----------+---------+
| id | username  | balance |
+----+-----------+---------+
|  1 | 张无忌    |     500 |
|  4 | 赵敏      |    1500 |
+----+-----------+---------+
```

<br/>

##### 设置读已提交隔离级别

```mysql
#会话1，
set session transaction isolation level read committed;
set autocommit=0;
mysql> show variables like '%isolation%';
+-----------------------+----------------+
| Variable_name         | Value          |
+-----------------------+----------------+
| transaction_isolation | READ-COMMITTED |
+-----------------------+----------------+
#会话1，开始验证，使用test库
mysql> use test;
Database changed
mysql> select *from account;
+----+-----------+---------+
| id | username  | balance |
+----+-----------+---------+
|  1 | 张无忌    |     500 |
|  4 | 赵敏      |    1500 |
+----+-----------+---------+

#会话1，开启事务1
set autocommit=0;
start transaction;
update account set username='john' where id=1;


#会话2
set session transaction isolation level read committed;
set autocommit=0;
#名字没有变化 但是不可重复读和幻读没有办法避免
mysql> select * from account;
+----+-----------+---------+
| id | username  | balance |
+----+-----------+---------+
|  1 | 张无忌    |     500 |
|  4 | 赵敏      |    1500 |
+----+-----------+---------+


#但是没有解决不可重复读
#当会话1提交了
commit；
#此时会话2再查发现表中数据变化了，前后不一样，所以出现了不可重复读情况
```

<br/>

##### 设置重复读隔离级别

```mysql
#会话1，
set session transaction isolation level repeatable read;
set autocommit=0;
mysql> show variables like '%isolation%';
+-----------------------+-----------------+
| Variable_name         | Value           |
+-----------------------+-----------------+
| transaction_isolation | REPEATABLE-READ |
+-----------------------+-----------------+
#会话1，开启事务1
set autocommit=0;
start transaction;
update account set username='john' where id=1;
#此时切换到会话2

#会话2
set session transaction isolation level repeatable read;
set autocommit=0;
mysql> select * from account; -- 此时没有改为john，所以没有脏读
+----+-----------+---------+
| id | username  | balance |
+----+-----------+---------+
|  1 | 张无忌    |     500 |
|  4 | 赵敏      |    1500 |
+----+-----------+---------+

#会话1提交
commit;

#会话2检查 没有改，说明在事务2执行的期间，事务1不允许对这个字段进行更新
mysql> select * from account;
+----+-----------+---------+
| id | username  | balance |
+----+-----------+---------+
|  1 | 张无忌    |     500 |
|  4 | 赵敏      |    1500 |
+----+-----------+---------+
mysql> commit; -- 再新开一个事务，此时就更新了
Query OK, 0 rows affected (0.00 sec)

mysql> select * from account;
+----+----------+---------+
| id | username | balance |
+----+----------+---------+
|  1 | john     |     500 |
|  4 | 赵敏     |    1500 |
+----+----------+---------+
```

<br/>

##### 设置串行化隔离级别

```mysql
#会话1，
set session transaction isolation level serializable;
set autocommit=0;
mysql> show variables like '%isolation%';
+-----------------------+--------------+
| Variable_name         | Value        |
+-----------------------+--------------+
| transaction_isolation | SERIALIZABLE |
+-----------------------+--------------+
mysql> select * from account;
+----+----------+---------+
| id | username | balance |
+----+----------+---------+
|  1 | john     |     500 |
|  4 | 赵敏     |    1500 |
+----+----------+---------+
update account username='mmm'; -- 2行受影响
#此时切换到会话2进行插入操作发现阻塞了
#直到会话1执行以下commit后，会话2才返回
commit;
#会话2
set session transaction isolation level serializable;
set autocommit=0;
mysql> insert into account value(null,'yyz',5000); -- 这句阻塞了！！！ 如果没有这个级别的，就会插入成功
```

<br/>

#### savepoint回滚点

语法：savepoint 节点名 

用来设置保存点 ，回滚到保存点必须搭配rollback使用

```mysql
#演示savepoint的使用
mysql> select * from account; -- 此时有3条数据
+----+----------+---------+
| id | username | balance |
+----+----------+---------+
|  1 | mmm      |     500 |
|  4 | mmm      |    1500 |
|  7 | yyz      |    5000 |
+----+----------+---------+

set auto commit=0;
start transaction;
delete from account where id=1;
savepoint a; -- 设置一个保存点叫a
delete from account where id=4;
rollback to a; 


mysql> select * from account; -- 最后1号删了4号没删回滚了
+----+----------+---------+
| id | username | balance |
+----+----------+---------+
|  4 | mmm      |    1500 |
|  7 | yyz      |    5000 |
+----+----------+---------+

```

<br/>

<br/>

## 九、视图

含义：虚拟表，和普通表一样使用。MySQL5.1版本后出现的新特性。是通过表动态生成的数据。只保存sql逻辑，不保存查询结果。

好处：

	1.重用sql语句

	2.简化复杂sql操作，不必知道查询细节

	3.保护数据，提高了安全性

```mysql
/*
 *  语法：
 *    create view 视图名
 *    as 复杂的查询语句
 *
 *  应用场景：
 *    1.多个地方用到同样的查询结果
 *    2.该查询结果用到的sql比较复杂
 */
 
 
#案例：
use student;
#查询姓张的学生名字和专业名字
#以前的做法
mysql> select s.studentname,m.majorname 
from student s 
inner join major m on s.majorid=m.majorid 
where s.studentname like '张%';
+-------------+-----------+
| studentname | majorname |
+-------------+-----------+
| 张三封      | javaee    |
| 张翠山      | javaee    |
| 张无忌      | html5     |
+-------------+-----------+

create view v1 as
select s.studentname,m.majorname 
from student s 
inner join major m on s.majorid=m.majorid ;
#这样可以直接查
mysql> select * from v1 where s.studentname like '张%';;
+-------------+-----------+
| studentname | majorname |
+-------------+-----------+
| 张三封      | javaee    |
| 张翠山      | javaee    |
| 张无忌      | html5     |
+-------------+-----------+
```

<br/>

### 创建视图

```mysql
use myemployees;

#案例1:查询名字中包含a字符的员工名字、部门名字和工种信息
#创建视图
mysql> create view v1 as  
select e.last_name,d.department_name,j.job_title  
from employees e 
inner join departments d on e.department_id=d.department_id 
inner join jobs j on j.job_id=e.job_id;
#使用视图
mysql> select * from v1 where last_name like '%a%';


#查询各部门的平均工资级别
#首先查询到各部门的平均工资
mysql> select e.department_id ,avg(salary) as avgsal from employees e group by e.department_id;
#再把上一步的查询结果做成一个视图
create view v2 as
select e.department_id ,avg(salary) as avgsal from employees e group by e.department_id;
#使用视图和等级表进行连接
mysql> select v.department_id,jg.grade_level from v2 v  
inner join job_grades  jg on v.avgsal between jg.lowest_sal and jg.highest_sal;


#查询平均工资最低的部门名和工资
#这里可以服用上一步的视图,并且做成视图
create view v3 as
select * from v2 order by avgsal asc limit 1;
#视图连接部门表
mysql> select d.department_name,v.avgsal  
from departments d  
inner join v3 v on v.department_id=d.department_id;
```

<br/>

### 修改视图

```mysql
#方式1
/*
 *  语法：
 *    create or replace view 视图名
 *      as 查询语句;
 *    如果该视图存在就修改，不存在就创建
 */
#案例，修改上面v3的视图为工种的平均工资
create or replace view v3 as
select job_id,avg(salary) as avgsal from employees group by job_id;


#方式2
/*
 *  语法：
 *  alter view 视图名
 *    as 查询语句;
 *  这里视图必须存在
 */
 
#案例
alter view v3 as
select * from employees;
```

<br/>

### 删除视图

```mysql
/*
 *  语法：
 *    drop view 视图名,视图名,视图名； -- 可以删除多个
 *
 */
 drop view v1,v2,v3;
```

<br/>

### 查看视图的结构

```mysql
/*
 *
 *
 */
#案例
#先创建一个视图
create or replace view v3 as
select job_id,avg(salary) as avgsal from employees group by job_id;
#查看视图
mysql> desc v3;
+--------+--------------+------+-----+---------+-------+
| Field  | Type         | Null | Key | Default | Extra |
+--------+--------------+------+-----+---------+-------+
| job_id | varchar(10)  | YES  |     | NULL    |       |
| avgsal | double(23,6) | YES  |     | NULL    |       |
+--------+--------------+------+-----+---------+-------+
mysql> show create view v3;
+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+
| View | Create View                                                                                                                                                                                                          | character_set_client | collation_connection |
+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+
| v3   | CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v3` AS select `employees`.`job_id` AS `job_id`,avg(`employees`.`salary`) AS `avgsal` from `employees` group by `employees`.`job_id` | utf8                 | utf8_general_ci      |
+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+
mysql> show create view v3\G;
*************************** 1. row ***************************
                View: v3
         Create View: CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v3` AS select `employees`.`job_id` AS `job_id`,avg(`employees`.`salary`) AS `avgsal` from `employees` group by `employees`.`job_id`
character_set_client: utf8
collation_connection: utf8_general_ci

```

<br/>

作业

```mysql
#1.创建视图emp_v1，要求查询电话号码以‘011’开头的员工姓名和工资和邮箱
mysql> create or replace view emp_v1 as
select last_name,salary,email from employees 
where phone_number like '011%';

#2.创建视图emp_v2,要求查询部门的最高工资大于12000的部门信息
create or replace view emp_v2 as
select department_id,max(salary) as maxsal from employees group by department_id having maxsal>12000;

mysql> select d.* from departments d 
inner join emp_v2 e on d.department_id=e.department_id;

drop view emp_v1,emp_v2;
```

<br/>

### 视图的更新

更改视图中的数据

视图的可更新性和视图中的查询定义有关系，以下类型不能更新

	1.包含以下关键字的sql语句：分组函数，group by,distinct,having union union all

	2.常量视图

	3.select 中包含子查询

	4.from一个不能更新的视图

	5.where子句的子查询引用了from子句中的表

```mysql
create or replace view myv1 as
select last_name,email,salary*12*(1+ifnull(commission_pct,0)) as "annual salary"
from employees;

mysql> select * from myv1;

#1.插入数据
insert into myv1 values('张飞','zf@qq.com',100000); --  Column 'annual salary' is not updatable
#修改一下视图
create or replace view myv1 as
select last_name,email
from employees;
#插入数据
insert into myv1 values('张飞','zf@qq.com'); -- 视图中和原始表中都有这条数据

#2.修改数据
update myv1 set last_name='张无忌' where last_name='张飞';-- 视图中和原始表中这条数据都更新了

#3.删除数据
delete from myv1 where last_name='张无忌';-- 视图中和原始表中这条数据都删除了



#不能更新的视图之常量视图
create or replace view myv2 as
select 'john' name;
update myv2 set name='lucy'; -- 报错
#不能更新的视图之where子句的子查询引用了from子句中的表
create or replace view myv2 as
select last_name,email,salary
from employees 
where employee_id in
(
  select manager_id from employees where manager_id is not null
);
```

<br/>

### 视图和表的对比

||创建语法|是否实际占用物理空间|使用|
|--|--|--|--|
|视图|create view|只是保存了sql逻辑|一般不能增删改|
|表|create table|实际保存了数据|增删改查|

<br/>

<br/>

## 十、变量

变量的分类

```mysql
/*
 *  系统变量
 *      全局变量
 *      会话变量
 *
 *  自定义变量
 *      用户变量
 *      局部变量
 */
```

<br/>

### 系统变量

变量是由系统提供的，不是用户定义的，属于服务器层面。

```mysql
#查看系统变量的语法
#1.查看所有的全局系统变量\会话系统变量
show global｜【session】 variables;

#2.查看满足条件的全局｜会话系统变量
show global｜【session】 variables like '%xxx%';

#3.查看指定的系统变量
select @@global.系统变量名字;
select @@session.系统变量名字;-- 可以不写session

#4.为某个系统变量赋值
#方式一
set global 变量名字 =xx;
set session 变量名字 =xx;-- 可以不写session
#方式二
set @@global.变量名字 =xx;
set @@session.变量名字 =xx; -- 可以不写session
```

#### 全局变量

		作用域：服务器每次启动都会为所有的全局变量赋予初始值，针对所有的会话（连接）有效，但是不能跨重启（重启后失效，如果要持久，必须修改配置文件）。

```mysql
#案例：查看所有的全局变量
show global variables;
#案例：查看部分的全局变量
show global variables like '%isolation%';
#案例：查看制定的全局变量
mysql> select @@global.transaction_isolation;
+--------------------------------+
| @@global.transaction_isolation |
+--------------------------------+
| REPEATABLE-READ                |
+--------------------------------+
#案例：为某个全局变量赋值
set global autocommit=0; -- 跨链接有效,新开启一个会话查到都是0
set @@global.autocommit=1;
```

<br/>

#### 会话变量

	作用域：仅仅针对当前的会话有效。

```mysql
#案例：查看所有的会话变量
show session variables; -- 可以不写session
#案例：查看部分的会话变量
show session variables like '%isolation%';
#案例：查看制定的会话变量
mysql> select @@session.transaction_isolation;
+---------------------------------+
| @@session.transaction_isolation |
+---------------------------------+
| REPEATABLE-READ                 |
+---------------------------------+
#案例：为某个会话变量赋值
set session autocommit=0; -- 跨链接无效,新开启一个会话查到还是1
set @@session.autocommit=1;
```

<br/>

### 自定义变量

含义：变量是用户自定义的，不是由系统提供的。

使用步骤：声明、赋值、使用（查看、比较、运算）

<br/>

#### 用户变量

作用域：针对当前的会话（连接）有效，同于会话变量的作用域。

应用于任何地方，可以放在begin end 的里面，或者外面

```mysql
/*
 *  语法：
 *    1.声明并初始化(3种,赋值操作符为=和:=)：
 *      set @用户变量名=值;
 *      set @用户变量名:=值;
 *      select @用户变量名:=值;
 *    2.赋值更新用户变量
 *        通过上面的三种方式，声明初始化也可以用来更新
 *        select 变量值 into @变量名 from 表;
 *    3.查看用户变量的值
 *        select @用户变量名;
 *  
 *  
 *  
 */
 
#案例
set @name='john';
select @name:=100;

#案例
select count(*) into people from employees;
mysql> select count(*) into @count from employees;
mysql> select @count;
+--------+
| @count |
+--------+
|    107 |
+--------+

#案例：声明2个变量并赋予初始值，求和并打印
set @num1=1;
set @num2=2;
set @sum=@num1+@num2;
select @sum;
```

<br/>

#### 局部变量

作用域：仅仅在begin end中间有效

应用在begin end 中间，而且是在begin后第一句。

```mysql
/*
 *  语法：
 *    1.声明
 *      declare 变量名 类型 
 *      declare 变量名 类型 default 值;
 *    2.赋值 
 *      set 局部变量名=值;--注意不用加@
 *      set 局部变量名:=值;--注意不用加@
 *      select @局部变量名:=值; -- 这里要加@
 *      select 变量值 into 局部变量名 from 表; --注意不用加@
 *    3.使用
 *      select 局部变量名; -- 不用加@
 */
 
 
#案例：声明2个变量并赋予初始值，求和并打印
 
 
 
#案例
create procedure myp3(in username varchar(20),in password varchar(20))
begin
declare result varchar(20) default ''; -- 1.声明并初始化变量
select count(*) into result -- 2.赋值变量
from admin 
where admin.username=username and admin.password=password;

select result; -- 3.使用变量
end $
```

<br/>

#### 用户变量和局部变量的对比

||作用域|定义和使用的位置|语法|
|--|--|--|--|
|用户变量|当前的会话|会话中的任何地方|必须加@符号，不用限定类型|
|局部变量|begin end中|只能在begin end 中，且为第一句|一般不用加@，需要限定类型|

<br/>

## 十一、存储过程和函数

<br/>

### 存储过程

含义：一组**预先编译好**的sql语句集合，理解成批处理语句。

存储过程往往是做增删改。

好处：

	1.提高代码的重用性

	2.简化了操作

	3.减少了编译次数，并且减少了数据库的连接次数，提高了效率。

<br/>

#### 创建存储过程和调用存储过程

```mysql
/*
 *  语法：
 *    create procedure 存储过程名(参数列表)
 *    begin
 *        存储过程体（一组合法的sql语句）
 *    end
 *
 *
 *  注意点：
 *    1.参数列表包含3部分：参数模式、参数名、参数类型 eg:in stuname varchar(20)
 *      参数模式由三个：IN/OUT/INOUT
 *      IN：该参数需要调用方传值
 *      OUT：该参数可以作为返回值
 *      INOUT：类似于引用，传入参数，也会返回值
 *    2.如果存储过程中只有一句话，那么begin end可以省略不写
 *    3.存储过程体中每条sql语句结尾必须加分号；
 *      存储过程结尾可以使用delimiter重新设置
 *      语法：delimiter 结束标记  
 *      eg：delimiter $
 *          begin
 *          ...
 *          end $
 *      注意这里修改了分界符，后面都得用$
 */
 
 
/*
 *  语法：
 *    call 存储过程名(实参列表);
 */
```

案例

```mysql
#1.空参数列表的存储过程
#案例：插入到admin表中五条记录
use girls;
mysql> select * from admin;
+----+----------+----------+
| id | username | password |
+----+----------+----------+
|  1 | john     | 8888     |
|  2 | lyt      | 6666     |
+----+----------+----------+
#创建存储过程
delimiter $
create procedure myp1()
begin
insert into admin(username,password) 
values('john','0000'),
('lily','0000'),
('rose','0000'),
('jack','0000'),
('tom','0000');
end $
#调用存储过程
call myp1()$
mysql> select * from admin$
+----+----------+----------+
| id | username | password |
+----+----------+----------+
|  1 | john     | 8888     |
|  2 | lyt      | 6666     |
|  3 | john     | 0000     |
|  4 | lily     | 0000     |
|  5 | rose     | 0000     |
|  6 | jack     | 0000     |
|  7 | tom      | 0000     |
|  8 | john     | 0000     |
|  9 | lily     | 0000     |
| 10 | rose     | 0000     |
| 11 | jack     | 0000     |
| 12 | tom      | 0000     |
+----+----------+----------+

#---------------------------------------------------------------------------
#2.创建带in模式参数的存储过程,这里的in类型参数就是个局部变量
#案例：根据女神名字，查询对应的男神信息
#创建存储过程
create procedure myp2(in beautyName varchar(20))
begin 
select bo.* from boys bo
left join beauty be on bo.id=be.boyfriend_id
where be.name=beautyName; 
end $
#调用存储过程
mysql> call myp2('王语嫣')$
+----+---------+--------+
| id | boyName | userCP |
+----+---------+--------+
|  4 | 段誉    |    300 |
+----+---------+--------+

#案例：创建存储过程来实现，用户是否登录成功，传入一个用户名和密码，和admin表中数据进行对比看是否登陆成功
create procedure myp3(in username varchar(20),in password varchar(20))
begin
declare result varchar(20) default ''; -- 1.声明并初始化变量
select count(*) into result -- 2.赋值变量
from admin 
where admin.username=username and admin.password=password;
select result; -- 3.使用变量
end $
#调用存储过程
mysql> call myp3('张飞','8888')$
+--------+
| result |
+--------+
| 0      |
+--------+
mysql> call myp3('jack','0000')$
+--------+
| result |
+--------+
| 2      |
+--------+
#改进版本
create procedure myp4(in username varchar(20),in password varchar(20))
begin
declare result int default 0; -- 1.声明并初始化变量
select count(*) into result -- 2.赋值变量
from admin 
where admin.username=username and admin.password=password;
select if(result>0,'登录成功','登录失败'); -- 3.使用变量
end $
mysql> call myp4('张飞','8888')$
+--------------------------------------------+
| if(result>0,'登录成功','登录失败')         |
+--------------------------------------------+
| 登录失败                                   |
+--------------------------------------------+
mysql> call myp4('jack','0000')$
+--------------------------------------------+
| if(result>0,'登录成功','登录失败')         |
+--------------------------------------------+
| 登录成功                                   |
+--------------------------------------------+



#---------------------------------------------------------------------------
#3.创建带out模式的存储过程
#案例1:根据女神名字，返回对应的男神名 --- 带一个out
create procedure myp5(in beautyName varchar(20),out boyName varchar(20))
begin
select  bo.boyName into boyName
from boys bo
inner join beauty be on bo.id=be.boyfriend_id
where be.name=beautyName;
end $
#调用
set @bname=''$
call myp5('小昭',@bname)$
select @bname$
+-----------+
| @bname    |
+-----------+
| 张无忌    |
+-----------+
#案例2:根据女神名，返回对应的男神名和男神魅力值,注意into只能用一次
create procedure myp6(in beautyName varchar(20),out boyName varchar(20),out userCP int)
begin
select bo.boyName,bo.userCP into boyName,userCP
from boys bo
inner join beauty be on bo.id=be.boyfriend_id
where be.name=beautyName;
end $
#调用
call myp6('小昭',@bName,@usercp)$
select @bname,@usercp$
+-----------+---------+
| @bname    | @usercp |
+-----------+---------+
| 张无忌    |     100 |
+-----------+---------+



#---------------------------------------------------------------------------
#4.创建带inout模式的存储过程
#案例1:传入a和b2个值，q和b都翻倍并返回
create procedure myp7(inout a int,inout b int)
begin 
  set a=a*2;
  set b=b*2;
end $

#调用
set @m=10$
set @n=20$
call myp7(@m,@n)$
select @m,@n$
+------+------+
| @m   | @n   |
+------+------+
|   20 |   40 |
+------+------+
```

<br/>

作业

```mysql
delimiter $
#创建存储过程，实现传入用户名和密码，插入到admin表中
create procedure test_pro1(in username varchar(20),in password varchar(20))
begin
insert into admin(admin.username,admin.password) values(username,password);
end$
call test_pro1('yyz','666')$

#创建存储过程，实现传入女神的编号，返回女神的名称和电话
create procedure test_pro2(in id int, out name varchar(50),out phone varchar(11))
begin
select be.name,be.phone into name,phone 
from beauty be
where be.id=id;
end $
call test_pro2(1,@bename,@bephone)$
select @bename,@bephone$
+---------+-------------+
| @bename | @bephone    |
+---------+-------------+
| 柳岩    | 18209876577 |
+---------+-------------+

#创建存储过程或函数，实现传入两个女神的生日，返回大小
create procedure test_pro3(in be1 datetime,in be2 datetime, out result int)
begin
  select datediff(be1,be2) into result;
end $
mysql> call test_pro3('1993-3-3','1994-9-19',@ret)$
mysql> select @ret$
+------+
| @ret |
+------+
| -565 |
+------+

#创建存储过程，实现传入一个日期，格式化为xx年xx月xx日返回
create procedure test_pro4(in mydate datetime,out result varchar(50))
begin
select date_format(mydate,'%y年%m月%d日') into result;
end $

call test_pro4('1994-9-19',@ret)$
select @ret$
+-----------------+
| @ret            |
+-----------------+
| 94年09月19日    |
+-----------------+
call test_pro4(now(),@ret)$


#创建存储过程或函数，实现传入女神的姓名，返回‘女神 and 男神’ 名字的字符串
create procedure test_pro5(in beautyName varchar(20),out ret varchar(50))
begin
  select concat(be.name,'AND',ifnull(bo.boyName,'null')) into ret
  from beauty be
  left join boys bo on be.boyfriend_id=bo.id
  where be.name=beautyName;
end $

call test_pro5('柳岩',@ret)$
select @ret$
+---------------+
| @ret          |
+---------------+
| 柳岩ANDnull   |
+---------------+


#创建存储过程或函数，根据传入的条目数和起始索引，查询beauty表中的记录
create procedure test_pro6(in size int,in offset int )
begin
  select * from beauty limit offset,size;
end $
call test_pro6(3,5)$
```

<br/>

#### 删除存储过程

```mysql
/*
 *  语法：
 *    drop procedure 存储过程名称;
 *  注意：只能一次删除一个
 */
 
drop procedure myp1;
```

<br/>

#### 查看存储过程的信息

```mysql
show create procedure myp2;
show create procedure myp2\G;
```

<br/>

### 函数

含义：一组**预先编译好**的sql语句集合，理解成批处理语句。

好处：

	1.提高代码的重用性

	2.简化了操作

	3.减少了编译次数，并且减少了数据库的连接次数，提高了效率

**存储过程和函数的区别**

	存储过程可以有0个返回，也可以有多个返回；适合做批量插入、批量更新等操作。

	函数有且只有1个返回；适合做处理数据后返回一个结果

<br/>

#### 创建函数和调用函数

```mysql
/*
 *  语法：
 *    create function 函数名(参数列表) returns 返回类型
 *    begin
 *      函数体
 *        return 值
 *    end 
 *  
 *  注意：
 *    1.参数列表包含两部分：参数名和参数类型，没有参数模式！！！
 *    2.函数体一定有return 语句，否则会报错；如果return语句没有放在函体的最后也不报错，但是不建议。
 *    3.当函数体内只有一句话，可以省略begin end
 *    4.使用delimiter 语句设置结束标志
 */
 
 
/*
 *  语法：
 *    select 函数名(参数列表)
 *
 */
```

案例

```mysql
#先打开创建函数的功能，mysql默认是关闭的
set global log_bin_trust_function_creators=true;
mysql> show global variables  like '%_function_creators%'$
+---------------------------------+-------+
| Variable_name                   | Value |
+---------------------------------+-------+
| log_bin_trust_function_creators | ON    |
+---------------------------------+-------+

use myemployees;

#---------------------------------------------------------------------------
#1.无参数有返回值的函数
#案例：返回公司的员工个数
create function myf1() returns int
begin 
  declare ret int default 0; -- 定义一个变量
  select count(*) into ret  -- 为变量赋值
  from employees;
  return ret;
end $
select myf1()$
+--------+
| myf1() |
+--------+
|    107 |
+--------+

#---------------------------------------------------------------------------
#2.有参数有返回值的函数
#案例1：根据员工名返回他的工资
create function myf2(name varchar(20)) returns double
begin
  set @sal=0; -- 定义用户变量
  select salary into @sal from employees where last_name=name limit 1;
  return @sal;
end $
select myf2('K_ing')$
+---------------+
| myf2('K_ing') |
+---------------+
|         24000 |
+---------------+

#案例2:根据部门名，返回该部门的平均工资
create function myf3(dname varchar(50)) returns double
begin
  set @sal=0;
  select avg(salary) into @sal
  from employees e 
  inner join departments d on e.department_id=d.department_id
  where d.department_name=dname;
  return @sal;
end $
select myf3('IT')$
+------------+
| myf3('IT') |
+------------+
|       5760 |
+------------+
```

<br/>

#### 删除存储过程

```mysql
drop function myf2;
```

<br/>

#### 查看存储过程

```mysql
show create function myf3;
show create function myp3\G;
```

<br/>

**函数和存储过程都存储在系统库mysql里的proc表里面**

```mysql
这块没找到
```

<br/>

作业

```mysql
#案例：创建函数，实现传入2个float，返回2者和
create function test_func1(num1 float,num2 float) returns float
begin
  declare sum float default 0;
  set sum=num1+num2;
  return sum;
end $
select test_func1(1,2)$
+-----------------+
| test_func1(1,2) |
+-----------------+
|               3 |
+-----------------+
```

<br/>

<br/>

## 十二、流程控制结构

顺序结构：程序从上往下依次执行

分支结构：程序从两条或者多条路径中选择一条执行

循环结构：程序在满足一定条件的基础上，重复执行一段代码

<br/>

### 分支结构

```mysql
#---------------------------------------------------------------------------
#1.if函数
/*
 *  语法：
 *    if(exp1,exp2,exp3); -- exp1成立返回exp2，否则返回exp3
 */
#案例
mysql> select if(10>5,'大','小');
+----------------------+
| if(10>5,'大','小')   |
+----------------------+
| 大                   |
+----------------------+
mysql> select last_name,commission_pct,if(commission_pct is null,'没奖金','有奖金') from employees;


#---------------------------------------------------------------------------
#2.case结构
# case函数的使用1:
#  语法：
#     case 要判断的字段或表达式
#     when 常量1 then 要显示的值或语句（值不用加分号，语句要加）;
#     ...
#     else 要现实的值或语句（默认情况）;
#     end case;
#
#   特点：
#     1.可以作为表达式，嵌套在其他语句中使用，可以放在任何地方，比如begin end中或者外面；
#       可以作为独立语句去使用，只能放在begin end中
#     2.如果when中的语句满足或者条件成立，则执行对应的then后面的语句，并且结束case
#       如果都不满足，执行else中的语句或者值
#     3.else可以省略，但是所有的when都不满足且没有else，则返回null
#

#案例：作为表达式去使用
#案例：查询员工的工资：如果部门号为30，显示工资的1.1倍；为40显示1.2倍，50为1.3倍，其余的1倍
select last_name,department_id,salary,
(
  case department_id
  when 30 then 1.1*salary
  when 40 then 1.2*salary
  when 50 then 1.3*salary
  else salary
  end
) as wages
from employees;

# case函数的使用2：类似多重if
#   语法：
#     case
#       when 条件1 then 值/语句;
#       when 条件2 then 值/语句;
#       else 值/语句;
#     end case;

#案例：查询员工工资，大于等于20000，显示A级别，大于等于15000显示B级别，大于等于10000显示C级别，否则显示D级别
select last_name,
(
  case
  when salary>=20000 then 'A'
  when salary>=15000 then 'B'
  when salary>=10000 then 'C'
  else 'D'
  end
) as class 
from employees;



#案例：作为独立语句去使用
#创建存储过程，根据传入的成绩，90-100显示A，80-90显示B，60-80显示C，否则显示D
create procedure test_case(in grade int)
begin
  declare ret char(1) default 'D';
  case
  when grade>=90 and grade<=100 then select 'A';
  when grade>=80 then select 'B';
  when grade>=60 then select 'C';
  else select 'D';
  end case;
end $
call test_case(95)$
+---+
| A |
+---+
| A |
+---+



#---------------------------------------------------------------------------
#3.if结构
/*
 *  语法：
 *    if 条件1 then 语句1;
 *    elseif 条件2 then 语句2;
 *    ...
 *   【else 语句n;】
 *    end if
 *
 *  注意：只能用在begin end中间
 */
#案例：#创建函数，根据传入的成绩，90-100返回A，80-90返回B，60-80返回C，否则返回D
create function test_case1(score int) returns char(1)
begin
if score>=90 and score<=100 then return 'A';
elseif score>=80 then return 'B';
elseif score>=60 then return 'C';
else return 'D';
end if;
end $

select test_case1(50)$
+----------------+
| test_case1(50) |
+----------------+
| D              |
+----------------+
```

<br/>

### 循环结构

都只能放在begin end中间

切记、必须放在begin end里面

分类：while、loop、repeat

循环控制：iterate类似于continue、leave类型于break

```mysql
#---------------------------------------------------------------------------
#1.while循环
/*
 *  语法：
 *    【标签:】while 循环条件 do
 *      循环体;
 *    end while 【标签】
 *
 */
 
 
 
#---------------------------------------------------------------------------
#2.loop循环
/*
 *  语法：
 *    【标签:】loop
 *      循环体;
 *    end loop 【标签】
 *
 *    可以用来描述简单的死循环
 */
  
  
#---------------------------------------------------------------------------
#3.repeat循环
/*
 *  语法：
 *    【标签:】repeat
 *      循环体;
 *    until 结束循环的条件
 *    end repeat 【标签】;
 *
 *    可以用来描述简单的死循环
 */
 
 
#案例：没有循环控制；批量插入，根据次数插入到admin表中多条记录
use girls$
create procedure pro_while1(in insertCount int)
begin
  declare i int default 1;
  a:while i<=insertCount do
    insert into admin(username,password) values(concat('Rose',i),'666');
    set i=i+1;
  end while a;
end $
call pro_while1(10)$

#案例：添加leave；批量插入，根据次数插入到admin表中多条记录，如果次数大于20则停止
truncate table admin$
drop procedure pro_while1$
create procedure pro_while1(in insertCount int)
begin
  declare i int default 1;
  a:while i<=insertCount do
    insert into admin(username,password) values(concat('xiao',i),'666');
    if i>=20 then leave a; -- 标签在这用
    end if;
    set i=i+1;
  end while a;
end $
call pro_while1(100)$

#案例，添加iterate语句，批量插入，根据次数插入到admin表中多条记录，只插入偶数次
truncate table admin$
drop procedure pro_while1$
#注意这里的i累加必须放在iterate前面，否则跳过了更新i值造成死循环
create procedure pro_while1(in insertCount int)
begin
  declare i int default -1;
  a:while i<=insertCount do
    set i=i+1;
    if mod(i,2)!=0 then iterate a;
    end if;
    insert into admin(username,password) values(concat('jack',i),'666');
  end while a;
end $
call pro_while1(100)$
```

<br/>

#### 循环总结

|名称|语法|特点|位置|
|--|--|--|--|
|while|Label:while condition  do<br/>	loop_list;<br/>end while Label;|先判断后执行|begin和end中间|
|repeat|Label:repeat<br/>	loop_list;<br/>until condition<br/>end repeat Label;|先执行后判断|begin和end中间|
|loop|Label:loop<br/>	loop_list<br/>end loop Label；|没有条件的死循环|begin和end中间|

<br/>

### 流程控制的经典案例

```mysql
#已知表stringcontent
#其中字段 id自增长，content varchar(20)
#要求向该表插入指定个数的随机字符串
drop table if exists stringcontent$
create table stringcontent
(
id int primary key auto_increment,
content varchar(20)
)$

create procedure test_random_str_insert(in insertCount int)
begin
  declare i int default 1;
  declare str varchar(26) default 'abcdefghigklmnopqrstuvwxyz';
  declare offset int default 1;
  declare len int default 1;
  while i<=insertCount do
    set offset=floor(rand()*26+1); -- 产生偏移量
    set len=floor(rand()*(20-offset+1)+1); -- 产生长度 -- 这里因为要求content长度是20，所以要求长度最大是20
    insert into stringcontent(content) values(substr(str,offset,len));
    set i=i+1;
  end while;
end $
call test_random_str_insert(100)$
```
