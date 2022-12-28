text = input().split()
char = {}
for el in text:
    for letter in el:
        if letter not in char:
            char[letter] = 0
        char[letter] += 1
for key, value in char.items():
    print(f"{key} -> {value}")