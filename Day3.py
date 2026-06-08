# Conditional statements if/else 
# if condn:
#  do this 
# else:
#  do this 

water_level= int(input("What is the water level:\n"))
if water_level >=120:
    print("Stop filling")
else:
    print("Continue filling")
    
# comparison operator 
# == equal to >= greater than equal to 
# Water slide ticker booking 
# modulo operator 
# % it gives remaineder 

# check if a number is even or odd 
number=int(input("Enter the number :\n"))
if number==0:
    print("ZERO")
elif number%2==0:
    print("EVEN")
else:
    print("ODD")


# Water park ticket booking (shall also ask for age and picture needed or not and price accordingly)
print("Hello welcome to Lassan waterpark")
age=int(input("Enter your age:\n"))
height=float(input("Enter your height in meters:\n"))
pic=input("Do you want a picture Y or N")
if age>=18 and height>=1.7 and pic=="Y":
    print("Please pay 15$")
elif age<18 and height>=1.7 and pic=="Y":
    print("Please pay 12$")
elif age>=18 and height>=1.7 and pic=="N":
    print("Please pay 10$")
elif age<18 and height>=1.7 and pic=="N":
    print("Please pay 7$")
elif age>45 and age<65:
    print("You can get free ride")
else:
    print("Not eligible for waterpark entry G mara ")
    

# Pizza delivery app
print("Welcome to lassan pizza")
price=0
size=input("Enter the size S,M or L\n")
cheese=input("want cheese Y or N\n")
lassan=input("Want lassan Y or N\n")
if size=="S":
    price+=100
elif size=="M":
    price+=200
elif size=="L":
    price+=300

if cheese=="Y":
    price+=50

if lassan=="Y":
    price+=10
print(f"Final price for your pizza is {price} you selected {size} size and additional cheese {cheese} and additional lassan {lassan} ")

# logical operator 
# and , or , not