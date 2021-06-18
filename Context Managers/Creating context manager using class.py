class MyContextManager:
	def __init__(self,filename,mode):
		self.filename=filename
		self.mode=mode
	def __enter__(self):
		self.file=open(self.filename,self.mode)
		return self.file
	def __exit__(self,exc_type,exc_val,traceback):
		self.file.close()


with  MyContextManager('sample.txt','w') as f:
	f.write('Created this file using my own class based context manager')

# with MyContextManager('sample.txt','w') yeh constructor ko run karega aur fir enter ko
# enter se jo file object return hoga woh f mei jata hai

print(f.closed)