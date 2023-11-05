import itertools             
import string
import time


def common_guess(word: str) -> str | None:
    """Checks a file filled with common words"""

    with open('words.text', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'


# Goes through every combination of chars
def brute_force(word: str, length: int, digits: bool, symbols: bool) -> str | None:
    """Performs brute force on finding a word"""

    # Modify this for total symbols
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length): # the function generates all possible combinations of characters from the chars iterable with a specified length length
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'
        # print(guess, attempts) # Comment this out when you're not testing


def input_val(type_input: string) -> bool:
    retry: bool = True
    while retry:
        input_value: str = input(f"Do you want to use {type_input}? Y/N: ")
        if input_value.lower() == "y":
            use_it: bool = True
            retry = False
        elif input_value.lower() == "n":
            use_it: bool = False
            retry = False
    return use_it


def main():
    print('Searching...')
    password: str = 't91#'

    # Search for common words before using the actual brute force
    if common_match := common_guess(password): #"walrus operator" (:=) in your code to assign the result of the brute_force function to the cracked variable while also checking if the result is truthy. 
        print(common_match)
    else:
        include_digits = input_val("digits") 
        include_symbols = input_val("symbols")
        start_time: float = time.perf_counter()
        for i in range(3,5):
            if cracked := brute_force(password, length=i, digits=include_digits, symbols=include_symbols):
                print(cracked)
                break
            else:
                print('There was no match...')
        end_time: float = time.perf_counter()
        # Display the time it took
        print("Time for the research: ", round(end_time - start_time, 2), 's')

if __name__ == '__main__':
    main()
