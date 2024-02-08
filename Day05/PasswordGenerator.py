#Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

print("Password Gen")
#number_strings = int(input("How many count of strings do you want in your pass?\n"))
number_letters= int(input("How many letters would you like in your pass?\n")) 
number_symbols = int(input(f"How many symbols do you want\n"))
number_numbers = int(input(f"How many numbers do you want?\n"))

for l in range(number_letters):
    letter = random.choice(letters)
    print(letter[l])
for s in range(number_symbols):
    symbol = random.choice(symbols)
    print(symbol)
for n in range(number_numbers):
    number = random.choice(numbers)
    print(number)