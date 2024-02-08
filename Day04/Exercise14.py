names = names_string.split(", ") # This part cause bug in visual code because I don't know what is behind of it
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

names_items = len(names) #This will bring the lenght of the list from the variable names

random_choice = random.randint(0, names_items -1) #
print(names[random_choice]+" is going to buy the meal today!")
