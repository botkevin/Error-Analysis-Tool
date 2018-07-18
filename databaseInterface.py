import mysql.connector as mariadb

class database_interface:

    def __init__(self, h, u, pswd, db, t, lt):
        self.mariadb_connection = mariadb.connect(host = h, user = u, password = pswd, database = db)
        self.cursor = self.mariadb_connection.cursor()
        self.table = t
        self.lt = lt

    #self, date, time, position, level, code, content
    def write(self, data):
        command = "INSERT INTO " + self.table + ' VALUES ("{0}", "{1}", "{2}", {3}, {4}, "{5}")'.format(*data)
        self.cursor.execute(command)
        self.mariadb_connection.commit()

    def log(self, ts, tool, msg):
        command = 'INSERT INTO ' + self.lt + '(ts, tool, message) VALUES ("'+ ts + '". "' + tool + '", "' + msg + '")')
	self.cursor.execute(command)
	self.mariadb_connection.commit()
