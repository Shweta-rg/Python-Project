from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
def say_bye():
    return "<u><b>Bye<b><u>"

# after putting username in url whateven two input comes up in function


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!."


if __name__ == "__main__":
    app.run(debug=True)
