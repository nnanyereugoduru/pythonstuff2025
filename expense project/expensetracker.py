import json
import os

file_path = r'C:\Users\Durun\OneDrive\Documents\term 1 freshman\c++ projects\PYTHONGOLDER\expense project\expenses.json'


def log_expense(log):
    print('choose the expense type: ')
    print('1. recreational')
    print('2. bills')
    print('3. food')
    print('4. shopping')
    print('5. other')
    user_input_choice = int(input('>> '))

    if user_input_choice == 1: 
        while True:
            try:      
                new1 = float(input('enter expenses(type letter to cancel): '))
                log['recreational'].append(new1)
                
            except ValueError:
                print("exiting...")
                break
    elif user_input_choice == 2:
       while True:
            try:
                new2 = float(input('enter expenses(letter to cancel): '))
                log['bills'].append(new2)
                
            except ValueError:
                print("exiting...")
                break
    elif user_input_choice == 3:
        while True:
            try:
                new3 = float(input('enter expenses(letter to cancel): '))
                log['food'].append(new3)
                
            except ValueError:
                print("exiting...")
                break

    elif user_input_choice == 4:
        while True:
            try:
                new4 = float(input('enter expenses(letter to cancel): '))
                log['shopping'].append(new4)
                
            except ValueError:
                print("exiting...")
                break

    elif user_input_choice == 5:
        while True:
            try:
                new5 = float(input('enter expenses(letter to cancel): '))
                log['other'].append(new5)
                
            except ValueError:
                print("exiting...")
                break

    else:
        print('invalid')

    with open(file_path, 'w') as file:
        json.dump(log, file , indent= 4)
    print('saved')
         
def check_log(log):
    for name, info in log.items():
        print()
        print(f'{name} : {info}')

def calculate(log):
    print('what calculations')
    print()
    print('1. averages')
    print('2. sum')
    user_choice = int(input('>> '))
    average = 0
    if user_choice == 1:
        for name, info in log.items():
            if len(info) > 0: 
                average = sum(info)/len(info)
                print(f'the average for {name} is {average:.2f}')     
            else:
                print(f'there are no numbers in {name}') 
    elif user_choice == 2:
        for name, info in log.items():
            if len(info) > 0:
                print(f'the sum of all spending in {name} is {sum(info)}')
            else:
                print(f'no info present in {name}')

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        log = json.load(file)
else: 
    log = {'recreational': [], 'bills': [], 'food': [], 'shopping' : [], 'other' : [], }
    with open(file_path, 'w') as file:
        json.dump(log, file, indent= 4)
    print('saved')

online = True
count = 0
while online:
    count += 1
    if count <= 1:
        print("welcome....")

    print("EXPENSE TRACKER")
    print("1. log expenses")
    print("2. check log")
    print("3. calculate")
    print("4. quit")
    user_choice = input("what will you proceed with (choose the number): ")  
    try:
            user_choice = int(user_choice)

            if user_choice == 1:
                log_expense(log)
            elif user_choice == 2:
                check_log(log)
            elif user_choice == 3:
                calculate(log)
            elif user_choice == 4:
                online = False
            else:
                print("try again..")
                continue
    except ValueError:
        print("invalid")    