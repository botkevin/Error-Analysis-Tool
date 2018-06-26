import mysql.connector as mariadb

class database_interface:

    def __init__(self, u, pswd, db)
        self.mariadb_connection = mariadb.connect(user = u, password = pswd, database = db)
        self.cursor = mariadb_connection.cursor()

    def write(self, date, time, position, level, code, content)
        cursor.execute("INSERT INTO errorlog VALUES (%s,%s,%s,%s,%s,%s)", (date, time, position, level, code, content))
        mariadb_connection.commit()
