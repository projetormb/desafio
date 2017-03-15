import MySQLdb

class Database(object):

    def __init__(self):

        my_host = 'mysql.mbcorporate01.com.br'
        my_user = 'mbcorporate01'
        my_passwd = 'Desafio2017'
        my_dbname = 'mbcorporate01'

        self.connection = MySQLdb.connect(host = my_host, user = my_user, passwd = my_passwd, db = my_dbname)

    def Inserir(self, usuario, texto):

        values = []
        values.append(usuario)
        values.append(texto)
        #values = ['zezinho', 'algum texto do zezinho']

        q  = 'START TRANSACTION;'
        q = 'INSERT INTO `mbcorporate01`.`UltimosTw` (`Usuario`, `Texto`) VALUES (%s, %s);'
        q += 'COMMIT;'

        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q, values)



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
        if self.connection is not None:
            self.connection.close()
