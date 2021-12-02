def gradingStudents(grades):

    grades_length = len(grades)
    result = []
    i=0

    while i<grades_length:
        if grades[i]>=38 and ((grades[i] - grades[i] % 5) + 5) -grades[i]<3:
            a = (grades[i] - grades[i] % 5) + 5
        else:
            a = grades[i]
        i += 1
        result.append(a)
    return result

q = int(input("type quantity:").strip())

total = []

for turkey in range(q):
    istanbul = int(input("type numbers:").strip())
    total.append(istanbul)
print(gradingStudents(total))
