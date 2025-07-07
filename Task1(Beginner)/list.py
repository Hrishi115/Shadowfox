justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
length = len(justice_league)
justice_league.extend(["Batgirl", "Nightwing"])
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(justice_league)

justice_league.remove("Superman")
pos = justice_league.index("Aquaman")
justice_league.insert(pos + 1, "Superman")
print(justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league.sort()
print(justice_league)