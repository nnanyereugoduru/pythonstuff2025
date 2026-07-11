import openpyxl
import random

# create a new workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Student Grades"

# header row
ws.append(['ID', 'Math', 'English', 'Science', 'Average', 'GRADE'])

# student data



students = [[f"ST-{i:04d}", random.randint(60, 100), random.randint(60, 100), random.randint(60, 100)] for i in range(500)]


for student in students:
    id = student[0]
    math, english, science = student[1], student[2], student[3]
    average = round((math + english + science) / 3, 2)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    ws.append([id, math, english, science, average, grade])
   
# save
wb.save('student_grades.xlsx')
print("spreadsheet saved")