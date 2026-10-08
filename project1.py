
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password="nitika@2008",database='Data_Analyst')
if conn.is_connected():
    print("connection ok")

cursor=conn.cursor()
# cursor.execute('show tables;')
# print(cursor.fetchall())
# q='select* from emp; '
# cursor.execute(q)
# print(cursor.fetchall())

# q='select*from emp where age=20;'
# cursor.execute(q)
# print(cursor.fetchall())

# q='select*from emp where age=%s'
# age=int(input('please enter id you want to fetch:'))
# cursor.execute(q,(age,))

# print(cursor.fetchall())


# t="create table user(id int,name varchar(20),password int);"
# cursor.execute(t)
# print("table")
# cursor.execute("show tables;")
# print(cursor.frtchall())
# t="insert into user values(1,'vani',1234);"
# cursor.execute(t)
# conn.commit()
# t="select*from user;"
# cursor.execute(t)
# print(cursor.fetchall())
user_name=input("Enter your name:")
password=int(input("Enter your password:"))
q="select* from user where name=%s AND password=%s"
cursor.execute(q(user_name,password))
if cursor.fetchone():
    print("Welcome to Dashboard")



