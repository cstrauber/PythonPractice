#print a list of names in my departments
import csv
f = open('new_faculty.csv', 'rb')
listicle = csv.reader(f)
departments = ['Classics', 'English', 'Philosophy', 'Religion']
for row in listicle:
	for department in departments:
		if department in row:
			print row[0] + ' ' + row[1] + ', ' + row[2]

