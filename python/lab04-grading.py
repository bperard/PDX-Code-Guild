score = int(input('On a scale of 0-100, how well did you?'))
grade = ''
if score > 100:
    grade = 'Overachiever'
elif score > 89:
    grade = 'A'
elif score > 79:
    grade = 'B'
elif score > 69:
    grade = 'C'
elif score > 59:
    grade = 'D'
elif score >= 0:
    grade = 'F'
else:
    grade = 'Leave'

print(grade)
