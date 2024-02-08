print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice_one = input("Select between Right or Left.\n")

if choice_one == "Right":
    print("Game Over.")
elif choice_one == "Left":
    print("Swim or wait")
    choice_two = input("Select between Swim or Wait.\n")
    if choice_two  == "Swim":
        print("Game Over.")
    elif choice_two == "Wait":
        print("Which door you choose?")
        choice_three = input("Select between Red, Yellow or Blue.\n")
    if choice_three == "Red":
        print("Game Over.")
    elif choice_three == "Blue":
        print("Game Over.")
    else:
        print("You won.")