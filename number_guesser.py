import random

print("Hello!")
print("Welcome to 'Guess the number game'.")
print('How the game works: you will enter a number and that will be your range to guess the number!')
top_range = input('Type a number to begin: ')

# .isdigit() checks if the number is digit and not a string 
if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print ('Please enter a number larger than 0.')
        quit()

else: 
    print('Please enter a number!')
    quit()

random_number = random.randint(0, top_range)

guesses = 0


while True:
    guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Please enter a number!")
        continue


    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print('Guess lower!')
    else: 
        print('Guess higher!')



print("you got it in", guesses, "guesses")