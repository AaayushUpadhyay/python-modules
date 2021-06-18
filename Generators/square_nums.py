# def square_numbers(nums):
# 	result = []
# 	for i in nums:
# 		result.append(i*i)
# 	return result

# my_nums = square_numbers([1,2,3,4,5])


# print(my_nums) #[1, 4, 9, 16, 25]

# Converting the above function into a generator

# def square_numbers(nums):
# 	for i in nums:
# 		yield(i*i)
# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums) #<generator object square_numbers at 0x000000CCE558EC80>
# # Generator ek ek karke values deta hai
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# # ek baar generator ne saari values de din toh next time value lane pe error dega
# print(next(my_nums)) #StopIteration

# Another method of making generator
my_nums=(i*i for i in [1,2,3,4,5] )
# print(my_nums)

# aise generator se values nikalne pe error nhi milega kyunki loop apne ap sahi jagah ruk jayega
# for num in my_nums:
# 	print(num)

# Converting generator into a list
# print(list(my_nums)) # this method takes a lot of memory hence not recommended

# We can return multiple things from a function using yield
def fun():
	yield 12
	yield 13
	yield 14
x=fun()
print(next(x))