from contextlib import contextmanager

@contextmanager
def MyContextManager(filename,mode):
	try:
		file=open(filename,mode)
		yield file
	finally:
		file.close()
		# chahe error aye ya nhi humari file close ho jayes


with MyContextManager('sample1.txt','w') as f:
	f.write('Created this file using function based context manager')

print(f.closed)