import MySQLdb

class Database(object):

    def __init__(self):

        host = 'mysql.mbcorporate01.com.br'
        user = 'mbcorporate01'
        passwd = 'Desafio2017'
        db = 'mbcorporate01'

        self.connection = MySQLdb.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.db)

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
        self.connection.close()
