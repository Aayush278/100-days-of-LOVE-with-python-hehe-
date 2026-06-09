#Today is day 4 actually day 6 
# randomisation and python lists
import random
x=random.randint( 1, 10)
print(x)
if x==7:
    print("You won")
else:
    print("G MARA")


y=random.random()
print(y*10)

z=random.uniform(1,10)
print(z)

# tails or heads 
gh=random.randint(1,2)
if gh==1:
    print("HEADS")
else:
    print("tails")

# lists
fruit=["cherry","banana","apple"]
print(fruit[1])
fruit[1]="minion"
fruit.append("Aayush")
print(fruit)
fruit.extend(["rutti","Gua","hehe"])
print(fruit)


# code for bill pay heheh
friends=["aayush","Itishree","raman","maggie"]
ji=random.randint(0,3)
print(friends[ji])
print(random.choice(friends))

