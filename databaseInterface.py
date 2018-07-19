import mysql.connector as mariadb
import datetime

class database_interface:

    month_dict={'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

    def __init__(self, h, u, pswd, db, t, lt):
        self.mariadb_connection = mariadb.connect(host = h, user = u, password = pswd, database = db)
        self.cursor = self.mariadb_connection.cursor()
        self.table = t
        self.lt = lt

    #self, date, time, position, level, code, content
    def write(self, data):
        last = data[0].split('.')
        month = Err_parse.month_dict[last[0]]
        day = last[1]
        time = data[1]
        year = str(datetime.date.today().year)
        ts = year + '-' + month + '-' + day + ' ' + time + ':00'
        command = 'INSERT INTO ' + self.table + '(ts, position, level, code, content) VALUES ("' + \
                  ts + '", "' + data[2] + '", "' + data[3] + '", "' + data[4] + '", "' + data[5] + '")'
        self.cursor.execute(command)
        self.mariadb_connection.commit()

    def log(self, ts, tool, msg):
        command = 'INSERT INTO ' + self.lt + '(ts, tool, message) VALUES ("'+ ts + '", "' + tool + '", "' + msg + '")'
        self.cursor.execute(command)
        self.mariadb_connection.commit()

    def get_start(self):
        rv = ''
        command = 'SELECT ts FROM ' + self.t + 'ORDER BY TS DESC LIMIT 1'
        self.cursor.execute(command)
        for ts in self.cursor:
            rv = ts
        return rv
        
