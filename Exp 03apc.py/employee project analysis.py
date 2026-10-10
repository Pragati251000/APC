project1 = {"Amit", "Priya", "Rahul"}
project2 = {"Priya", "Neha", "Rahul"}

print("Both projects:", project1 & project2)
print("Only project 1:", project1 - project2)
print("Only project 2:", project2 - project1)
print("All employees:", project1 | project2)