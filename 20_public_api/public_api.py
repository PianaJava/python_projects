from flask import Flask, request
from random import randint, choice
from datetime import datetime


'''
Custom Public API
'''
app = Flask(__name__)

@app.route('/')    # first enf point
def index():
    """The home page of our api."""

    # Great the user with some random phrases and the date & time
    phrases: list[str] = ['Welcome to this page!', 'You are looking good today!', 'The weather is great!']
    return {'phrase': choice(phrases),
            'date': datetime.now()}

@app.route('/about') #Still to be extended
def about():
    return 'The about page'

@app.route('/api/random')  # /api/random?number=10000&text=helloworld the second endpoint
def random():
    """The random endpoint of our api."""

    # Define some queries for our api endpoint
    number_input = request.args.get('number', type=int)   #we want to get the argunet of number 
    text_input = request.args.get('text', type=str, default='default_text')

    # Check that the number is of the correct type before doing anything
    if isinstance(number_input, int):   # if number input is of type int
        return {
            'input': number_input,
            'random': randint(0, number_input),
            'text': text_input,
            'date': datetime.now()
        }
    else:
        return {'Error': 'Please only enter numbers.'}
    

@app.route('/api/testfunction')
def testfunction():
    #new functionality to be implemented in the future 
    return {"test": "TEST"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
