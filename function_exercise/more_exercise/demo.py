def multiplication_sign(first, second, third):
    result = first * second * third
    if result < 0:
        return 'negative'
    elif result > 0:
        return 'positive'
    elif result == 0:
        return 'zero'


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(multiplication_sign(first_num, second_num, third_num))