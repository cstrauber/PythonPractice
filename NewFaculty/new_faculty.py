import csv
f = open('new_faculty.csv', 'rb')
list = csv.reader(f)
departments = ['Classics', 'English', 'Philosophy', 'Religion']
i = 0
for row in list:
	for department in departments:
		if row in department:
			i += 1
print str(i) + 'New Faculty this year'
