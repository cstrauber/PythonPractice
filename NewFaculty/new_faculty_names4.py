#print to a file

def my_new_faculty_list():
    import csv
    f = open('NewFaculty/new_faculty.csv', 'rb')
    new_faculty_list = csv.reader(f)
    departments = ['Classics', 'English', 'Philosophy', 'Religion']
    for row in new_faculty_list:
	    if row[2] in departments:
		    print row[0] + ' ' + row[1] + ', ' + row[2]
x = open('NewFaculty/mynewfaculty.txt', 'a')
myString = str(x)
x.write(myString)
x.close

