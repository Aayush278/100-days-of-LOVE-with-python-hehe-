import random
word_list=["aayush","itishree","ramu","rancho","dragon"]
choosen_word=random.choice(word_list)



placeholder=""
for dog in range(len(choosen_word)):
    placeholder+="_ "
print(choosen_word)
print(placeholder)
guess=input("guess a letter:\n").lower()


display=""
for letter in choosen_word:
    if letter == guess:
        display+= letter
    else:
        display+="_ "

print(display)

