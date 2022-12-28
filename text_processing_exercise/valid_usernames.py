usernames = input().split(', ')
for el in usernames:
    if 3 <= len(el) <= 16:
        if el.isalnum():
            print(el)
        elif '_' in el or '-' in el:
            print(el)
