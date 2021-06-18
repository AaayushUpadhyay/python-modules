# Decorator with arguments

def fun(arguments):
	def decorator_function(fun):
		print(arguments +": inside decorator_function\n")
		def wrapper_function():
			print(arguments +": inside wrapper_function\n")
			return fun()
		return wrapper_function
	return decorator_function


@fun("Hello")
def display():
	print("display function ran")

display()
