# Decorators

def my_fun():
	print("We are inside my_fun\n")
	def my_fun1():
		print("We are inside my_fun1 "+'\n')
		def my_fun2():
			print("We are inside my_fun2 "+'\n')
		return my_fun2

	return my_fun1

x=my_fun
# print(x()()())

# Decorator is a function that takes another function as argument
# performs some tasks on it and returns another function

# simple example
# Example 1
# def fun1(x):
# 	x()
# 	print("in fun1")

# def hello():
# 	print("I am in hello")

# fun1(hello)


# Example 2
# def fun1(x):
# 	print("in fun 1")
# 	return x()
	

# def hello():
# 	print("I am in hello")

# hello=fun1(hello)

# hello


# # Example 3
# def fun1(x):
# 	print("in fun 1")
# 	return x()
	
# @fun1
# def hello():
# 	print("I am in hello")

# hello

# Another example
# <this entire thing is equal to>
# def decorator_function(fun):
# 	print("inside decorator_function\n")
# 	def wrapper_function():
# 		print("inside wrapper_function\n")
# 		return fun()
# 	return wrapper_function()


# def hello():
# 	print("I am in hello")
# hello=decorator_function(hello)
# <the code written below>

# @decorator_function
# def hello():
# 	print("I am in hello")
# hello=decorator_function(hello)





# def decorator_function(fun):
# 	print("inside decorator_function\n")
# 	def wrapper_function():
# 		print("inside wrapper_function\n")
# 		return fun()
# 	return wrapper_function


# @decorator_function
# def display():
# 	print("display function ran")

# display()


# @decorator_function
# def display_info(name,age):
# 	print("display function ran with arguments {} {}".format(name,age))


# display_info('Ayush','23')
#TypeError: wrapper_function() takes 0 positional arguments but 2 were given



# To remove above error
# def decorator_function(fun):
# 	print("inside decorator_function\n")
# 	def wrapper_function(*args,**kwargs):
# 		print("inside wrapper_function\n")
# 		return fun(*args,**kwargs)
# 	return wrapper_function


# @decorator_function
# def display():
# 	print("display function ran")

# display()


# @decorator_function
# def display_info(name,age):
# 	print("display function ran with arguments {} {}".format(name,age))


# display_info('Ayush','23')

