"""  Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

BMI Wikipedia Page
 """
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

H_size = (float(height) ** 2)
W_size = int(weight)

BMI = int(W_size/H_size)
print(BMI)