from string import ascii_letters, digits
from random import choice, randint
from os import path


while True:
    try:
        passwd_len = int(input("how much characters do u want? "))
        break
    except ValueError:
        print("Enter a number!")
numbers = []
chars = list(ascii_letters) + list(digits)
passwd = []

for i in range(9):
    numbers.append(randint(0,9))

for i in range(passwd_len):
    passwd.append(choice(chars))


if not path.isfile("passwd.txt"):
    with open("passwd.txt", 'a') as f:
        f.write("".join(passwd))
else:
    with open("passwd.txt", "w") as f:
        f.write("".join(passwd))

print("".join(passwd))
print("Saved to file also!")
input()
