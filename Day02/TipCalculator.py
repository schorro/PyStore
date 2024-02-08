print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\n"))
percentage_bill = int(input("What percentage tip would you like to give: 10, 12 or 15%?\n"))
people_split_bill = int(input("How many people to split the bill?\n"))
percentage_bill_total = total_bill * (percentage_bill/100)
bill = (total_bill + percentage_bill_total)/people_split_bill

print(f"Each person should pay: $ {bill}")
