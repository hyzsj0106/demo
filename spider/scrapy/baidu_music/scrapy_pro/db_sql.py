import pymysql

class MySql:

    def __init__(self, host, user, password, database, port):
        self.db = pymysql.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database,
                                  port=port,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  charset='utf8mb4')

        self.cursor = self.db.cursor()

    def update(self, sql, data):
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
        except:
            self.db.rollback()
            print('数据修改失败,请检查sql语句~')
            print(sql, data)

    def query(self, sql):
        try:
            result = self.cursor.execute(sql)

            return result
        except:
            print('数据查询失败,请查看sql语句~')

    def __del__(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':

    # 用前先测试
    db = MySql('localhost', 'root', '123456', 'kuname', 3306)
    sql = 'insert into demo values (%s, %s, %s, %s, %s, %s)'
    data = ()
    db.update(sql, data)