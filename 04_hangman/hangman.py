from random import choice


def run_game():
    word_input: str = choice(['apple', 'secret', 'banana'])     #pick random word_input among those 

    # A friendly interactive welcome message
    username: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {username}!')

    # Setup
    guessed: str = ''  # Will contain all the letters used to guess
    attempts: int = 3  # Set the amount of attempts you want the user to have

    # The game
    while attempts > 0:
        blanks: int = 0

        print('Word: ', end=' ')
        for char in word_input:
            if char in guessed:
                print(char, end=' ')
            else:
                print('_', end=' ')
                blanks += 1

        print()  # Add a blank line

        # If there are no blanks left, that means the user won the game!
        if blanks == 0:
            print('You got it!')
            break

        # Get user input
        guess: str = input('Enter a letter: ')

        # Check that the user isn't just guessing the same letter again
        if guess in guessed:
            print(f'You already used: "{guess}". Please try with another letter!')
            continue

        if len(guess) == 1:
            guessed += guess 

        # Check that the guess is in the input word
        if guess not in word_input and len(guess)==1:
            attempts -= 1
            print(f'Sorry, that was wrong... ({attempts} attempts remaining)')
            # Add the guess to the guessed string
        
        #check length string and word input 
        elif len(guess) > 1 and guess != word_input: 
            print(f"ERROR!!!!, It's only possible to add more than one letter to guess the word, try again, you still have {attempts} attempts)")
            continue

        elif guess == word_input:
            print('You got it!')
            break

        # Game-over if attempts reaches 0
        if attempts == 0:
            print('No more attempts remaining... You lose.')
            break


if __name__ == '__main__':
    run_game()
