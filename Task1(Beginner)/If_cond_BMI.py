# BMI Calculator

height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kgs): "))
bmi = weight / (height**2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else: 
    print("Underweight")
