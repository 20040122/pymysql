import pymysql
class DBUtil():
    conn=None
    @classmethod
    def get_conn(cls):
        if cls.conn is None:
            cls.conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="test",charset="utf8")
        return cls.conn
    @classmethod
    def close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn=None
    @classmethod
    def select_all(cls,sql):
        cursor=None
        result=None
        try:
            cls.get_conn()
            cursor=cls.conn.cursor()
            cursor.execute(sql)
            result=cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            cls.close_conn()
            return result
    @classmethod
    def uid(cls,sql):
        cursor=None
        try:
            cls.get_conn()
            cursor=cls.conn.cursor()
            cursor.execute(sql)
            cls.conn.commit()
        except Exception as e:
            print(e)
            cls.conn.rollback()
        finally:
            cursor.close()
            cls.close_conn()

