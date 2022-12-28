numbers = input().split(', ')
numbers = list(map(int, numbers))
positive_numbers = [el for el in numbers if el >= 0]
negative_numbers = [el for el in numbers if el < 0]
even_numbers = [el for el in numbers if el % 2 == 0]
odd_numbers = [el for el in numbers if el % 2 != 0]
print(f'Positive: {str(positive_numbers)[1:-1]}')
print(f'Negative: {str(negative_numbers)[1:-1]}')
print(f'Even: {str(even_numbers)[1:-1]}')
print(f'Odd: {str(odd_numbers)[1:-1]}')