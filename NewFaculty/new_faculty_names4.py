#print to a file
import csv
f = open('new_faculty.csv', 'rb')
new_faculty_list = csv.reader(f)
departments = ['Classics', 'English', 'Philosophy', 'Religion']
for row in new_faculty_list:
	if row[2] in departments:
			return row[0] + ' ' + row[1] + ', ' + row[2]
f = open('output.txt', 'w')
f.write(whatever)
f.close
