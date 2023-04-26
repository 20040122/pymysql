# 1. 导入pymysql模块
import pymysql
# 2. 创建连接对象
conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="mysql",charset="utf8")
# 3. 创建游标对象
cursor=conn.cursor()
# 4. 执行sql语句
cursor.execute("select version()")
# 5. 获取结果
result=cursor.fetchone()
print(result[0])
# 6. 关闭游标对象
cursor.close()
# 7. 关闭连接对象
conn.close()
