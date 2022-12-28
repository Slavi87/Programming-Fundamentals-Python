def password_validator(password):
    validator = []
    if len(password) < 6 or len(password) > 10:
        validator.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        validator.append("Password must consist only of letters and digits")
    counter_of_digits = 0
    for digits in password:
        if digits.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        validator.append("Password must have at least 2 digits")
    return validator


password_input = input()
password_is_not_valid = password_validator(password_input)
if len(password_is_not_valid) == 0:
    print("Password is valid")
else:
    print('\n'.join(password_is_not_valid))
