import csv
f = open('new_faculty.csv', 'rb')
listicle = csv.reader(f)
departments = ['Classics', 'English', 'Philosophy', 'Religion']
i = 0
for row in listicle:
	for department in departments:
		if department in row:
			i += 1
print str(i) + ' New Faculty this year'
