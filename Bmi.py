weight = int(input("Enter your weight \n"))
height =float(input("enter your height\n"))


bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi<18.5:
 print("underweight")
elif bmi>=18.5 and bmi<25:
 print("normal")
else:
 print("overweight")
    