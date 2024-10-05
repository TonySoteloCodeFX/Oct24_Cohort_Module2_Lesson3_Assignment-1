print("----------")
print("Task #1")

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
week_2 = temperatures[7:14]

print(week_2)

print("----------")
print("Task #2")

temps_over_100 = []

for temp in temperatures:
    if temp >= 100:
        temps_over_100.append(temp)

print(temps_over_100)