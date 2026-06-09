x=["rock","scissors","paper"]
import random
x=random.choice(x)
print('''       _------.
      /  ,     \_
    /   /  /{}\ |o\_
   /    \  `--' /-' \
  |      \      \    |
 |              |`-, |
 /              /__/)/
|              |''')
print("Welcome to game hehe")
user=input("rock paper or scissors :\n").lower()
if user==x:
    print("draw")
elif x=="rock" and user=="scissors":
    print("Computer won")
elif x=="paper" and user=="rock":
    print("computer won")
elif x=="scissors" and user=="paper":
    print("computer won")
elif user=="rock" and x=="scissors":
    print("user won")
elif user=="paper" and x=="rock":
    print("user won")
elif user=="scissors" and x=="paper":
    print("user won")
else:
    print("G Mara")
