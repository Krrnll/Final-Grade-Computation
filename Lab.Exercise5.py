# Kris Rainiell D. Basco
# November 10, 2025
# This program computes the final grade of a students using loopings.

print("Welcome to Grades Computation")

# Lecture Class Standing Grade Input
print("\nClass Standing (Lecture) 70%")

# Collection of Number of Assignments, Projects, Recitations, and Quizzes
print()
num_assignments_lec = int(input("Enter the number of Lecture Assignments: "))
num_projects_lec = int(input("Enter the number of Lecture Projects: "))
num_recitations_lec = int(input("Enter the number of Lecture Recitations: "))
num_quizzes_lec = int(input("Enter the number of Lecture Quizzes: "))

# Collection of Lecture Assignment Grades
print("\nEnter Lecture Assignment Grades:")
assignment_total_lec = 0
for i in range(num_assignments_lec):
    assignment_grade = float(input(f"  Assignment {i+1}: "))
    assignment_total_lec += assignment_grade
assignment_lec = assignment_total_lec / num_assignments_lec if num_assignments_lec > 0 else 0

# Collection of Lecture Project Grades
print("\nEnter Lecture Project Grades:")
project_total_lec = 0
for i in range(num_projects_lec):
    project_grade = float(input(f"  Project {i+1}: "))
    project_total_lec += project_grade
project_lec = project_total_lec / num_projects_lec if num_projects_lec > 0 else 0

# Collection of Lecture Recitation Grades
print("\nEnter Lecture Recitation Grades:")
recitation_total_lec = 0
for i in range(num_recitations_lec):
    recitation_grade = float(input(f"  Recitation {i+1}: "))
    recitation_total_lec += recitation_grade
recitation_lec = recitation_total_lec / num_recitations_lec if num_recitations_lec > 0 else 0

# Collection of Lecture Quiz Grades
print("\nEnter Lecture Quiz Grades:")
quiz_total_lec = 0
for i in range(num_quizzes_lec):
    quiz_grade = float(input(f"  Quiz {i+1}: "))
    quiz_total_lec += quiz_grade
quiz_lec = quiz_total_lec / num_quizzes_lec if num_quizzes_lec > 0 else 0

# Lecture Examination Grade Input
print()
print("Examination (Lecture) 30%")

print()
examination_lec = float(input("Enter your Examination Grade (30%): "))

# Lecture Grade Computation
lecture_computation = (assignment_lec * 0.15) + (project_lec * 0.20) + (recitation_lec * 0.10) + (quiz_lec * 0.25)
total_lecture_computation = (lecture_computation) + (examination_lec * 0.30)


# Laboratory Class Standing Grade Input
print("\n\nClass Standing (Laboratory) 30%")

# Collection of Number of Assignments, Projects, Recitations, and Quizzes
print()
num_assignments_lab = int(input("Enter the number of Laboratory Assignments: "))
num_projects_lab = int(input("Enter the number of Laboratory Projects: "))
num_recitations_lab = int(input("Enter the number of Laboratory Recitations: "))
num_quizzes_lab = int(input("Enter the number of Laboratory Quizzes: "))

# Collection of Laboratory Assignment Grades
print("\nEnter Laboratory Assignment Grades:")
assignment_total_lab = 0
for i in range(num_assignments_lab):
    assignment_grade = float(input(f"  Assignment {i+1}: "))
    assignment_total_lab += assignment_grade
assignment_lab = assignment_total_lab / num_assignments_lab if num_assignments_lab > 0 else 0

# Collection of Laboratory Project Grades
print("\nEnter Laboratory Project Grades:")
project_total_lab = 0
for i in range(num_projects_lab):
    project_grade = float(input(f"  Project {i+1}: "))
    project_total_lab += project_grade
project_lab = project_total_lab / num_projects_lab if num_projects_lab > 0 else 0

# Collection of Laboratory Recitation Grades
print("\nEnter Laboratory Recitation Grades:")
recitation_total_lab = 0
for i in range(num_recitations_lab):
    recitation_grade = float(input(f"  Recitation {i+1}: "))
    recitation_total_lab += recitation_grade
recitation_lab = recitation_total_lab / num_recitations_lab if num_recitations_lab > 0 else 0

# Collection of Laboratory Quiz Grades
print("\nEnter Laboratory Quiz Grades:")
quiz_total_lab = 0
for i in range(num_quizzes_lab):
    quiz_grade = float(input(f"  Quiz {i+1}: "))
    quiz_total_lab += quiz_grade
quiz_lab = quiz_total_lab / num_quizzes_lab if num_quizzes_lab > 0 else 0

# Laboratory Examination Grade Input
print()
print("Midterm Examination (Laboratory) 30%")

print()
midterm_lab = float(input("Enter your Midterm Laboratory Examination Grade (30%): "))

# Laboratory Grade Computation
laboratory_computation = (assignment_lab * 0.15) + (project_lab * 0.20) + (recitation_lab * 0.10) + (quiz_lab * 0.25)
total_laboratory_computation = (laboratory_computation) + (midterm_lab * 0.30)

# Final Grade Computation
print("\nFinal Grade Lecture (70%) + Laboratory (30%)")
final_grade = (total_lecture_computation * 0.70) + (total_laboratory_computation * 0.30)

# Equivalent and Remarks Section
print()
if final_grade >= 96.5:
    equivalent = 1.00
    remarks = ("You Passed!!!")
elif final_grade >= 93.5:
    equivalent = 1.25
    remarks = ("You Passed!!!")
elif final_grade >= 90.5:
    equivalent = 1.50
    remarks = ("You Passed!!!")
elif final_grade >= 87.5:
    equivalent = 1.75
    remarks = ("You Passed!!!")
elif final_grade >= 84.5:
    equivalent = 2.00
    remarks = ("You Passed!!!")
elif final_grade >= 81.5:
    equivalent = 2.25
    remarks = ("You Passed!!!")
elif final_grade >= 78.5:
    equivalent = 2.50
    remarks = ("You Passed!!!")
elif final_grade >= 75.5:
    equivalent = 2.75
    remarks = ("You Passed!!!")
elif final_grade >= 74.5:
    equivalent = 3.00
    remarks = ("You Passed!!!")
else:
    equivalent = 5.00
    remarks = ("You Failed!!!")

print(f"Your Final Grade is {final_grade:.2f} which is equivalent to {equivalent:.2f} {remarks}")