import csv
f = open('new_faculty.csv', 'rb')
list = csv.reader(f)
department = ['English']
for row in list:
    if row in department:
        print department
    else:
        print 'Nope'
