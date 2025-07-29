
#............. number matching or biggest number iputing game between system and user..............

import random as rm

while True:
    try:
        mychoice = int(input("Enter a number between 1 to 10: "))
        if not (1 <= mychoice <= 10):
            print("Please choose a number within the range!")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    computer_choice = rm.randint(1, 10)
    
    if mychoice > computer_choice:
        print("User chose a bigger number than computer.")
    elif mychoice < computer_choice:
        print("System chose a bigger number than user.")
    else:
        print("It's a tie! Play again.")
    
    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans == 'n':
        print("Thanks for playing!")
        break
