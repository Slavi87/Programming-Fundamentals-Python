version = input().split('.')
version = list(map(int, version))
new_version = []
new_version.append(version[0])
new_version.append(version[1])
new_version.append(version[2] + 1)
if new_version[2] > 9:
    new_version[1] += 1
    if new_version[1] > 9:
        new_version[1] = 0
        new_version[0] += 1
    new_version[2] = 0
print(* new_version, sep='.')
