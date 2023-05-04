from flask import Flask

app = Flask(__name__)
# made decorator make_bold make_empahsis make_underlined


def make_bold(function):
    def wrapper():
        bold_text = function()
        return "<b>"+function() + "</b>"
    return wrapper


def make_underlined(function):
    def wrapper():
        # bold_text = function()
        return "<u>"+function() + "</u>"
    return wrapper


def make_empahsis(function):
    def wrapper():
        # bold_text = function()
        return "<em>"+function() + "</em>"
    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
@make_bold
@make_underlined
@make_empahsis
def say_bye():
    return "Bye"

# after putting username in url whateven two input comes up in function


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!."


if __name__ == "__main__":
    app.run(debug=True)
