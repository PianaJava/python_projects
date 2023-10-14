from random import randint

# Start the program with basic setup
min, max = 1, 10
random_number: int = randint(min, max)
print(f'Guess the number in the range from {min} to {max}.')

x=1
max_attempts = 3

# Run an infinite loop for the game till 3 guess
while x <= max_attempts:
    # Get the user guess
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue
    
    # Check the user guess
    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print('You guessed it!')
        break
    x += 1

# If the loop exits without a correct guess
if x > max_attempts:
    print(f"GAME OVER! The correct number was {random_number}.")