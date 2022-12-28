def sum_of_digits(num):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in num:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number = input()

print(sum_of_digits(number))
