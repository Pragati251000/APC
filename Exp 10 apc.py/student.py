
# f = open("student.txt", "w")
# f.write("Name: Amit\n")
# f.write("Roll No: 101\n")
# f.write("Branch: Computer Engineering\n")
# f.write("Semester: 5")
# f.close()

# print("File created successfully")




# f = open("student.txt", "r")
# print(f.read())
# f.close()



# f = open("student.txt", "a")
# f.write("\nCollege: DYP")
# f.close()

# print("Information appended")



# f = open("student.txt", "r")

# for line in f:
#     print(line, end="")

# f.close()



# f = open("student.txt", "r")
# lines = f.readlines()
# print("Total lines:", len(lines))
# f.close()




# f = open("student.txt", "r")
# text = f.read()
# print("Total words:", len(text.split()))
# f.close()



# f = open("student.txt", "r")
# text = f.read()
# print("Total characters:", len(text))
# f.close()



# f = open("student.txt", "r")
# lines = f.readlines()

# for line in reversed(lines):
#     print(line, end="")

# f.close()




# f = open("student.txt", "r")
# text = f.read().lower()
# vowels = 0
# consonants = 0

# for ch in text:
#     if ch.isalpha():
#         if ch in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# f.close()




# f = open("student.txt", "r")
# text = f.read()

# a = d = s = sp = 0

# for ch in text:
#     if ch.isalpha():
#         a += 1
#     elif ch.isdigit():
#         d += 1
#     elif ch == " ":
#         s += 1
#     else:
#         sp += 1

# print("Alphabets:", a)
# print("Digits:", d)
# print("Spaces:", s)
# print("Special characters:", sp)
# f.close()




# f = open("student.txt", "r")
# words = f.read().split()
# longest = max(words, key=len)

# print("Longest word:", longest)
# f.close()




# f = open("student.txt", "r")
# words = f.read().lower().split()
# d = {}

# for word in words:
#     d[word] = d.get(word, 0) + 1

# print(d)
# f.close()





# word = input("Enter word: ").lower()
# f = open("student.txt", "r")
# count = 0

# for i, line in enumerate(f, 1):
#     words = line.lower().split()
#     n = words.count(word)

#     if n > 0:
#         print("Line number:", i)
#         count += n

# print("Occurrences:", count)
# f.close()




# old = input("Enter word to replace: ")
# new = input("Enter new word: ")

# f = open("student.txt", "r")
# text = f.read()
# f.close()

# text = text.replace(old, new)

# f = open("student.txt", "w")
# f.write(text)
# f.close()

# print("Word replaced")





# f = open("program.py", "r")
# lines = f.readlines()
# f.close()

# f = open("without_comments.py", "w")

# for line in lines:
#     if not line.lstrip().startswith("#"):
#         f.write(line)

# f.close()
# print("Comments removed")





# f = open("student.txt", "r")
# text = f.read()
# f.close()

# f = open("uppercase.txt", "w")
# f.write(text.upper())
# f.close()

# print("Uppercase file created")




# f = open("students.csv", "w")
# f.write("RollNo,Name,Marks\n")
# f.write("101,Amit,85\n")
# f.write("102,Priya,92\n")
# f.write("103,Rahul,78\n")
# f.close()

# f = open("students.csv", "r")
# lines = f.readlines()[1:]
# students = []

# for line in lines:
#     roll, name, marks = line.strip().split(",")
#     students.append((roll, name, int(marks)))

# for s in students:
#     print(s)

# top = max(students, key=lambda x: x[2])
# print("Highest:", top[1], top[2])
# print("Average:", sum(s[2] for s in students) / len(students))

# for s in students:
#     if s[2] > 80:
#         print("Above 80:", s[1])

# f.close()




# def display():
#     f = open("employee.txt", "r")
#     employees = []

#     for line in f:
#         i, n, d, s = line.strip().split(",")
#         employees.append((i, n, d, float(s)))

#     f.close()
#     for e in employees:
#         print(e)
#     return employees

# def highest():
#     e = display()
#     print("Highest paid:", max(e, key=lambda x: x[3]))

# def average():
#     e = display()
#     print("Average salary:", sum(x[3] for x in e) / len(e))

# def above_salary(amount):
#     e = display()
#     for x in e:
#         if x[3] > amount:
#             print(x)

# f = open("employee.txt", "w")
# f.write("1,Amit,IT,50000\n")
# f.write("2,Priya,HR,60000\n")
# f.write("3,Rahul,Sales,40000\n")
# f.close()

# display()
# highest()
# average()
# above_salary(45000)





