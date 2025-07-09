import time

for i in range (1,11):
    print("Perfrom 10 jumping jacks")
    time.sleep(20)
    
    completed = i*10
    
    if completed == 100:
        print("Congratulations! You completed all 100 Jumping Jacks!")

    user_in = input("Are you tired?(reply 'yes' or 'y'): ").lower().strip()

    if user_in == "yes" or user_in == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower().strip()
        if skip == "yes" or user_in == "y":
            print(f"You Completed a total of {completed} jumping jacks!")
            break
        else: 
            remaining = 100 - completed
            print(f"{remaining} jumping jacks remaining!")
    elif user_in == "no" or user_in == "n":
        remaining = 100 - completed
        print(f"You Completed a total of {completed} jumping jacks!")