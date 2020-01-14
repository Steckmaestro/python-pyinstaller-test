from flask import Flask
from calc.functions import add_values

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, welcome to our mock calculator</h1></ br>' \
        '/add/<operand1>&<operand2>'


@app.route('/add/<operands>')
def addition(operands):
    oper1, oper2 = operands.split('&')
    result = add_values(oper1, oper2)
    return 'Result ' + str(result)


if __name__ == '__main__':
    app.run(debug=True)
