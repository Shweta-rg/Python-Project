from flask import Flask
from random import randrange

app = Flask(__name__)
guess_number = randrange(9)
print(guess_number)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


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
