import csv


def read():
    with open('createcsv.csv','r') as rf:
        a = csv.reader(rf)

        for l in a:
            print(l)




'''def write():

    with open('mycsv.csv' , 'w') as f:
        a = csv.writer(f)
        a.writerow(['5', 'Rama', '1542'])
'''

def append():
    with open('createcsv.csv','a') as af:

        new_data = ['5','Rama','1852']
        append_data = csv.writer(af)
        append_data.writerow(new_data)





read()
append()
read()