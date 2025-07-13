my_expense = {
    "Train":3900,
    "Cab":1200,
    "Hotel":1500,
    "Food":500,
    "Shopping":1700
}
partner_expense = {
    "Train":3900,
    "Cab":1400,
    "Hotel":1200,
    "Food":400,
    "Shopping":2500
}

sum = 0
sum2 = 0

for i in my_expense:
    sum = sum + my_expense[i]
    sum2 = sum2 + partner_expense[i]

print(f"My total expenses: {sum}")
print(f"Partners' total expenses: {sum2}")
if sum > sum2:
    print("Therefore, I spent more than my partner.")
else:
    print("Therefore, My partner spent more than I did.")

max_diff = 0
category_with_max_diff = ""

for category in my_expense:
    my_value = my_expense[category]
    partner_value = partner_expense[category]
    diff = abs(my_value - partner_value)
    
    if diff > max_diff:
        max_diff = diff
        category_with_max_diff = category

print(f"Category with highest difference: {category_with_max_diff}")
print(f"Difference in spending: {max_diff}")
