attendance = {
    "Monday": {"Amit", "Priya", "Rahul"},
    "Tuesday": {"Amit", "Priya", "Neha"},
    "Wednesday": {"Amit", "Priya", "Rahul"}
}

days = list(attendance.values())

all_students = set.union(*days)
every_day = set.intersection(*days)

print("Attended all classes:", every_day)

from collections import Counter
count = Counter()

for students in days:
    count.update(students)

print("Attended only once:", [s for s in count if count[s] == 1])
print("Total unique students:", len(all_students))