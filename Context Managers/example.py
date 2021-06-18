import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
	try:
		cwd=os.getcwd()
		os.chdir(destination)
		yield

	finally:
		os.chdir(cwd)


print(os.getcwd())
with change_dir('Sample-Dir-One'):
	print(os.listdir())
print(os.getcwd())

print(os.getcwd())
with change_dir('Sample-Dir-Two'):
	print(os.listdir())
print(os.getcwd())
