text = input().split()
output_text = [el for el in text if len(el) % 2 == 0]
print('\n'.join(output_text))