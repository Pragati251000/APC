import re

text = input("Enter social media post: ")

hashtags = re.findall(r"#[A-Za-z0-9_]+", text)

print("Hashtags:", hashtags)