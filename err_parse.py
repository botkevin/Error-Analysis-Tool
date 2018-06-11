import csv

month_dict={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
p_month = 0
p_day = 0
p_time = 0

def load(file_name):
    data = []
    with open(file_name) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data = list(data)
    data = data[2:]
    return data

#destructive
def merge_content(data):
    for row in data:
        row[5] = row[5].strip()
        if row[1] != '':
            master = row
        else:
            master[5] += ' ' + row[5]
    #get rid of excess
    rv = []
    for row in data:
        if row[1] != '':
            rv.append(row)
    p_row = rv[99]
    first = p_row[1].split('.')
    p_month = month_dict[first[1]]
    p_day = int(first[2])
    p_time = int(re.sub(':', '', p_row[2])
    return rv

#returns index to start
def start(data):
    for i in range(len(data)):
        row = data[i]
        first = row[1].split('.')
        month = month_dict[first[1]]
        day = int(first[2])
        time = int(re.sub(':', '', row[2]))
        if p_month < month or p_day < day or p_time < time:
            return i
    print("No new errors")
    return 100
