import re

pattern = r"\d+"

text = input()
while text:
    matches = re.findall(pattern, text)
    if matches:
        print(' '.join(matches), end=' ')
    text = input()