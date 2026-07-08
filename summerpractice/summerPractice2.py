import random

def get_random_number():
    return random.randint(1,100)

a = get_random_number()

count = 0
while True:
    count += 1
    try:
        user_input = input("Enter a random number ")
        user_number = int(user_input)
        
        if user_number > a:
            print("too high")
        elif user_number == a:
            print("thats right")
            print("got it in " + str(count) + " times ")
            break
        else:
            print("too low")
    except ValueError:
        print("Please enter a valid number")
        