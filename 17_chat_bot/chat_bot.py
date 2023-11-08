from difflib import get_close_matches
import json
import datetime
import sys

def get_best_match(user_question: str, questions: dict) -> str | None:
    """Compares the user message similarity to the ones in the dictionary"""

    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6) #n=1 = only one as response. cutoff it's the grade of recognize

    # Return the first best match, else return None
    if matches:
        return matches[0]


def chatbot(knowledge: dict):
    """Chatbot"""

    while True:
        user_input: str = input('You: ')
        
        #take the current time
        current_day_and_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        brain['do you know what the time is?'] = f"Date and Time is: {current_day_and_time}"

        # Finds the best match, otherwise returns None
        best_match: str | None = get_best_match(user_input, knowledge)

        # Gets the best match from the knowledge base
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        elif user_input == "exit":
            print("Exiting the BOT...")
            sys.exit(1)
        else:
            print('Bot: I don\'t understand... Could you try rephrasing that?')


if __name__ == "__main__":

    with open('.\data_json.json', 'r') as json_file:
        brain: dict = json.load(json_file)

        print(brain)

    chatbot(knowledge=brain)
