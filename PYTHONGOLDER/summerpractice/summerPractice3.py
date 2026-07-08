def add_contact(contact_book):
    user_name = input("enter the new contact name: ")
    phone_number = int(input("enter the persons number: "))
    email = input("enter email ")
    adress = input("address ")
    contact_book[user_name] = {"phone" : phone_number, "email" : email, "address" : adress}
    
    
def look_up_contact(contact_book):
    user_lookup = input("Enter user name correctly ")
    if user_lookup in contact_book:
        info = contact_book[user_lookup]
        print()
        print(">>>>> Curent available infomation")
        print("Phone " + str(info["phone"]))
        print("email " + str(info["email"]))
        print("address " + str(info["address"]))
        print()
    else:
        print("not found")
    
def delete_contact(contact_book):
    user_delete = input("what contact u want to delete")
    if user_delete in contact_book:
        info = contact_book[user_delete]
        print()
        print(">>>>> Curent available infomation")
        print("Phone " + str(info["phone"]))
        print("email " + str(info["email"]))
        print("address " + str(info["address"]))
        print()
        print("............deleting now")
        del contact_book[user_delete]
    else:
        print ("what u typed does not exist")

def edit_contact(contact_book):
    user_edit = input("enter name correctly ")
    
    if user_edit in contact_book:
        info = contact_book[user_edit]
        print("1. phone ")
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
            

        
contact_book = {}


while True:
    print ("menu")
    print ("1. add a contact")
    print ("2. Look up a contact")
    print("3. delete contact")
    print("4. edit ")
    print("5. quit")
    try:
        user_choice = int(input("which number do u choose only choose the number "))
        if user_choice > 5:
            print("invalid number")
            continue
        if user_choice == 1:
            add_contact(contact_book)
        elif user_choice == 2:
            look_up_contact(contact_book)
        elif user_choice == 3:
            delete_contact(contact_book)
        elif user_choice == 4:
            edit_contact(contact_book)
        else:
            break
    except ValueError:
        print("invalid try again")