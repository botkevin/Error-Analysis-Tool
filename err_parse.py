# see constructor for details of params needed.
# use the function run() to start the program.

class Err_parse:
    month_dict={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
    
    #interval is in seconds
    #@params directory filename to store the files in. The directory filename to open to find the data. The interval in seconds to poll the data.
    def __init__(self, port, open_filename, interval, msd, umsd, host, user, pswd, db, table, lt, log_dir):
        self.port = port
        self.inter = interval
        self.op_file = open_filename
        self.ptime = datetime.datetime.min
        self.mount_script_dir = msd
        self.umount_script_dir = umsd
        self.ld = log_dir
        try:
            self.maria = di.database_interface(host, user, pswd, db, table, lt, port)
        except NotImplementedError:
            self.write('sql login failed')
        self.log('Error tool start')

    def log(self, msg):
        self.maria.log(str(datetime.datetime.now()), self.port, msg)
        self.write(msg)

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
            month = int(Err_parse.month_dict[first[0]])
            day = int(first[1])
            year = datetime.date.today().year
            time = row[1].split(':')
            now_time = datetime.datetime(year, month, day, hour = int(time[0]), minute = int(time[1]))
            if self.ptime < now_time:
                return i
        # print("No new entries")
        return len(data)

    #writes log to csv
    def write(self, msg):
        with open(self.ld, 'a') as csvfile:
            csvfile.write(str(self.port + ', ' + datetime.datetime.now()) + ', ' + self.port + ', msg')

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
                self.update_p()
                start_index = self.start(data)
                data = data[start_index:]
                self.write_db(data)
                data = []
                time.sleep(self.inter)
        except KeyboardInterrupt:
            self.log('Closed Error Tool')
        except Exception as e:
            self.log(str(e) + ": " + str(traceback.extract_tb))
            raise e
            #self.log(str(e) + ": " + str(e.message))
