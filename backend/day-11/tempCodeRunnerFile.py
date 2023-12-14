import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'students.txt')

student_names = []

# Assuming 'students.txt' is in the same directory as 'main.py'
with open('students.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        student_names.append(line.strip())
    student_names.sort()

# Print or use student_names as needed
for name in student_names:
    print(name)