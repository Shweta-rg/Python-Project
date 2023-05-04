from flask import Flask
from random import randrange

app = Flask(__name__)
guess_number = randrange(9)
print(guess_number)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route("/<int:number>")
def guess(number):
    if (guess_number == number):
        return "<p>You got it!!</p>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number < guess_number:
        return "<p>You are too low!!</p>" \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<p>You are high!!</p>" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
