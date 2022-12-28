def palindrome_numbers(nums):
    palindrome_lst = []
    for el in nums:
        if el == el[::-1]:
            palindrome_lst.append("True")
        else:
            palindrome_lst.append("False")
    return palindrome_lst


numbers = input().split(', ')
print('\n'.join(palindrome_numbers(numbers)))