
# here we will compare memory usage of list and generator



import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.time()
# people = people_list(1000000)
# t2 = time.time()

t1 = time.time()
people = people_generator(1000000)
t2 = time.time()

# print ('Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()))
print ('Took {} Seconds'.format(t2-t1))