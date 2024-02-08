print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    
    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 60:
        print("Free entrance! ")
    else:
        bill = 12
        print("Adults tickets $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print (f"Your final bill if {bill}")
    
else:
    print("You can't ride the rollercoaster.")
    