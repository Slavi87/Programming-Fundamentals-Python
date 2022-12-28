import re

regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()

valid_names = re.findall(regex, text)
print(*valid_names)