# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# easy one 
password=""
for char in range(1, nr_letters + 1):
    idk=random.choice(letters)
    password+=idk
    
for raar in range(1, nr_symbols +1):
    ram=random.choice(symbols)
    password+=ram

for krr in range(1, nr_numbers + 1):
    rak=random.choice(numbers)
    password+=rak
print(f"Lere ye tera bread aur ye tera password {password}")






# normal one 
password=[]
for achar in range(1, nr_letters + 1):
    x=random.choice(letters)
    password.append(x)
for raar in range(1, nr_symbols +1):
    xy=random.choice(symbols)
    password.append(xy)
for krr in range(1, nr_numbers + 1):
    xyz=random.choice(numbers)
    password.append(xyz)
random.shuffle(password)
fppass=""
for e in password:
    fppass+=e
print(f"ye le le tera dudh nahi khana le password {fppass}")

