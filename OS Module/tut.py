import os
# from datetime import datetime

# to know all the methods available in the module

# print(dir(os))

# ['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 
# 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL',
#  'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT',
# 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 
# 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__',
# '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list',
# '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir',
# 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding',
# 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe',
# 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode',
# 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 
# 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin',
# 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat',
# 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 
# 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace',
# 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 
# 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 
# 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd',
# 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 
# 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 
#  'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 
#  'waitstatus_to_exitcode', 'walk', 'write']


# To get to know your current working directory

# print(os.getcwd())

# E:\corey-python\OS Module

# To get to know all the files in the cwd

# print(os.listdir()) 
# listdir() displays all files and folders at a given location passed to it.
# by default the listdir() shows all the files,folders in the cwd

# To change your cwd
# os.chdir('E://corey-python//OS Module')
# print(os.getcwd())


# To create a new folder-->(folders are created,deleted,updated in the cwd)
# os.mkdir('New')

# mkdir can only create the top level folder , not sub folders
# To create subfolders we use
# os.makedirs('New2/sub1/sub2')



# To delete a folder
# os.rmdir('New')
# rmdir can only delete folders that are empty
# os.removedirs('New2/sub1/sub2')
# removedirs delete the entire folder along with its contents


# Renaming a file
# os.rename('tut.py','sample.py')

# to get info about a file
# print(os.stat('tut.py'))
# os.stat_result(st_mode=33206, st_ino=562949953497475, st_dev=1826526023, st_nlink=1, 
# st_uid=0, st_gid=0, st_size=3027, st_atime=1617420359, st_mtime=1617420422, st_ctime=1617420359)

# st_mtime--> last modification time : os.stat('tut.py').st_mtime

# To get timestamps in human readable format
# a=os.stat('tut.py').st_mtime
# print(datetime.fromtimestamp(a))
# 2021-04-03 09:07:55.703388



# st_size --> size of file in bytes : os.stat('tut.py').st_size

# os.walk('location')
# this function first goes inside the location
# and lists all the files/folders inside it
# then yeh ek ek karke saare folders mei jata hai aur unke andar 
# ke files/folders ko list karta hai
# returns a generator that generates a three item tuple (Current Path,Directories,Files)

# for dirpath,dirnames,filenames in os.walk('E://corey-python'):
# 	print('Current Path :', dirpath)
# 	print('Directories :',dirnames)
# 	print('Files :',filenames)
# 	print()


# Access home directory location by grabbing home environment variable
os.environ.get('HOME') # Returns a path
# To properly join two files together use os.path.join()
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# the benefit of os.path.join, is it takes the guess work out of inserting a slash


# os.path has other useful methods

os.path.basename
# This will grab filename of any path we are working on

os.path.dirname('/tmp/test.txt')
# returns the directory /tmp

os.path.split('/tmp/test.txt')
# returns both the directory and the file as a tuple

os.path.exists('/tmp/test.txt')
# returns a boolean

os.path.isdir('/tmp/test.txt')
# returns False

os.path.isfile('/tmp/test.txt')
# returns True

os.path.splitext('/tmp/test.txt')
# Splits file route of the path and the extension
# returns (‘/tmp/test’, ‘.txt’)
# This is alot easier than parsing out the extension. 
# Splitting off and taking the first value is much better.
# Very useful for file manipulation