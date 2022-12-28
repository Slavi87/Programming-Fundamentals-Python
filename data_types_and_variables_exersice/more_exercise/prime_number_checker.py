num = int(input())
not_prime = False
# if num > 1:
for i in range(2, num):
    if (num % i) == 0:
        not_prime = True
        break
if not_prime:
    print("False")

else:
    print("True")