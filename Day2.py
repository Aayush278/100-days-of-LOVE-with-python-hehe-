print(len("Hello"))

#type error 

#Data types in python 
# string:- Anything enclosed in double quotes 

print("Hello"[-1]) #Indexing start from zero 
# i.e  - 01234 and from left this starts from -1

print("123"+"456")
print(123+456)

# Integer = 1234..... only the numbers 
#Float= 1.89 8.89 number with decimal values are float data type 
Pie=3.149
print(Pie)

# Boolean it's is either true or false 
# like in normal world we use 10,000,000 commas but in python we can use _ just for 
# our comfort computer sees it as normal number 

print(type("HEHE"))
print(type(1))
print(type(1.2))
print(type(False))


# type is a function like it's basically a machine that performs 
# performs a defined set or work 
# like aalu to chips making machine we dont care how it works it works and if we put rock instead of aalu then error
# as len(568) gives error 

# print(len(568))

# Type conversion and type casting 

print(int("123"))
print(bool("123"))
print(float(123))
print(type(str(123)))


print("Number of letter in your name " + str(len(input("Enter your name :\n")))) 
# if no str type conversion used here then it will give concatenation error
# as str cant be added with int 

# Mathematical operations 
print(123+45) # addn
print(3*2) # multn
print(3**2) # to the power 
print(5/3) # This gives float 
print(5//3) # this give int
print(7-3) # substraction 


# it uses bodmaslr or pemdaslr rule 

# bmi calculator 
weight=int(input("Enter your weight in kg\n"))
height=float(input("Enter your height in meter\n")) #because input returns str by default ans string cant math 
bmi=weight/height**2
x=round(bmi)
print("Your BMI is :",x)
is_healthy = True



# f-strings 
print(f"your weight is {weight} and your height is {height} and you are winning is {is_healthy}")