


#VARIOUS WAYS OF IMPORTS

# from my_module import find_index
# from my_module import find_index as fi,test
# from my_module import find_index,test
# import my_module as mm


courses=["History","Physics","Computer","Math"]
import sys
import os
# print(os.__file__) : module ki location janne ke liye we can use __file__
# python kuch specific locations pe file ko search karta hai, aur woh saari locations
# ko hum sys.path list mei dekh sakte hai
print(sys.path)

# ['E:\\corey-python\\Import Modules and Exploring The Standard Library',
#  'C:\\Users\\par\\Documents\\python39.zip', 'C:\\Users\\par\\Documents\\DLLs', 
#  'C:\\Users\\par\\Documents\\lib', 'C:\\Users\\par\\Documents', 
#  'C:\\Users\\par\\Documents\\lib\\site-packages']


# if the module we are using is in some other location instead of CWD the we can append the
# location in sys.path and use the module present there

# sys.path.append('C:\\Users\\par\\Desktop\\my_module')

from my_module import *
index=find_index(courses,"Math")
print(test)
print(index)


