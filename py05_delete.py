import pymysql

try:
    conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="test",charset="utf8")
    cursor=conn.cursor()
    sql="delete from test01 where id='2'"
    cursor.execute(sql)
    conn.commit()
    print(conn.affected_rows())
except Exception as e:
    print('Error:',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()