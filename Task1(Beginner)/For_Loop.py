import random

six = 0
one = 0
consecutive_six = 0
prev_roll = None

for i in range (20):
    Die_rolled = random.choice([1,2,3,4,5,6])
    print(f"Result: {Die_rolled}")

    if Die_rolled == 6:
        six+=1
    if Die_rolled == 1:
        one+=1
    if Die_rolled == 6:
        if prev_roll == 6:
            consecutive_six+=1    
    prev_roll = Die_rolled

print(f"Total number of 6's: {six}")
print(f"Total number of 1's: {one}")
print(f"Total number of consecutive 6's: {consecutive_six}")