# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
year_leap_first_condition = year % 4
year_leap_second_condition = year % 100
year_leap_third_condition = year % 400

if year_leap_first_condition == 0 and year_leap_second_condition > 0:
    print("Leap year")
elif year_leap_second_condition == 0 and year_leap_third_condition > 0:
    print("Not leap year")
else:
    print("Not leap year")