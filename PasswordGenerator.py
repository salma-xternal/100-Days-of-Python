import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nrl = int(input("How many letters would you like in your password?\n"))
nrs = int(input(f"How many symbols would you like?\n"))
nrn = int(input(f"How many numbers would you like?\n"))


password_list = []
for x in range(0, nrl):
    password_list += random.choice(letters)
for g in range(0, nrs):
    password_list += random.choice(symbols)
for b in range(0, nrn):
    password_list += random.choice(numbers)
random.shuffle(password_list)


password = ""
for k in password_list:
    password += k

print(f"Generated Password: {password}")
