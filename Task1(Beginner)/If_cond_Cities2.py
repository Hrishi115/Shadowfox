Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai","Bangalore", "Chennai", "Delhi"]

city1 = input("Enter first city name: ").title().strip()
city2 = input("Enter second city name: ").title().strip()

if city1 in Australia and city2 in Australia:
    print(f"{city1} and {city2} are present in Australia")
elif city1 in UAE and city2 in UAE:
    print(f"{city1} and {city2} are present in UAE")
elif city1 in India and city2 in India:
    print(f"{city1} and {city2} are present in India")
else:
    print("They don't belong to the same country")