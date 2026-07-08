import random

random_word = random.choice(['capital', 'the', 'quest', 'water', 'house', 'police', 'apple' , 'problem'])
guessed_letters = []
playing = True
lives = 9
while playing:
    user_input = input('\n enter a letter: ').lower().strip()
   
    if user_input in guessed_letters:
        print (" already guessed that")
        continue

    guessed_letters.append(user_input)
    count = 0
    if user_input not in random_word.lower():
            lives -= 1
            print(f'incorrect remaining lives are {lives}')
            if lives == 0:
                print(f"ggs good luck next time the word was: {random_word}")
                playing = False
    for letter in random_word.lower():
        if letter in guessed_letters:
            count += 1
            #print(f'{count} is right')
            print(letter, end=' ')

            if count == len(random_word):
                print('\n completed')
                print(random_word, end=' ')
                playing = False
               
        else:
            print('_', end=" ")