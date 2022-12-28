def tribonacci_sequence(n):
    if n < 1:
        return
    first = 1
    second = 1
    third = 2
    print(first,"", end="")
    if n > 1:
        print(second,"", end="")
    if n >= 2:
        print(third,"", end="")
    for i in range(3, n):
        current_num = first + second + third
        first = second
        second = third
        third = current_num

        print(current_num,"", end="")


number = int(input())
tribonacci_sequence(number)

