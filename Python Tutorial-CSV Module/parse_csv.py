# CSV - Comma Separated Values

import csv
# Reading a csv file
# with open('names.csv','r') as csv_file:
# 	csv_reader=csv.reader(csv_file)
# 	# .read() return a generator so we have to loop over it
# 	for line in csv_reader:
# 		print(line)

# OUTPUT
# ['first_name', 'last_name', 'email']
# ['John', 'Doe', 'john-doe@bogusemail.com']
# ['Mary', 'Smith-Robinson', 'maryjacobs@bogusemail.com']
# ['Dave', 'Smith', 'davesmith@bogusemail.com']
# ['Jane', 'Stuart', 'janestuart@bogusemail.com']...

# IF WE DONT WANT THE FIRST LINE THEN

# with open('names.csv','r') as csv_file:
# 	csv_reader=csv.reader(csv_file)
# 	next(csv_reader)
# 	# .read() return a generator so we have to loop over it
# 	for line in csv_reader:
# 		print(line)

# OUTPUT
# ['John', 'Doe', 'john-doe@bogusemail.com']
# ['Mary', 'Smith-Robinson', 'maryjacobs@bogusemail.com']
# ['Dave', 'Smith', 'davesmith@bogusemail.com']
# ['Jane', 'Stuart', 'janestuart@bogusemail.com']
# ['Tom', 'Wright', 'tomwright@bogusemail.com']
# ['Steve', 'Robinson', 'steverobinson@bogusemail.com']...

# IF WE WANT ONLY THE EMAILS OR FIRST NAMES OR LAST NAMES
# with open('names.csv','r') as csv_file:
# 	csv_reader=csv.reader(csv_file)
# 	next(csv_reader)
# 	# .read() return a generator so we have to loop over it
# 	for line in csv_reader:
# 		# print(line[0]) # ONLY FIRST NAMES
# 		# print(line[1]) # ONLY LAST NAMES
# 		# print(line[2]) # ONLY EMAILS



# WRITING A CSV FILE
# # writing data in csv file with '-' as delimiter

# with open('names.csv','r') as csv_file:
# 	csv_reader=csv.reader(csv_file)
# 	with open('new_file.csv','w') as new_file:
# 		csv_writer=csv.writer(new_file,delimiter='-')

# 		for line in csv_reader:
# 			csv_writer.writerow(line)


# writing data in csv file with '\t(tab space)' as delimiter

# with open('names.csv','r') as csv_file:
# 	csv_reader=csv.reader(csv_file)
# 	with open('new_file.csv','w') as new_file:
# 		csv_writer=csv.writer(new_file,delimiter='\t')

# 		for line in csv_reader:
# 			csv_writer.writerow(line)

# Reading data from a file with a different delimiter

# with open('names.csv','r') as csv_file:
# 	csv_reader=csv.reader(csv_file,delimiter='@')
# 	for line in csv_reader:
# 		print(line)
# output
# ['first_name,last_name,email']
# ['John,Doe,john-doe', 'bogusemail.com']
# ['Mary,Smith-Robinson,maryjacobs', 'bogusemail.com']
# ['Dave,Smith,davesmith', 'bogusemail.com']
# ['Jane,Stuart,janestuart', 'bogusemail.com']


# Using dictionary readers and writers

# reading a csv file using dictionary readers
# with open('names.csv','r') as csv_file:
# 	csv_reader=csv.DictReader(csv_file) #header values become keys
# 	for line in csv_reader:
# 		print(line)
# 		# if we just want emails
# 		# print(line['email'])


# writing a csv file using dictionary writers

with open('names.csv','r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	with open('new_file.csv','w') as new_file:
		# fieldnames = ['first_name','last_name','email']

		# if we dont want emails in our new file
		fieldnames = ['first_name','last_name']
		csv_writer=csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')

		# if we want header values to be displayed then
		csv_writer.writeheader()

		for line in csv_reader:
			del line['email'] # if we dont want emails in our new file
			csv_writer.writerow(line)
