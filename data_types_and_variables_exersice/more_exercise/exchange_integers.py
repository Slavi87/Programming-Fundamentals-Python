a = int(input())
b = int(input())

print('Before:')
print(f'a = {a}')
print(f'b = {b}')
a, b = b, a
print('After:')
print("a =", a,)
print("b =", b,)
