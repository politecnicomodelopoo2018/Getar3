import pymysql

class DB(object):

    @staticmethod
    def run(query):
        db = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'alumno',
                             db = 'mydb',
                             charset = 'utf8',
                             autocommit = 'True')

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        db.close()
        return cursor