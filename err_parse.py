import csv

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
    return rv
