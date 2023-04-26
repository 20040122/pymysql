# 1. 导入pymysql模块
import pymysql
# 2. 创建连接对象
conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="tpshop2.0",charset="utf8")
# 3. 创建游标对象
cursor=conn.cursor()
# 4. 执行sql语句,查询表tp_goods的3,4行数据
cursor.execute("select goods_name from tp_goods")
# 5. 获取结果,将游标位置置于2，自动从第三行开始读；
cursor.rownumber=2
result=cursor.fetchmany(2)
print(result[0][0])
print(result[1][0])
# 6. 关闭游标对象
cursor.close()
# 7. 关闭连接对象
conn.close()
