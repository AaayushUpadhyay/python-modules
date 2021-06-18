import os
os.chdir('E:/corey-python/Automate Parsing and Renaming of Multiple Files/files')
for f in os.listdir():
	f_course,f_ext=os.path.splitext(f)
	f_name=f_course.split('-')[0]
	f_num=f_course.split('-')[1]
	new_name="{}-{}.txt".format(f_num[1],f_name)
	os.rename(f,new_name)