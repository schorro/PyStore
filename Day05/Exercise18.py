target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

#even = target%2
if target < 0 or target > 1000:
    print("You type a wrong number")
else:
    #for number in range(0, len(target)):
    #    target[n] = int(target[n])
    total = 0
    for number in range(2,target+1):
        if number % 2 == 0:
            total += number
print(total)
