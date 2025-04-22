import pymysql # 导入操作MySQL数据库的模块


# 打开数据库连接
def open():
    db = pymysql.Connect(host='localhost', port=3306, user='root', password='20031223',
                                        database='shbnetshop', charset='utf8')

    return db # 返回连接对象
db = open()