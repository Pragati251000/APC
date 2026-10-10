s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()

s1 = "".join(ch for ch in s1 if ch.isalnum())
s2 = "".join(ch for ch in s2 if ch.isalnum())

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")