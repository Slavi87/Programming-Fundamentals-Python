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



# def factorial(number):
#     for current_num in range(1, number):
#         number *= current_num
#     return number
#
#
# first_number = int(input())
# second_number = int(input())
# first_number_factorial = factorial(first_number)
# second_number_factorial = factorial(second_number)
# final_factorial_result = first_number_factorial / second_number_factorial
# print(f'{final_factorial_result:.2f}')
