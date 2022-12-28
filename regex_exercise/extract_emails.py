import re

pattern = r"\b([a-z0-9\.\_\-]+@[a-z\.\-]+)\b"
text = input()
matches = re.findall(pattern, text)
print('\n'.join(matches))