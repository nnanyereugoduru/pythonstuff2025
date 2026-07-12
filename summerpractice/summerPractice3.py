import json
import os

path = r'C:\Users\Durun\OneDrive\Documents\term 1 freshman\c++ projects\PYTHONGOLDER\summerpractice\contactbook.json'

def add_contact(contact_book):
    user_name = input("enter the new contact name: ")
    phone_number = input("enter the persons number: ")
    email = input("enter email ")
    adress = input("address ")
    contact_book[user_name] = {"phone" : phone_number, "email" : email, "address" : adress}
    
    
def look_up_contact(contact_book):
    user_lookup = input("Enter user name correctly ")
    if user_lookup in contact_book:
        info = contact_book[user_lookup]
        print()
        print(">>>>> Curent available infomation")
        print(f"Phone : {info['phone']}")
        print(f"Email is : {info['email']}")
        print(f"address is : {info['address']}")
        print()
    else:
        print("not found")
    
def delete_contact(contact_book):
    user_delete = input("what contact u want to delete")
    if user_delete in contact_book:
        info = contact_book[user_delete]
        print()
        print(">>>>> Curent available infomation")
        print(f"Phone is {info['phone']}")
        print(f"Email : {info['email']}")
        print(f"address : {info['address']}")
        print()
        print("............deleting now")
        del contact_book[user_delete]
    else:
        print ("invalid")

def edit_contact(contact_book):
    user_edit = input("enter name correctly ")
    
    if user_edit in contact_book:
        info = contact_book[user_edit] 
        print("1. phone ") # deemed it too small for an options dictionary
        print("2. email ")
        print("3. address")
        check_1 = int(input("what do u want to edit "))
        if check_1 == 1:
            info["phone"] = input("enter new phone number: ")
        elif check_1 == 2:
            info["email"] = input("enter new email ")
        elif check_1 == 3:
            info["address"] = input("enter new address")
        else:
            print("invalid")
    else:
        print("name does not exist")

# added this          
if os.path.exists(path):
    with open(path, 'r' ) as file:
        contact_book = json.load(file)
else:            
    contact_book = {}
    with open(path, 'w') as file:
        json.dump(contact_book, file, indent= 4)

online = True

options = {1: add_contact,
           2: look_up_contact, 
            3: delete_contact, 
            4: edit_contact,
           }
while online:
    print ("menu")
    print ("1. add a contact")
    print ("2. Look up a contact")
    print("3. delete contact")
    print("4. edit ")
    print("5. quit")

    try:
        user_choice = int(input("which number do u choose only choose the number "))
        if user_choice == 5:
            online = False
        elif user_choice in options:
            options[user_choice](contact_book)
            with open(path, 'w') as file:
                json.dump(contact_book, file, indent=4)
        else:
            print('invalid')
    except ValueError:
        print("invalid try again")