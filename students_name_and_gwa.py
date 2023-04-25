# read a file contains names of student together with gwa
with open("students_name_gwa.txt", "r") as student_name_gwa:
    # split name and gwa
    students_files = {}
    for line in student_name_gwa:
        name, gwa = line.strip().split(",")
        students_files[name] = float(gwa)
# output name of student with the highest gwa
highest_student = min(students_files.values())
for name, gwa in students_files.items():
    if gwa == highest_student:
        print('\033[0;30;47m*' *150)
        print(f"The student who has the highest gwa is {name} with gwa of {gwa}".center(150, "*"))
        print('\033[0;30;47m*' *150)