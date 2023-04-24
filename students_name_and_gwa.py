import re
students_gwa = []
# read a file contains names of student together with gwa
with open("students_name_gwa.txt", "r") as student_name_gwa, open("students_name.txt", "a") as student_name, open("students_gwa.txt", "a") as student_gwa:
    for line in student_name_gwa:
        for i in re.findall(r'\d+(?:\.\d+)?', line):
            students_gwa.append(i)
            student_gwa.write(str(students_gwa) + "\n")
# output name of student with the highest gwa