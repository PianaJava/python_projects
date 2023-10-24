import random
import sys


class RPS:
    def __init__(self):
        print('Welcome to RPS 9000!')

        # Moves for display
        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.my_wins = 0
        self.ai_wins = 0
        self.total_count = 0

    def play_game(self):
        # Get the user input and lower() it
        user_move: str = input('Rock, paper, or scissors? >> ').lower()

        # Give the user an option to exit
        if user_move == 'exit':
            print('Thanks for playing!')
            self.display_results()
            print("TOTAL NUMBER OF PLAYS: ", self.total_count)

            sys.exit()
        else:
        # Check that the user made a valid move, else try again
            if user_move not in self.valid_moves:
                print('Invalid move...')
                
                return self.play_game()

            # The AI's move
            ai_move: str = random.choice(self.valid_moves)

            self.display_moves(user_move, ai_move)
            self.my_wins, self.ai_wins = self.check_move(user_move, ai_move)
            print(f"Updated result, ME: {self.my_wins}, AI: {self.ai_wins}")
            self.total_count += 1

    def display_moves(self, user_move: str, ai_move: str):
        # Display everything nicely
        print('----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')

    def check_move(self, user_move: str, ai_move: str) :
        # The game logic

        if user_move == ai_move:
            print('It is a tie!')
            self.my_wins += 1
            self.ai_wins += 1

        elif (user_move == 'rock' and ai_move == 'scissors') or \
             (user_move == 'scissors' and ai_move == 'paper') or \
             (user_move == 'paper' and ai_move == 'rock'):
            print('You win!')
            self.my_wins += 1
        else:
            print('AI wins...')
            self.ai_wins += 1
        return self.my_wins, self.ai_wins
    
    def display_results(self):
        if self.my_wins > self.ai_wins:
            print("You won more games!")
        elif self.ai_wins > self.my_wins:
            print("AI won more games!")
        else:
            print("It's a tie!")

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()

        

