import re
student_gwa = []
student_name = []
# read a file contains names of student together with gwa
with open("students_name_gwa.txt", "r") as student_name_gwa:
    for line in student_name_gwa:
        for i in re.findall(r'\d+(?:\.\d+)?', line):
            student_gwa.append(i)
            if student_gwa >= 1.0:
                for i in re.findall(r'\f'):
                    student_name.append(i)
print(student_gwa)
# output name of student with the highest gwa