number = int(input())
positive_list = []
negative_list = []
# positive_count = 0
# negative_sum = 0
for current_num in range(number):
    num = int(input())
    if num < 0:
        negative_list.append(num)
    else:
        positive_list.append(num)

print(positive_list)
print(negative_list)
print(f'Count of positives: {len(positive_list)}')
print(f'Sum of negatives: {sum(negative_list)}')
