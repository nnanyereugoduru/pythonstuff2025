import random

a = random.randint(1,100)
count = 0

while True:
    try:
        user_input = int(input("Enter a random number "))
        count += 1
        
        if user_input > a:
            print("too high")
        elif user_input == a:
            print("thats right")
            print(f'got it in {count} {'guess' if count == 1 else 'guesses'}')
            break
        else:
            print("too low")

    except ValueError:
        print("Please enter a valid number")
        