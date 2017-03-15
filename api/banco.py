# testando acesso ao mysql

import MySQLdb

class Database:
    host = 'mysql.mbcorporate01.com.br'
    user = 'mbcorporate01'
    passwd = 'Desafio2017'
    db = 'mbcorporate01'

    def __init__(self):
        self.connection = MySQLdb.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.db)

    def query(self, q):
        #self.connection = MySQLdb.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.db)

        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q)

        #self.connection.close()
        return cursor.fetchall()

        #return cursor.fetchall()


    def queryWithParams(self, q, params):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q, params)


    def __del__(self):
        self.connection.close()
