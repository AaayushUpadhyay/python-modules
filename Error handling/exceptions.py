# 4 blocks of exception handling in python,
# jis part of code mei error ane ke chances ho woh try mei hoga


# apna khud ka exception banane ke liye we will create a class which inherits from the Exception class
# Aur hume Exception class ke constructor ko override karna padega 
class ValueTooSmallException(Exception):
    def __init__(self,message):
        super().__init__(message)



try:
  a=int(input("Enter value of a\n"))
  b=int(input("Enter value of b\n"))
  if a<100 or b<100:
      raise ValueTooSmallException("Use dimaag for low level calculations")
  c=a/b
	
# error ane ke baad uski handling except block mei hogi
# except Exception har ek error ko handle karega
# except Exception as e:
# 	# print("Value sahi dalo") #ya toh hum apna custom message display kar sakte ya phir 
#     print(e) # ya phir python ka error mssg display kar sakte


# agar hum kuch particular exceptions ko handle karna chahte hai tbb 

# apna khud ka exception
except ValueTooSmallException as e:
    print(e)


except ZeroDivisionError as e:
    print("Denominator cannot be zero")
except ValueError:
    print("Enter valid integers only")

# Agar koi error nhi ayi tbb else block chalega
else:
	print(c)

# Koi error aye ya nhi finally  chalega
finally:
	print("mujhe ghanta fark nhi padta")



