import csv
import re
from pathlib import Path
import time
import databaseInterface as di
import subprocess
import datetime

# A data collection tool to analyze error history csv files to combine them into one document and update it continuously
# see constructor for details of params needed.
# use the function run() to start the program.

class Err_parse:
    month_dict={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    
    #interval is in seconds
    #@params directory filename to store the files in. The directory filename to open to find the data. The interval in seconds to poll the data.
    def __init__(self, port, open_filename, interval, msd, umsd, host, user, pswd, db, table, lt):
        self.port = port
        self.inter = interval
        self.op_file = open_filename
        self.ptime = datetime.min
        self.mount_script_dir = msd
        self.umount_script_dir = umsd
        self.maria = di.database_interface(host, user, pswd, db, table, lt)
        self.log('Error tool start')

    def log(self, msg):
        self.maria.log(str(datetime.datetime.now()), self.port, msg)

    #load the data
    def load(self):
        subprocess.call(["bash", self.mount_script_dir, self.port])
        data = []
        try:
            with open('/media/'+self.port+'/'+self.op_file) as csvfile:
                data = csv.reader(csvfile, delimiter=',')
                data = list(data)
                data = data[2:]
            subprocess.call(["sh", self.umount_script_dir, self.port])
        except FileNotFoundError:
            data = []
        return data
    
    #destructivly merges the content row of the log so that the contents are all in one line.
    def merge_content(self, data):
        for row in data:
            row[5] = row[5].strip()
            if row[0] != '':
                master = row
            else:
                master[5] += ' ' + row[5]
        #get rid of excess
        rv = []
        for row in data:
            if row[0] != '':
                rv.append(row)
        return rv
    
    #returns index to start getting new data
    def start(self, data):
        for i in range(len(data)):
            row = data[i]
            first = row[0].split('.')
            month = Err_parse.month_dict[first[0]]
            day = int(first[1])
            year = datetime.date.today().year
            time = row[1].split(':')
            now_time = datetime.datetime(year, month, day, hour = time[0], minute = time[1])
            if self.ptime < now_time:
                return i
        # print("No new entries")
        return len(data)

    #deprecated
    #writes data to csv
    def write(self, data, loc_name, option):
        f = None
        my_file = Path(loc_name)
        if my_file.is_file():
            f = open(loc_name, option)
        else:
            f = open(loc_name, 'w')
            f.write('Error History\n')
            f.write('Date, Time, Position, Level, Code, Content\n')
        for row in data:
            msg = row[0] + ', ' + row[1] + ', ' + row[2] + ', ' + row[3] + ', ' + row[4] + ', ' + row[5] + '\n'
            f.write(msg)
        f.close()

    def write_db(self, data):
        for row in data:
            self.maria.write(row)

    #stores latest 100 lines of data
    def cache(self, data):
        self.write(data, 'cache.csv', 'w')

    #udates the latest time that was read
    def update_p(self):
        date = self.maria.get_start()
        if date:
            self.ptime = date
            # print('month: ' + str(self.p_month) + ', day: '+ str(self.p_day) + ', time: '+ str(self.p_time))

    #runs all of the above functions. Run this to start the program.
    def run(self):
        try:
            while True:
                data = self.load()
                data = self.merge_content(data)
                self.cache(data)
                start_index = self.start(data)
                self.update_p(data)
                data = data[start_index:]
                self.write_db(data)
                data = []
                time.sleep(self.inter)
        except KeyboardInterrupt:
            self.log('Closed Error Tool')
        except Exception as e:
            self.log(str(e) + ": " + str(e.message))
