# Write a separate program to accomplish each of these exercises. Save each pro-
# gram with a filename that follows standard Python conventions, using lowercase
# letters and underscores, such as simple_message.py and simple_messages.py.
# 2-1. Simple Message: Assign a message to a variable, and then print that
# message.
# 2-2. Simple Messages: Assign a message to a variable, and print that message.
# Then change the value of the variable to a new message, and print the new
# message.

secret="I finally shared my secret with someone"
print(secret)
secret="Feels so free"
print(secret.title())
# this title makes every first character capital 
name = "Ada Lovelace         "
print(len(name))
print(name.upper())
print(name.lower())

# upper converts all to upercase and lower converts all to lower case 
# concatenation
first_name = "ada\n"
last_name = "\tkhan"
full_name = f"{first_name} {last_name}" #we used f strings here 
print(full_name)





# try using r stripp
# Removing Prefixes 
# nostarch_url = 'https://thesemicolon.online'
# nostarch_url.removeprefix('https://')
# print(nostarch_url)         debug this shit 



# multiple assisgnments
x,y,z=(1,2,3)
print(x)
print(y)


# Constants
# A constant is a variable whose value stays the same throughout the life of a
# program. Python doesn’t have built-in constant types, but Python program-
# mers use all capital letters to indicate a variable should be treated as a con-
# stant and never be changed:
# MAX_CONNECTIONS = 5000
# When you want to treat a variable as a constant in your code, write the
# name of the variable in all capital letters.
import this
