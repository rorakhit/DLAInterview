import os
from flask import Flask, redirect, render_template, request, url_for
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fb9804937eae1df6a619ec3b44d8368e90cc064a1ae5196c'


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form.get('project-input')
        validated_expression = validate_input(input_text)
        return redirect(url_for('answer', input_expression=validated_expression))
    print(os.path)
    return render_template("project.html")

def validate_input(text):
    # get rid of whitespace
    text = text.replace(" ", "")

    # use regex to get the proper pattern (number, +-*/, number)
    result = re.fullmatch('^(\d+)([\+\-\*\/])(\d+)$', text)

    if result == None:
        raise TypeError("Invalid input expression. Please only use +, -, *, and / operations and 2 numeric values on either side of the operation.")
    elif result.group(2) == '/' and int(result.group(3)) == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    else:
        return result.group(0)

@app.route("/answer", methods=['GET'])
def answer():
    expression = request.args.get('input_expression')
    # I'm only using eval here because I'm confident that my regex will keep invalid operations from happening
    # but it could still probably be overloaded with huge numbers maybe?
    answer = eval(expression)
    return render_template("answer.html", expression=expression, answer=answer)

@app.errorhandler(TypeError)
@app.errorhandler(ZeroDivisionError)
def error_handling(e):
    return render_template('error.html', error=e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)