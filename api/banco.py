import MySQLdb

class Database(object):

    def __init__(self):
        pass

    def Inserir(self, usuario, texto):

        values = []
        values.append(usuario)
        values.append(texto)

        q = """INSERT INTO `mbcorporate01`.`UltimosTw` (`Usuario`, `Texto`) VALUES (%s, %s);"""

        my_host = 'mysql.mbcorporate.com.br'
        my_user = 'mbcorporate01'
        my_passwd = 'Desafio2017'
        my_dbname = 'mbcorporate01'

        connection = MySQLdb.connect(host = my_host, user = my_user, passwd = my_passwd, db = my_dbname, charset='utf8', init_command='SET NAMES UTF8')
        cursor = connection.cursor()
        try:
            cursor.execute(q, values)
            connection.commit()
        except:
            connection.rollback()
        connection.close()


    # IMPLEMENTAR: vou contar quantos tweets foram gravados no banco.. select count por exemplo .....
    def query(self, q):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q)
        return cursor.fetchall()
