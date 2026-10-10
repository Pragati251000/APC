from array import array

a = array('i', [10, 20, 30, 40, 50])

print("Array elements:", a)

a.append(60)
print("After adding element:", a)

a.remove(30)
print("After removing element:", a)