import sys


def center_point(x1, y1, x2, y2):
    nums_x = [x1, x2]
    nums_y = [y1, y2]
    min_diff_x = sys.maxsize
    min_diff_y = sys.maxsize
    for i in nums_x:
        if abs(i - 0) < min_diff_x:
            min_diff_x = i
        elif abs(i - 0) == min_diff_x:
            continue
    for j in nums_y:
        if abs(j - 0) < min_diff_y:
            min_diff_y = j
        elif abs(j - 0) == min_diff_y:
            continue
    return f'({int(min_diff_x)}, {int(min_diff_y)})'


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(center_point(x_1, y_1, x_2, y_2))