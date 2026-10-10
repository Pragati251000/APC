# String length 
# s = input("Enter a string: ")
# count = 0

# for ch in s:
#     count += 1

# print("Length:", count)


# count consonenets,vowels,digits,spaces,special char.
# s = input("Enter a string: ")
# vowels = consonants = digits = spaces = special = 0

# # for ch in s:
#     if ch.lower() in "aeiou":
#         vowels += 1
#     elif ch.isalpha():
#         consonants += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     else:
#         special += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special characters:", special)


# #Reverse String

# s = input("Enter a string: ")
# rev = ""

# for ch in s:
#     rev = ch + rev

# print("Reversed string:", rev)


# #Palidrome check

# s = input("Enter a string: ")
# rev = ""

# for ch in s:
#     rev = ch + rev

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# #Count uppercase,lowercase

# s = input("Enter a string: ")
# upper = lower = 0

# for ch in s:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1

# print("Uppercase:", upper)
# print("Lowercase:", lower)


# #Replace character

# s = input("Enter a string: ")
# old = input("Enter character to replace: ")
# new = input("Enter new character: ")

# result = ""

# for ch in s:
#     if ch == old:
#         result += new
#     else:
#         result += ch

# print("Result:", result)


# #remove char.

# s = input("Enter a string: ")
# result = ""

# for ch in s:
#     if ch != " ":
#         result += ch

# print("String without spaces:", result)


# #Frequency of characters

# s = input("Enter a string: ")
# ch = input("Enter character: ")
# count = 0

# for c in s:
#     if c == ch:
#         count += 1

# print("Frequency:", count)


# #First and last character

# s = input("Enter a string: ")

# if s:
#     print("First character:", s[0])
#     print("Last character:", s[-1])
# else:
#     print("Empty string")

# #ASCII

# s = input("Enter a string: ")

# for ch in s:
#     print(ch, "=", ord(ch))


# #Word count

# s = input("Enter a sentence: ")
# words = s.split()

# print("Total words:", len(words))


# #Longest word

# s = input("Enter a sentence: ")
# words = s.split()

# if words:
#     longest = words[0]

#     for word in words:
#         if len(word) > len(longest):
#             longest = word

#     print("Longest word:", longest)
# else:
#     print("No words found")


# #Shortest word

# s = input("Enter a sentence: ")
# words = s.split()

# if words:
#     shortest = words[0]

#     for word in words:
#         if len(word) < len(shortest):
#             shortest = word

#     print("Shortest word:", shortest)
# else:
#     print("No words found")


# #Title case 

# s = input("Enter a sentence: ")
# print("Title case:", s.title())


# #Print dupicate character

# s = input("Enter a string: ")
# seen = ""
# duplicates = ""

# for ch in s:
#     if ch in seen and ch not in duplicates:
#         duplicates += ch
#     else:
#         seen += ch

# print("Duplicate characters:", duplicates)


# #Frequency of every charcter

# s = input("Enter a string: ")
# checked = ""

# for ch in s:
#     if ch not in checked:
#         count = 0

#         for c in s:
#             if c == ch:
#                 count += 1

#         print(ch, ":", count)
#         checked += ch


# #Anagram check

# s1 = input("Enter first string: ").replace(" ", "").lower()
# s2 = input("Enter second string: ").replace(" ", "").lower()

# if sorted(s1) == sorted(s2):
#     print("Anagrams")
# else:
#     print("Not anagrams")


# #Remove duplicate

# s = input("Enter a string: ")
# result = ""

# for ch in s:
#     if ch not in result:
#         result += ch

# print("Result:", result)


# #Substring search

# s = input("Enter main string: ")
# sub = input("Enter substring: ")

# if sub in s:
#     print("Substring found")
# else:
#     print("Substring not found")


# #Count occurrence of word

# s = input("Enter a sentence: ")
# word = input("Enter word to count: ")

# words = s.split()
# count = 0

# for w in words:
#     if w == word:
#         count += 1

# print("Occurrences:", count)


# #Password validator

# s = input("Enter password: ")

# upper = lower = digit = special = False

# for ch in s:
#     if ch.isupper():
#         upper = True
#     elif ch.islower():
#         lower = True
#     elif ch.isdigit():
#         digit = True
#     else:
#         special = True

# if len(s) >= 8 and upper and lower and digit and special:
#     print("Valid password")
# else:
#     print("Invalid password")

# #Run length encoding

# s = input("Enter a string: ")
# result = ""
# count = 1

# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         result += s[i - 1] + str(count)
#         count = 1

# if s:
#     result += s[-1] + str(count)

# print("Compressed string:", result)


# #String compression

# s = input("Enter a string: ")
# result = ""
# count = 1

# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         result += s[i - 1] + str(count)
#         count = 1

# if s:
#     result += s[-1] + str(count)

# if len(result) < len(s):
#     print("Compressed string:", result)
# else:
#     print("Original string:", s)


# #Most requent char

# s = input("Enter a string: ")
# max_count = 0
# most = ""

# for ch in s:
#     count = 0

#     for c in s:
#         if c == ch:
#             count += 1

#     if count > max_count:
#         max_count = count
#         most = ch

# if s:
#     print("Most frequent character:", most)
#     print("Frequency:", max_count)
# else:
#     print("Empty string")


# #Second most frequent character

# s = input("Enter a string: ")
# freq = {}

# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1

# items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# if len(items) >= 2:
#     print("Second most frequent character:", items[1][0])
#     print("Frequency:", items[1][1])
# else:
#     print("No second character")


# #Caesar and cipher

# s = input("Enter a message: ")
# shift = int(input("Enter shift value: "))

# encrypted = ""

# for ch in s:
#     if ch.isupper():
#         encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
#     elif ch.islower():
#         encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
#     else:
#         encrypted += ch

# print("Encrypted message:", encrypted)

# decrypted = ""

# for ch in encrypted:
#     if ch.isupper():
#         decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
#     elif ch.islower():
#         decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
#     else:
#         decrypted += ch

# print("Decrypted message:", decrypted)


# #Email editor

# email = input("Enter email address: ")

# if email.count("@") == 1:
#     name, domain = email.split("@")

#     if name and "." in domain and not domain.startswith(".") and not domain.endswith(".") and ".." not in email:
#         print("Valid email")
#     else:
#         print("Invalid email")
# else:
#     print("Invalid email")


# #word frequency dictionary

# s = input("Enter a paragraph: ").lower()
# words = s.split()
# freq = {}

# for word in words:
#     word = word.strip(".,!?;:")
#     if word:
#         freq[word] = freq.get(word, 0) + 1

# print("Word frequency:", freq)


# #sentence reversed

# s = input("Enter a sentence: ")
# words = s.split()
# words.reverse()

# print("Reversed sentence:", " ".join(words))

# #String rottation

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# if len(s1) == len(s2) and s2 in s1 + s1:
#     print("Yes")
# else:
#     print("No")


