names = ["Amit", "Priya", "Rahul"]
grades = [80, 90, 75]

names.append("Neha")
grades.append(85)

grades[0] = 88

print("Students:", names)
print("Grades:", grades)
print("Average:", sum(grades) / len(grades))
print("Highest:", max(grades))
print("Lowest:", min(grades))

names.remove("Rahul")
grades.pop(2)

print("Updated students:", names)
print("Updated grades:", grades)