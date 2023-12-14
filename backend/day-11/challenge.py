student_names = []

with open('backend\day-11\students.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        student_names.append(line.strip())
    student_names.sort()

with open('backend\day-11\students.txt', 'w') as file:
    for names in student_names:
        file.write(names + "\n")