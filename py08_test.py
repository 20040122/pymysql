from py07_数据库工具类封装 import DBUtil

# DBUtil.uid("delete from test01 where id='2'")
print(DBUtil.select_all("select * from test01"))