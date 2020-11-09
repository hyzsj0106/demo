import pymysql


class MySql:

    def __init__(self, host, user, password, database, port):
        self.db = pymysql.connect(host=host, user=user, password=password, database=database,
                                  port=port, cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def update(self, sql, data):
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
        except:
            self.db.rollback()
            print('数据修改失败,请检查sql语句~')
            print(sql, data)

    def query(self, sql, data):
        try:
            result = self.cursor.execute(sql, data)

            return result
        except:
            print('数据查询失败,请查看sql语句~')


if __name__ == '__main__':
    db = MySql('localhost', 'root', '123456', 'rain', 3306)