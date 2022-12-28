n = int(input())
student_dict = {}
for i in range(n):
    name = input()
    grade = input()
    if name not in student_dict:
        student_dict[name] = []
    student_dict[name].append(float(grade))
for key, value in student_dict.items():
    avg = sum(value) / len(value)
    if avg >= 4.50:
        print(f"{key} -> {avg:.2f}")
