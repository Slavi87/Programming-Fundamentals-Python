def grade_txt():
    if grade < 3:
        return 'Fail'
    elif grade < 3.5:
        return 'Poor'
    elif grade < 4.5:
        return 'Good'
    elif grade < 5.5:
        return 'Very Good'
    else:
        return 'Excellent'


grade = float(input())


print(grade_txt())
