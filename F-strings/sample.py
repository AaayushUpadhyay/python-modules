first_name='Ayush'
last_name='Upadhyay'

# Printing a sentence using format
sentence="My name is {} {}".format(first_name,last_name)
# print("Using .format : "+sentence)

# F-strings are great alternative to format
# print(f'My name is {first_name} {last_name}')

# We can run functions inside these curly braces
# print(f'My name is {first_name.upper()} {last_name.upper()}')

# With dictionary
d={'name':'Ayush Upadhyay','age':22}
# print(f'My name is {d["name"]} and age is {d["age"]}')

# Calculations can also be performed 
# print(f'4 times 11 is {11*4}')

# writing 0 padded values
# for i in range(1,11):
    # print(f'the value is {i:02}')


# Formatting float data
pi=3.14159265
# print(f'The value of pi is {pi:.4f}') #rounding off to 4 decimal places

# working with dates
from datetime import datetime
date=datetime(2021,4,13)
print(f'My birthday is on {date:%B %dth, %Y}')