import pymysql

try:
    conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="tpshop2.0",charset="utf8")
    cursor=conn.cursor()
    cursor.execute("select goods_name from tp_goods")
    result=cursor.fetchall()
    for i in result:
        print(i[0])
except Exception as e:
    print("Error: ",e)
finally:
    cursor.close()
    conn.close()