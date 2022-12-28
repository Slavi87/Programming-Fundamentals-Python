numbers_of_lines = int(input())
capacity = 255
total_litters = 0
none_litters = 0
for i in range(numbers_of_lines):
    litters = int(input())
    if capacity - litters < 0:
        print("Insufficient capacity!")
        continue
    capacity -= litters
    total_litters += litters
print(total_litters)