import err_parse as e
import csv

data = e.load('ERRHIST.csv')
def test_load():
    print('load')
    for i in range(5):
        print(data[i])
        print('')

#test merger
merge = []
def test_merge():
    global merge
    print('merge')
    merge = e.merge_content(data)
    for i in range(5):
        print(merge[i])

test_load()
test_merge()
