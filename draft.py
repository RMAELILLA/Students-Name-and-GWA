with open("students_name_gwa.txt", "r") as student_name_gwa:

    for line in student_name_gwa:
        line = line.rstrip().split(" ")
        if line.lstrip() >= 1.0:
            print(line)