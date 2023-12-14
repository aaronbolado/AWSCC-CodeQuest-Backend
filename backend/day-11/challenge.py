student_names = []

# Assuming 'students.txt' is in the same directory as 'main.py'
with open('students.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        student_names.append(line.strip())
    student_names.sort()

for names in student_names:
    print(names)