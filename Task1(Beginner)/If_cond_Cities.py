Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai","Banglore", "Chennai", "Delhi"]

city_by_user = input("Enter a city name: ").title().strip()

for city in Australia:
    if city == city_by_user:
        print(f"{city} is in Australia")
for city in UAE:
    if city == city_by_user:
        print(f"{city} is in UAE")
for city in India:
    if city == city_by_user:
        print(f"{city} is in India")