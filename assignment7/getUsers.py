


readfile = open('u.user', 'r')

for line in readfile:
	(id, age, gender, occupation, zipcode) = line.split('|')
	if age == '23' and gender == 'M' and occupation == 'student':
		print (id, age, gender, occupation, zipcode)