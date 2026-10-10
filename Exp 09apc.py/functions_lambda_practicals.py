
# import math

# # 1. Factorial
# def factorial(n):
#     if n < 0:
#         return None
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # 2. Even or Odd
# def check_even_odd(n):
#     return "Even" if n % 2 == 0 else "Odd"

# # 3. Greater of Two Numbers
# def greater(a, b):
#     return a if a > b else b

# # 4. Simple Interest
# def simple_interest(p, r, t):
#     return p * r * t / 100

# # 5. Prime Number
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # 6. Area of Circle
# def circle_area(r):
#     return math.pi * r * r

# # 7. Sum of First n Natural Numbers
# def natural_sum(n):
#     return n * (n + 1) // 2

# # 8. Power
# def power(base, exponent):
#     return base ** exponent

# # 9. Largest Element Without max()
# def largest(lst):
#     if not lst:
#         return None
#     result = lst[0]
#     for n in lst:
#         if n > result:
#             result = n
#     return result

# # 10. Count Vowels
# def count_vowels(s):
#     return sum(1 for ch in s.lower() if ch in "aeiou")

# # 11. Reverse String
# def reverse_string(s):
#     return s[::-1]

# # 12. Palindrome String or Number
# def is_palindrome(value):
#     s = str(value)
#     return s == s[::-1]

# # 13. Average of List
# def average(lst):
#     return sum(lst) / len(lst) if lst else 0

# # 14. Count Occurrences
# def count_occurrences(lst, element):
#     return lst.count(element)

# # 15. Unique Elements
# def unique_elements(lst):
#     return list(dict.fromkeys(lst))

# # 16. Second Largest Distinct Number
# def second_largest(lst):
#     values = sorted(set(lst))
#     return values[-2] if len(values) >= 2 else None

# # 17. First n Fibonacci Numbers
# def fibonacci(n):
#     a, b = 0, 1
#     result = []
#     for i in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result

# # 18. Percentage and Grade
# def percentage_grade(marks):
#     percentage = sum(marks) / 5
#     if percentage >= 90:
#         grade = "A"
#     elif percentage >= 75:
#         grade = "B"
#     elif percentage >= 60:
#         grade = "C"
#     elif percentage >= 40:
#         grade = "D"
#     else:
#         grade = "F"
#     return percentage, grade

# # 19. Electricity Bill Using Slabs
# def electricity_bill(units):
#     bill = 0
#     if units <= 100:
#         bill = units * 3
#     elif units <= 200:
#         bill = 100 * 3 + (units - 100) * 5
#     else:
#         bill = 100 * 3 + 100 * 5 + (units - 200) * 8
#     return bill

# # 20. Gross Salary
# def gross_salary(basic):
#     hra = basic * 0.20
#     da = basic * 0.10
#     return basic + hra + da

# # 21. Total Bill After Discount
# def total_bill(prices, quantities, discount=10):
#     subtotal = sum(p * q for p, q in zip(prices, quantities))
#     return subtotal - subtotal * discount / 100

# # 22. Minimum, Maximum, Sum and Average
# def list_statistics(lst):
#     if not lst:
#         return None
#     return min(lst), max(lst), sum(lst), average(lst)

# # 23. Student Records
# def student_total(marks):
#     return sum(marks)

# def student_percentage(marks):
#     return sum(marks) / len(marks)

# def student_grade(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 75:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 40:
#         return "D"
#     return "F"

# def student_records(students):
#     results = []
#     for name, roll, marks in students:
#         total = student_total(marks)
#         percentage = student_percentage(marks)
#         grade = student_grade(percentage)
#         results.append((name, roll, total, percentage, grade))
#     for record in results:
#         print(record)
#     percentages = [r[3] for r in results]
#     print("Class Average:", average(percentages))
#     print("Highest Scorer:", max(results, key=lambda x: x[3]))
#     print("Lowest Scorer:", min(results, key=lambda x: x[3]))

# # 24. Bank Account
# balance = 0
# transactions = []

# def deposit(amount):
#     global balance
#     if amount > 0:
#         balance += amount
#         transactions.append("Deposited: " + str(amount))
#     return balance

# def withdraw(amount):
#     global balance
#     if amount <= 0:
#         return "Invalid amount"
#     if amount > balance:
#         return "Insufficient balance"
#     balance -= amount
#     transactions.append("Withdrawn: " + str(amount))
#     return balance

# def balance_enquiry():
#     return balance

# def transaction_history():
#     return transactions.copy()

# # 25. Library Management
# books = {}

# def add_book(book):
#     books[book] = True

# def issue_book(book):
#     if books.get(book) is True:
#         books[book] = False
#         return "Book issued"
#     return "Book unavailable"

# def return_book(book):
#     if book in books:
#         books[book] = True
#         return "Book returned"
#     return "Book not found"

# def search_book(book):
#     return "Available" if books.get(book) is True else (
#         "Issued" if book in books else "Not found"
#     )

# def display_books():
#     return [book for book, available in books.items() if available]

# # 26. Modular Electricity Bill
# def calculate_energy_charge(units):
#     if units <= 100:
#         return units * 3
#     elif units <= 200:
#         return 300 + (units - 100) * 5
#     return 800 + (units - 200) * 8

# def fixed_charge():
#     return 50

# def calculate_tax(amount):
#     return amount * 0.05

# def electricity_bill_final(units, discount=0):
#     subtotal = calculate_energy_charge(units) + fixed_charge()
#     subtotal -= subtotal * discount / 100
#     return subtotal + calculate_tax(subtotal)

# # 27. Hospital Bill
# def consultation_charges(amount):
#     return amount

# def laboratory_charges(amount):
#     return amount

# def medicine_charges(amount):
#     return amount

# def room_charges(amount):
#     return amount

# def hospital_bill(consultation, laboratory, medicine, room, category):
#     total = (
#         consultation_charges(consultation)
#         + laboratory_charges(laboratory)
#         + medicine_charges(medicine)
#         + room_charges(room)
#     )
#     discounts = {"general": 0, "senior": 10, "poor": 20}
#     discount = discounts.get(category.lower(), 0)
#     return total - total * discount / 100

# # 28. Product Invoice
# products = {}

# def add_product(name, price, quantity):
#     products[name] = [price, quantity]

# def remove_product(name):
#     return products.pop(name, None)

# def calculate_subtotal():
#     return sum(price * quantity for price, quantity in products.values())

# def coupon_discount(subtotal, discount):
#     return subtotal * discount / 100

# def calculate_gst(amount, rate=18):
#     return amount * rate / 100

# def generate_invoice(discount=0, gst_rate=18):
#     subtotal = calculate_subtotal()
#     after_discount = subtotal - coupon_discount(subtotal, discount)
#     gst = calculate_gst(after_discount, gst_rate)
#     print("Products:", products)
#     print("Subtotal:", subtotal)
#     print("Discount:", coupon_discount(subtotal, discount))
#     print("GST:", gst)
#     print("Final Invoice:", after_discount + gst)

# # 29. Recursive Binary Search
# def binary_search(lst, target, low=0, high=None):
#     if high is None:
#         high = len(lst) - 1
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if lst[mid] == target:
#         return mid
#     if target < lst[mid]:
#         return binary_search(lst, target, low, mid - 1)
#     return binary_search(lst, target, mid + 1, high)

# # 30. Decimal to Binary Using Recursion
# def decimal_to_binary(n):
#     if n < 0:
#         return "-" + decimal_to_binary(-n)
#     if n < 2:
#         return str(n)
#     return decimal_to_binary(n // 2) + str(n % 2)

# # 31. Recursive Palindrome
# def recursive_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return recursive_palindrome(s[1:-1])

# # 32. Functions as Arguments
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b if b != 0 else "Cannot divide by zero"

# def calculate(a, b, operation):
#     return operation(a, b)

# # 33. Lambda Square
# square = lambda n: n * n

# # 34. Lambda Cube
# cube = lambda n: n ** 3

# # 35. Lambda Even
# even = lambda n: n % 2 == 0

# # 36. Lambda Maximum
# maximum = lambda a, b: a if a > b else b

# # 37. Lambda Simple Interest
# simple_interest_lambda = lambda p, r, t: p * r * t / 100

# # 38. Squares Using map()
# def map_squares(numbers):
#     return list(map(lambda x: x ** 2, numbers))

# # 39. Cubes Using map()
# def map_cubes(numbers):
#     return list(map(lambda x: x ** 3, numbers))

# # 40. Sum Corresponding Elements
# def add_lists(a, b):
#     return list(map(lambda x, y: x + y, a, b))

# # 41. Even Numbers Using filter()
# def filter_even(numbers):
#     return list(filter(lambda x: x % 2 == 0, numbers))

# # 42. Prime Numbers Using filter()
# def filter_primes(numbers):
#     return list(filter(lambda x: is_prime(x), numbers))

# # 43. Positive Numbers Using filter()
# def filter_positive(numbers):
#     return list(filter(lambda x: x > 0, numbers))

# # 44. Numbers Greater Than 50
# def greater_than_50(numbers):
#     return list(filter(lambda x: x > 50, numbers))

# # 45. Words Longer Than Five Characters
# def long_words(words):
#     return list(filter(lambda word: len(word) > 5, words))

# # 46. Sort Words by Length
# def sort_words(words):
#     return sorted(words, key=lambda word: len(word))

# # 47. Sort Students by Marks
# def sort_students(students):
#     return sorted(students, key=lambda student: student[1])

# # 48. Sort Employees by Salary
# def sort_employees(employees):
#     return sorted(employees, key=lambda employee: employee[1])

# # 49. Student Marks Processing
# def process_student_marks(students):
#     marks = list(map(lambda s: s[1], students))
#     print("Average Marks:", average(marks))
#     print("Above 75:", list(filter(lambda s: s[1] > 75, students)))
#     print("Sorted Students:", sorted(students, key=lambda s: s[1]))

# # 50. Employee Processing
# def process_employee_records(employees):
#     high_salary = list(filter(lambda e: e[2] > 50000, employees))
#     increased = list(map(lambda e: (e[0], e[1], e[2] * 1.10), employees))
#     sorted_employees = sorted(employees, key=lambda e: e[2])
#     print("Salary Above 50000:", high_salary)
#     print("Salary Increased by 10%:", increased)
#     print("Sorted by Salary:", sorted_employees)

# # 51. Product Processing
# def process_products(items):
#     values = list(map(lambda p: (p[0], p[1], p[2], p[1] * p[2]), items))
#     expensive = list(filter(lambda p: p[1] > 1000, values))
#     sorted_values = sorted(values, key=lambda p: p[3])
#     print("Product Values:", values)
#     print("Products Above 1000:", expensive)
#     print("Sorted by Total Value:", sorted_values)

# # 52. Word Processing
# def process_words(words):
#     print("Word Lengths:", list(map(lambda w: (w, len(w)), words)))
#     print("Words Longer Than 5:", list(filter(lambda w: len(w) > 5, words)))
#     print("Sorted by Length:", sorted(words, key=lambda w: len(w)))


