words = input().split()
palindrome = input()

palindrome_lst = ([el for el in words if el == el[::-1]])

# if palidrome in palidrome_lst:
counter = palindrome_lst.count(palindrome)
print(palindrome_lst)
print(f'Found palindrome {counter} times')

