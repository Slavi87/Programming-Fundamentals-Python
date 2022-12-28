vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
final_string = list(i for i in text if i not in vowels)
print(''.join(final_string))
