print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
join_names = name1.lower()+name2.lower()

count_t = join_names.count('t')
count_r = join_names.count('r')
count_u = join_names.count('u')
count_e = join_names.count('e')
total_true = count_t+count_r+count_u+count_e

count_l = join_names.count('l')
count_o = join_names.count('o')
count_v = join_names.count('v')
count_ee = join_names.count('e')
total_love = count_l+count_o+count_v+count_ee

total_total = str(total_true) + str(total_love)
if  int(total_total) < 10 or int(total_total) > 90:
    print(f"Your score is {total_total}, you go together like coke and mentos.")
elif int(total_total) >= 40 and int(total_total) <= 50:
    print(f"Your score is {total_total}, you are alright together.")
else:
    print(f"Your score is {total_total}.")