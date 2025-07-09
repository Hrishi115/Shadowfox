import time

for i in range (1,11):
    print("Perfrom 10 jumping jacks")
    time.sleep(20)
    user_in = input("Are you tired?(reply 'yes' or 'y'): ").lower().strip()
    if user_in == "yes" or user_in == "y":
        user_in = input("Do you want to skip the remaining sets?: ").lower().strip()
        if user_in == "yes" or user_in == "y":
            print(f"You Completed a total of {10*i} jumping jacks!")
            break
        else: 
            continue
    else:
        continue
else:
    print("Congratulations! You completed all 100 Jumping Jacks!")