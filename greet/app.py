from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")
def welcome():
  return "welcome"

@app.route('/welcome/home')
def welcome_home():
  return "welcome home"

@app.route('/welcome/back')
def welcome_back():
  return "welcome back"

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
