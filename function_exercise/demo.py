def factorial(num_1, num_2):
    first_result = 1
    second_result = 1
    for i in range(1, num_1 + 1):
        first_result *= i
    for j in range(1, num_2 + 1):
        second_result *= j
    return f'{first_result / second_result:.2f}'


first_num = int(input())
second_num = int(input())
print(factorial(first_num, second_num))
