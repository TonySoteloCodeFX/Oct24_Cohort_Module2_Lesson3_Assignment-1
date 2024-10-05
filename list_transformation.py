print("----------")
print("Task #1")

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

print("----------")
print("Task #2")

average = sum(grades) // len(grades)
print(f"Average Score: {average}")