numbers = []

for i in range(1, 101):
    if i % 2 == 0:
        numbers.append(i)
    else:
        numbers.append(i - 1)

print(numbers)