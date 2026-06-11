# Loops 
# for loop 
fruits=["apple","mango","strawberry"]
for fruit in fruits:
    print(fruit)
    print(fruit+"Pie")


student_scores=[120,130,99,87,78,67,140,98]
print(sum(student_scores))
sum=0
for score in student_scores:
    sum+=score
print(sum)

print(max(student_scores))

maxi=0
for i in student_scores:
    if i>maxi:
        maxi=i
print(maxi)

# range function 
# for number in range(a,b):
#     print(number)

for number in range(1,10,2):
    print(number)

plus=0
for x in range(1,101):
    plus+=x
print(plus)
