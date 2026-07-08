
import random
import json
import os

file_path = 'C:\\Users\\Durun\\OneDrive\\Documents\\term 1 freshman\\c++ projects\\PYTHONGOLDER\\studentRoster\\newstudentscores.json'

def update_grades(chart):
    user_input = input("Enter the person u want to change their grade ")
    if user_input in chart:
        info = chart[user_input]
        print("1. Math")
        print("2. English")
        print("3. Science ")
        user_input_2 = int(input("choose grade to update: "))
        if user_input_2 == 1:
            info["Math"] = int(input("Enter new grade: "))
        elif user_input_2 == 2:
            info["English"] = int(input("Enter new grade: "))
        elif user_input_2 == 3:
            info["Science"] = int(input("Enter new grade: "))
        else:
            print("invalid")
            return
        
        with open(file_path, 'w') as file:
            json.dump(chart, file, indent= 4)
        print('saved')

        for name, grade in chart.items():
            print()
            print(">>>>" + name)
            for subject, score in grade.items():
                print("\t " + subject + ": " + str(score))
    

def grade_stuff(chart):
    class_average = 0
    for name, grade in chart.items():
        print(">>> " + name)
        new_score = 0
        for subject, score in grade.items():
            new_score += score
        class_average += new_score/3
        new_score_2 = new_score/3
        print("Average is : " + str(new_score_2))
        
        print()
    print("Class average is : " + str(class_average/len(chart)))

    print()
    print(">>>>> RANKING <<<<<")
    rank = 1
    for name, grade in sorted(chart.items(), key=lambda x: sum(x[1].values()) / len(x[1]), reverse=True):
        avg = sum(grade.values()) / len(grade)
        print(str(rank) + ". " + name + " - " + str(round(avg, 2)))
        rank += 1  
          
def student(chart):
    for name, grade in chart.items():
        print()
        print(">>>>" + name)
        for subject, score in grade.items():
            print(f"\t {subject}: {score}")
    

# random for testing reasons
if os.path.exists(file_path):
    with open(file_path,'r') as file:
        students = json.load(file)
    print("loading......")
else:
    students = {
        "Alice" : {"Math" : random.randint(1,100), "English": random.randint(1,100), "Science" : random.randint(1,100)},
        "David" : {"Math" : random.randint(1,100), "English": random.randint(1,100), "Science" : random.randint(1,100)},
        "Anthony" : {"Math" : random.randint(1,100), "English": random.randint(1,100), "Science" : random.randint(1,100)},
        "Carlos": {"Math" : random.randint(1,100), "English": random.randint(1,100), "Science" : random.randint(1,100)},
        "Patrick" : {"Math" : random.randint(1,100), "English": random.randint(1,100), "Science" : random.randint(1,100)},
    }
    with open(file_path, 'w') as file:
        json.dump(students, file,indent= 4 )
    print(f"data written in {file}")




while True:
    print()
    print("ROSTER SERVICES")
    print("brought to you by Patrick Incorporated")
    print(">>>>>>>> Menu <<<<<<<<<<")
    print("1. Students")
    print("2.Grades")
    print("3. update Grades")

    user_choice = input("what do you chose pick numbers only > ")
    try:
        updated_choice = int(user_choice)
        if updated_choice == 1:
            student(students)
        elif updated_choice == 2:
            grade_stuff(students)
        elif updated_choice == 3:
            update_grades(students)
        else:
            print("invalid")
            continue
    except ValueError:
        print("please enter a number")

