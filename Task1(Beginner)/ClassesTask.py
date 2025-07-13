class Avenger:
    def __init__(self, super_hero_name, name, age, gender, super_power, weapon):
        self.super_hero_name = super_hero_name
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def getinfo(self):
        print(f"\nAvenger: {self.super_hero_name}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon: {self.weapon}")

    def is_leader(self):
        if self.super_hero_name == "Captain America":
            print(f"\n{self.super_hero_name} is the leader of Avengers!")
        else:
            print(f"\n{self.super_hero_name} is not the leader of Avengers!")

super_heroes = [
    ("Captain America", "Steve Rogers", 150, "Male", "Super Strength", "Shield"),
    ("Iron Man", "Tony Stark", 35, "Male", "Technology", "Armour"),
    ("Black Widow", "Natasha Romanoff", 30, "Female", "Superhuman", "Batons"),
    ("Hulk", "Bruce Banner", 32, "Male", "Unlimited Strength", "No Weapon"),
    ("Thor", "Thor Odinson", 150, "Male", "Super Energy", "Mjolnir"),
    ("Hawkeye", "Clint Barton", 31, "Male", "Fighting Skills", "Bow and Arrows")
]

avengers = [Avenger(*hero) for hero in super_heroes]

for avenger in avengers:
    avenger.getinfo()
    avenger.is_leader()