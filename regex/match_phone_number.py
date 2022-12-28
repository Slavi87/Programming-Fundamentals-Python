import re

regex = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
# regex = r"\+359([\s-])2(\1)\d{3}(\1)\d{4}"
text = input()
matches = re.finditer(regex, text)
valid_phones = [match.group() for match in matches]
print(', '.join(valid_phones))