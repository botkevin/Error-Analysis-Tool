import csv
import re
from pathlib import Path
import time

class err_parser:
    month_dict={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    
    #interval is in seconds
    def __init__(self, store_dir, open_dir, interval):
        self.sto_dir = store_dir
        self.inter = interval
        self.op_dir = open_dir
        self.p_month = 0
        self.p_day = 0
        self.p_time = 0

    def load(self, file_name):
        data = []
        with open(file_name) as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            data = list(data)
        data = data[2:]
        return data
    
    #destructive
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
    
    #returns index to start
    def start(self, data):
        for i in range(len(data)):
            row = data[i]
            first = row[0].split('.')
            month = err_parser.month_dict[first[0]]
            day = int(first[1])
            time = int(re.sub(':', '', row[1]))
            if self.p_month < month and self.p_day < day and self.p_time < time:
                return i
        print("No new entries")
        return 100

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

    #stores latest 100 lines of data
    def cache(self, data):
        self.write(data, 'cache.csv', 'w')

    def update_p(self, data):
        p_row = data[99]
        last = p_row[0].split('.')
        self.p_month = err_parser.month_dict[last[0]]
        self.p_day = int(last[1])
        self.p_time = int(re.sub(':', '', p_row[1]))


    def run(self):
        while True:
            data = self.load(self.op_dir)
            data = self.merge_content(data)
            self.cache(data)
            start_index = self.start(data)
            self.update_p(data)
            data = data[start_index:]
            self.write(data, self.sto_dir, 'a')
            data = []
            time.sleep(self.inter)
